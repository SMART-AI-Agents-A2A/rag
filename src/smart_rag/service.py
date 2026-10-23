import logging
import math
import re
from collections import defaultdict
from time import monotonic
from typing import Any

from smart_rag.corpus import load_corpus, split_corpus, summarize_documents
from smart_rag.models import (
    Answerability,
    DataQualityStatus,
    EvidenceItem,
    IngestResponse,
    MetadataFilters,
    QueryBreadth,
    QueryPlan,
    QueryRequest,
    QueryResponse,
    RetrievalAssessment,
)
from smart_rag.providers import OpenRouterClient, ProviderError
from smart_rag.settings import Settings
from smart_rag.store import QdrantStore, SearchCandidate

logger = logging.getLogger(__name__)
CITATION_PATTERN = re.compile(r"\[([^\[\]]+)\]")


class RagService:
    def __init__(
        self,
        settings: Settings,
        *,
        store: QdrantStore | None = None,
        provider: OpenRouterClient | None = None,
    ) -> None:
        self.settings = settings
        self.store = store or QdrantStore(settings)
        self._provider = provider

    @property
    def provider(self) -> OpenRouterClient:
        if self._provider is None:
            self._provider = OpenRouterClient(self.settings)
        return self._provider

    def close(self) -> None:
        self.store.close()
        if self._provider is not None:
            self._provider.close()

    def load_documents(self):
        return load_corpus(
            self.settings.documents_dir,
            default_language=self.settings.default_language,
            allowed_languages=self.settings.languages,
        )

    def list_documents(self):
        return summarize_documents(self.load_documents())

    def ingest(self, *, reset: bool = False) -> IngestResponse:
        documents = self.load_documents()
        current_hashes = {document.path: document.document_hash for document in documents}
        indexed_hashes = {} if reset else self.store.indexed_document_hashes()
        changed_documents = [
            document for document in documents if indexed_hashes.get(document.path) != document.document_hash
        ]
        removed_paths = sorted(set(indexed_hashes) - set(current_hashes))
        chunks = split_corpus(
            changed_documents,
            chunk_size=self.settings.chunk_size,
            chunk_overlap=self.settings.chunk_overlap,
        )

        vectors = self._embed_in_batches([chunk.content for chunk in chunks])
        vector_size = self._resolve_vector_size(vectors)
        self.store.ensure_collection(vector_size, reset=reset)

        chunks_by_document: dict[str, list[int]] = defaultdict(list)
        for index, chunk in enumerate(chunks):
            chunks_by_document[chunk.document_path].append(index)

        for document in changed_documents:
            indexes = chunks_by_document[document.path]
            document_chunks = [chunks[index] for index in indexes]
            document_vectors = [vectors[index] for index in indexes]
            old_ids = set() if reset else self.store.point_ids_for_document(document.path)
            self.store.upsert(document_chunks, document_vectors)
            new_ids = {chunk.id for chunk in document_chunks}
            self.store.delete_point_ids(old_ids - new_ids)

        for path in removed_paths:
            self.store.delete_document(path)

        return IngestResponse(
            collection=self.settings.collection_name,
            documents_total=len(documents),
            documents_indexed=len(changed_documents),
            documents_unchanged=len(documents) - len(changed_documents),
            documents_removed=len(removed_paths),
            chunks_indexed=len(chunks),
            reset=reset,
            embedding_model=self.settings.embedding_model,
            vector_size=vector_size,
        )

    def query(self, request: QueryRequest) -> QueryResponse:
        started = monotonic()
        fallback_plan = QueryPlan(
            original_query=request.query,
            breadth=QueryBreadth.FOCUSED,
            subqueries=[request.query],
            filters=request.filters or MetadataFilters(),
            planning_degraded=True,
        )
        if not self.store.collection_exists():
            return empty_query_response(
                request.query,
                fallback_plan,
                status=DataQualityStatus.NOT_AVAILABLE,
                limitation="qdrant_collection_not_available",
                metadata={"collection": self.settings.collection_name, "retrieval_configured": False},
            )

        plan = self._plan(request, fallback_plan)
        try:
            response = self._retrieve(request, plan)
        except Exception as exc:  # the API returns an auditable failure instead of leaking provider details
            logger.exception("RAG retrieval failed")
            return empty_query_response(
                request.query,
                plan,
                status=DataQualityStatus.SOURCE_ERROR,
                limitation="retrieval_source_error",
                metadata={
                    "collection": self.settings.collection_name,
                    "error_type": type(exc).__name__,
                    "latency_ms": elapsed_ms(started),
                },
            )
        response.metadata["latency_ms"] = elapsed_ms(started)
        return response

    def _plan(self, request: QueryRequest, fallback: QueryPlan) -> QueryPlan:
        if not self.settings.query_planning_enabled:
            return fallback
        try:
            planned = self.provider.plan(
                request.query,
                max_subqueries=self.settings.max_subqueries,
                vocabulary=self._planning_vocabulary(),
            )
            return planned.model_copy(update={"filters": planned.filters.merged_with(request.filters)})
        except Exception as exc:  # planner is fail-open by design
            logger.warning("query planning failed; using original query", extra={"error_type": type(exc).__name__})
            return fallback

    def _planning_vocabulary(self) -> dict[str, list[str]]:
        documents = self.load_documents()
        fields = ("language", "crop", "region", "topic", "document_type")
        return {field: sorted({str(getattr(document.metadata, field)) for document in documents}) for field in fields}

    def _retrieve(self, request: QueryRequest, plan: QueryPlan) -> QueryResponse:
        queries = plan.subqueries[: self.settings.max_subqueries]
        query_vectors = self.provider.embed(queries)
        candidate_limit = max(
            self.settings.rerank_candidates,
            min(request.top_k or self.settings.top_k, self.settings.max_top_k),
        )
        per_query_limit = max(1, math.ceil(candidate_limit / len(queries)))
        candidates_by_id: dict[str, SearchCandidate] = {}
        query_candidate_ids: dict[str, set[str]] = {}
        for query, vector in zip(queries, query_vectors, strict=True):
            hits = self.store.search(vector=vector, limit=per_query_limit, filters=plan.filters)
            query_candidate_ids[query] = {hit.id for hit in hits}
            for hit in hits:
                existing = candidates_by_id.get(hit.id)
                if existing is None or hit.score > existing.score:
                    candidates_by_id[hit.id] = hit

        candidates = sorted(candidates_by_id.values(), key=lambda item: item.score, reverse=True)
        scored, score_kind, rerank_degraded = self._score_candidates(request.query, candidates)
        limit = min(
            request.top_k or self.settings.top_k,
            self.settings.max_top_k,
            self.settings.global_evidence_limit,
        )
        threshold = (
            self.settings.rerank_score_threshold if score_kind == "rerank" else self.settings.vector_score_threshold
        )
        selected = select_candidates(
            scored,
            threshold=threshold,
            limit=limit,
            max_chunks_per_document=self.settings.max_chunks_per_document,
        )
        evidence = [
            to_evidence(candidate, score, score_kind, rank) for rank, (candidate, score) in enumerate(selected, 1)
        ]
        selected_ids = {candidate.id for candidate, _ in selected}
        covered = [query for query, ids in query_candidate_ids.items() if selected_ids.intersection(ids)]
        missing = [query for query in queries if query not in covered]
        assessment = self._assess(request.query, evidence, covered=covered, missing=missing)

        if not evidence:
            return empty_query_response(
                request.query,
                plan,
                status=DataQualityStatus.COLLECTION_GAP,
                limitation="no_candidate_above_threshold",
                metadata={
                    "collection": self.settings.collection_name,
                    "candidate_count": len(candidates),
                    "score_kind": score_kind,
                    "score_threshold": threshold,
                    "rerank_degraded": rerank_degraded,
                },
            )

        answer = None
        answer_error: str | None = None
        generate_answer = self.settings.answer_enabled if request.generate_answer is None else request.generate_answer
        if generate_answer:
            try:
                answer = self.provider.answer(query=request.query, evidence=evidence)
                validate_answer_citations(answer, evidence)
            except Exception as exc:  # evidence remains usable if generation fails
                logger.warning("answer generation failed", extra={"error_type": type(exc).__name__})
                answer_error = type(exc).__name__
                answer = None

        status = (
            DataQualityStatus.OK if assessment.answerability is Answerability.COMPLETE else DataQualityStatus.PARTIAL
        )
        return QueryResponse(
            query=request.query,
            status=status,
            answer=answer,
            evidence=evidence,
            plan=plan,
            assessment=assessment,
            metadata={
                "collection": self.settings.collection_name,
                "embedding_model": self.settings.embedding_model,
                "rerank_model": self.settings.rerank_model if score_kind == "rerank" else None,
                "candidate_count": len(candidates),
                "evidence_count": len(evidence),
                "score_kind": score_kind,
                "score_threshold": threshold,
                "rerank_degraded": rerank_degraded,
                "answer_model": self.settings.answer_model if answer is not None else None,
                "answer_error_type": answer_error,
            },
        )

    def _score_candidates(
        self,
        query: str,
        candidates: list[SearchCandidate],
    ) -> tuple[list[tuple[SearchCandidate, float]], str, bool]:
        vector_scored = [(candidate, candidate.score) for candidate in candidates]
        if not self.settings.rerank_enabled or not candidates:
            return vector_scored, "vector", False
        try:
            hits = self.provider.rerank(query=query, documents=[candidate.content for candidate in candidates])
            reranked = [(candidates[hit.index], hit.score) for hit in hits]
            if not any(score >= self.settings.rerank_score_threshold for _, score in reranked) and any(
                score >= self.settings.vector_score_threshold for _, score in vector_scored
            ):
                return vector_scored, "vector", False
            return reranked, "rerank", False
        except Exception as exc:
            logger.warning("rerank failed; preserving vector scores", extra={"error_type": type(exc).__name__})
            return vector_scored, "vector", True

    def _assess(
        self,
        query: str,
        evidence: list[EvidenceItem],
        *,
        covered: list[str],
        missing: list[str],
    ) -> RetrievalAssessment:
        limitations: list[str] = []
        answerability = Answerability.PARTIAL if evidence else Answerability.NOT_ANSWERABLE
        if missing:
            limitations.append("subquery_coverage_incomplete")
        if not evidence:
            limitations.append("no_relevant_documentary_evidence")
            return RetrievalAssessment(
                answerability=answerability,
                limitations=limitations,
                covered_subqueries=covered,
                missing_subqueries=missing,
            )
        if not self.settings.sufficiency_judge_enabled:
            limitations.append("retrieval_sufficiency_not_validated")
        elif not missing:
            try:
                verdict = self.provider.judge_sufficiency(query=query, evidence=evidence)
            except Exception as exc:
                logger.warning("sufficiency judge failed", extra={"error_type": type(exc).__name__})
                verdict = None
            if verdict is True:
                answerability = Answerability.COMPLETE
            elif verdict is False:
                limitations.append("retrieved_evidence_insufficient")
            else:
                limitations.append("retrieval_sufficiency_not_validated")
        return RetrievalAssessment(
            answerability=answerability,
            limitations=limitations,
            covered_subqueries=covered,
            missing_subqueries=missing,
        )

    def _embed_in_batches(self, texts: list[str]) -> list[list[float]]:
        vectors: list[list[float]] = []
        for start in range(0, len(texts), self.settings.embedding_batch_size):
            vectors.extend(self.provider.embed(texts[start : start + self.settings.embedding_batch_size]))
        return vectors

    def _resolve_vector_size(self, vectors: list[list[float]]) -> int:
        if vectors:
            dimensions = {len(vector) for vector in vectors}
            if len(dimensions) != 1:
                raise ProviderError("embedding batches returned inconsistent vector sizes")
            detected = dimensions.pop()
        elif self.store.collection_exists():
            detected = self.store.vector_size() or 0
        else:
            detected = self.provider.probe_dimension()
        if not detected:
            raise ProviderError("could not determine embedding dimension")
        if self.settings.embedding_dimension is not None and self.settings.embedding_dimension != detected:
            raise ProviderError(
                f"configured embedding dimension {self.settings.embedding_dimension} "
                f"differs from provider dimension {detected}"
            )
        return detected


