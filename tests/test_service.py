from typing import Any

import pytest

from smart_rag.models import DataQualityStatus, EvidenceItem, QueryBreadth, QueryPlan, QueryRequest
from smart_rag.providers import ProviderError, RerankHit
from smart_rag.service import RagService, select_candidates, validate_answer_citations
from smart_rag.settings import Settings
from smart_rag.store import SearchCandidate


def candidate(identifier: str, score: float, document: str) -> SearchCandidate:
    return SearchCandidate(
        id=identifier,
        score=score,
        content=f"Technical passage {identifier}",
        metadata={
            "document_path": document,
            "source": f"{document}.pdf",
            "title": document,
            "heading_path": "Irrigation",
            "language": "en",
        },
    )


def test_selection_enforces_threshold_and_document_diversity() -> None:
    scored = [
        (candidate("1", 0.9, "a"), 0.9),
        (candidate("2", 0.8, "a"), 0.8),
        (candidate("3", 0.7, "b"), 0.7),
        (candidate("4", 0.2, "c"), 0.2),
    ]
    selected = select_candidates(scored, threshold=0.3, limit=3, max_chunks_per_document=1)
    assert [item.id for item, _ in selected] == ["1", "3"]


def test_answer_citations_must_reference_returned_evidence() -> None:
    evidence = [
        EvidenceItem(
            evidence_id="rag:one",
            source="source.pdf",
            title="Source",
            content="Evidence",
            score=0.9,
            score_kind="rerank",
            rank=1,
            document_path="source.md",
            heading_path="Section",
            language="en",
        )
    ]
    validate_answer_citations("Supported statement [rag:one].", evidence)
    with pytest.raises(ProviderError):
        validate_answer_citations("Unsupported statement [rag:other].", evidence)


class FakeStore:
    collection_name = "test"

    def collection_exists(self) -> bool:
        return True

    def search(self, **_: Any) -> list[SearchCandidate]:
        return [candidate("one", 0.8, "manual"), candidate("two", 0.7, "article")]

    def close(self) -> None:
        pass


class FakeProvider:
    def plan(self, query: str, **_: Any) -> QueryPlan:
        return QueryPlan(original_query=query, breadth=QueryBreadth.FOCUSED, subqueries=[query])

    def embed(self, texts: list[str]) -> list[list[float]]:
        return [[1.0, 0.0] for _ in texts]

    def rerank(self, **_: Any) -> list[RerankHit]:
        return [RerankHit(index=1, score=0.95), RerankHit(index=0, score=0.85)]

    def answer(self, **_: Any) -> str:
        return "Grounded answer [rag:two]."

    def close(self) -> None:
        pass


def test_query_pipeline_returns_grounded_answer_and_auditable_evidence() -> None:
    settings = Settings(
        openrouter_api_key="test",
        top_k=2,
        max_top_k=4,
        global_evidence_limit=4,
    )
    service = RagService(settings, store=FakeStore(), provider=FakeProvider())  # type: ignore[arg-type]
    response = service.query(QueryRequest(query="What supports drip irrigation?"))

    assert response.status is DataQualityStatus.PARTIAL
    assert response.answer == "Grounded answer [rag:two]."
    assert [item.evidence_id for item in response.evidence] == ["rag:two", "rag:one"]
    assert response.metadata["score_kind"] == "rerank"
    assert "retrieval_sufficiency_not_validated" in response.assessment.limitations