def select_candidates(
    scored: list[tuple[SearchCandidate, float]],
    *,
    threshold: float,
    limit: int,
    max_chunks_per_document: int,
) -> list[tuple[SearchCandidate, float]]:
    selected: list[tuple[SearchCandidate, float]] = []
    per_document: dict[str, int] = defaultdict(int)
    for candidate, score in sorted(scored, key=lambda pair: pair[1], reverse=True):
        if score < threshold:
            continue
        document_path = str(candidate.metadata.get("document_path", "unknown"))
        if per_document[document_path] >= max_chunks_per_document:
            continue
        selected.append((candidate, score))
        per_document[document_path] += 1
        if len(selected) >= limit:
            break
    return selected


def to_evidence(candidate: SearchCandidate, score: float, score_kind: str, rank: int) -> EvidenceItem:
    metadata = candidate.metadata
    return EvidenceItem(
        evidence_id=f"rag:{candidate.id}",
        source=str(metadata.get("source") or metadata.get("document_path") or "document"),
        title=str(metadata.get("title") or metadata.get("document_path") or "Document"),
        content=candidate.content,
        score=score,
        score_kind=score_kind,
        rank=rank,
        document_path=str(metadata.get("document_path", "")),
        heading_path=str(metadata.get("heading_path", "")),
        language=str(metadata.get("language", "")),
        metadata={
            key: value
            for key, value in metadata.items()
            if key not in {"title", "source", "document_path", "heading_path", "language"}
        },
    )


def validate_answer_citations(answer: str, evidence: list[EvidenceItem]) -> None:
    allowed = {item.evidence_id for item in evidence}
    citations = set(CITATION_PATTERN.findall(answer))
    if not citations.intersection(allowed):
        raise ProviderError("generated answer does not cite retrieved evidence")
    unsupported = {citation for citation in citations if citation.startswith("rag:") and citation not in allowed}
    if unsupported:
        raise ProviderError("generated answer cites evidence that was not retrieved")


def empty_query_response(
    query: str,
    plan: QueryPlan,
    *,
    status: DataQualityStatus,
    limitation: str,
    metadata: dict[str, Any],
) -> QueryResponse:
    return QueryResponse(
        query=query,
        status=status,
        answer=None,
        evidence=[],
        plan=plan,
        assessment=RetrievalAssessment(
            answerability=Answerability.NOT_ANSWERABLE,
            limitations=[limitation],
            covered_subqueries=[],
            missing_subqueries=plan.subqueries,
        ),
        metadata=metadata,
    )


def elapsed_ms(started: float) -> int:
    return round((monotonic() - started) * 1000)
