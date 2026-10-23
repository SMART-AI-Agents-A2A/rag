import json
import logging
import time
from dataclasses import dataclass
from typing import Any

import httpx

from smart_rag.models import EvidenceItem, MetadataFilters, QueryBreadth, QueryPlan
from smart_rag.settings import Settings

logger = logging.getLogger(__name__)


class ProviderError(RuntimeError):
    """Normalized failure from an external model provider."""


@dataclass(frozen=True)
class RerankHit:
    index: int
    score: float


class OpenRouterClient:
    def __init__(self, settings: Settings, *, transport: httpx.BaseTransport | None = None) -> None:
        if not settings.openrouter_api_key:
            raise ProviderError("RAG_OPENROUTER_API_KEY is required")
        self.settings = settings
        self._client = httpx.Client(
            base_url=settings.openrouter_base_url.rstrip("/") + "/",
            timeout=settings.openrouter_timeout_seconds,
            transport=transport,
            headers={
                "Authorization": f"Bearer {settings.openrouter_api_key}",
                "Content-Type": "application/json",
                "User-Agent": "smart-rag/1.0",
            },
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "OpenRouterClient":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def embed(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        body = self._request_json(
            "embeddings",
            {"model": self.settings.embedding_model, "input": texts},
        )
        data = body.get("data")
        if not isinstance(data, list) or len(data) != len(texts):
            raise ProviderError("embedding response is missing vectors")
        vectors: list[list[float] | None] = [None] * len(texts)
        for entry in data:
            if not isinstance(entry, dict):
                raise ProviderError("embedding response contains an invalid item")
            index = entry.get("index")
            embedding = entry.get("embedding")
            if not isinstance(index, int) or not 0 <= index < len(texts):
                raise ProviderError("embedding response contains an invalid index")
            if not isinstance(embedding, list) or not embedding:
                raise ProviderError("embedding response contains an empty vector")
            vectors[index] = [float(value) for value in embedding]
        if any(vector is None for vector in vectors):
            raise ProviderError("embedding response contains duplicate or missing indexes")
        resolved = [vector for vector in vectors if vector is not None]
        dimensions = {len(vector) for vector in resolved}
        if len(dimensions) != 1:
            raise ProviderError("embedding response contains inconsistent dimensions")
        return resolved

    def probe_dimension(self) -> int:
        return len(self.embed(["SMART RAG embedding dimension probe"])[0])

    def rerank(self, *, query: str, documents: list[str]) -> list[RerankHit]:
        if not documents:
            return []
        body = self._request_json(
            "rerank",
            {
                "model": self.settings.rerank_model,
                "query": query,
                "documents": documents,
                "top_n": len(documents),
            },
        )
        results = body.get("results")
        if not isinstance(results, list):
            raise ProviderError("rerank response is missing results")
        hits: list[RerankHit] = []
        seen: set[int] = set()
        for entry in results:
            if not isinstance(entry, dict):
                continue
            index = entry.get("index")
            score = entry.get("relevance_score")
            if not isinstance(index, int) or not 0 <= index < len(documents) or index in seen:
                continue
            if not isinstance(score, int | float):
                continue
            seen.add(index)
            hits.append(RerankHit(index=index, score=float(score)))
        if len(hits) != len(documents):
            raise ProviderError("rerank response did not return a complete candidate permutation")
        return sorted(hits, key=lambda hit: hit.score, reverse=True)

    def plan(
        self,
        query: str,
        *,
        max_subqueries: int,
        vocabulary: dict[str, list[str]],
    ) -> QueryPlan:
        vocabulary_text = "; ".join(f"{field}: {', '.join(values)}" for field, values in vocabulary.items())
        prompt = (
            "Plan retrieval over a curated agricultural document index. Do not answer the question. "
            "Return JSON with breadth ('focused' or 'broad'), subqueries (one to four natural-language searches), "
            "and filters with optional language, crop, region, topic, and document_type. Use a broad plan only when "
            "the question contains independent aspects. Add a metadata filter only when the user explicitly "
            "requests it. "
            "Map filters only to the following canonical values and omit unsupported filters: "
            f"{vocabulary_text}. Preserve the query language."
        )
        body = self._chat_json(
            model=self.settings.query_model,
            temperature=self.settings.query_temperature,
            top_p=self.settings.query_top_p,
            max_tokens=700,
            messages=[{"role": "system", "content": prompt}, {"role": "user", "content": query}],
            json_response=True,
        )
        try:
            breadth = QueryBreadth(str(body.get("breadth", "focused")))
            raw_subqueries = body.get("subqueries")
            subqueries = [str(item) for item in raw_subqueries] if isinstance(raw_subqueries, list) else [query]
            raw_filters = body.get("filters") if isinstance(body.get("filters"), dict) else {}
            filters = sanitize_planned_filters(MetadataFilters.model_validate(raw_filters), vocabulary)
            return QueryPlan(
                original_query=query,
                breadth=breadth,
                subqueries=subqueries[:max_subqueries] or [query],
                filters=filters,
                planning_degraded=False,
            )
        except (TypeError, ValueError) as exc:
            raise ProviderError("query planner returned an invalid plan") from exc

    def judge_sufficiency(self, *, query: str, evidence: list[EvidenceItem]) -> bool | None:
        passages = "\n\n".join(
            f"[{item.evidence_id}] {item.source} — {item.heading_path}\n{item.content[:1800]}" for item in evidence
        )
        prompt = (
            "You are a strict retrieval-sufficiency judge. Return JSON with one boolean field named sufficient. "
            "Set it to true only if the supplied passages fully support an answer to every part of the question. "
            "Do not use outside knowledge."
        )
        body = self._chat_json(
            model=self.settings.sufficiency_judge_model,
            temperature=self.settings.sufficiency_judge_temperature,
            top_p=self.settings.sufficiency_judge_top_p,
            max_tokens=120,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Question:\n{query}\n\nPassages:\n{passages[:8000]}"},
            ],
            json_response=True,
        )
        value = body.get("sufficient")
        return value if isinstance(value, bool) else None

    def answer(self, *, query: str, evidence: list[EvidenceItem]) -> str:
        passages = "\n\n".join(
            f"[{item.evidence_id}] Source: {item.source}; section: {item.heading_path}\n{item.content}"
            for item in evidence
        )
        system = (
            "Answer only from the supplied documentary evidence. Cite every factual claim with one or more evidence "
            "identifiers exactly as [<evidence-id>]. If the passages do not support a complete answer, state the gap "
            "explicitly. Never invent thresholds, measurements, publications, or recommendations. Respond in the same "
            "language as the question and keep the answer technically precise."
        )
        body = self._chat_json(
            model=self.settings.answer_model,
            temperature=self.settings.answer_temperature,
            top_p=self.settings.answer_top_p,
            max_tokens=self.settings.answer_max_tokens,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": f"Question:\n{query}\n\nEvidence:\n{passages}"},
            ],
            json_response=False,
        )
        answer = body.get("content")
        if not isinstance(answer, str) or not answer.strip():
            raise ProviderError("answer model returned empty content")
        return answer.strip()

    def _chat_json(
        self,
        *,
        model: str,
        temperature: float,
        top_p: float,
        max_tokens: int,
        messages: list[dict[str, str]],
        json_response: bool,
    ) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": max_tokens,
        }
        if json_response:
            payload["response_format"] = {"type": "json_object"}
        response = self._request_json("chat/completions", payload)
        try:
            content = response["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise ProviderError("chat response is missing message content") from exc
        if not isinstance(content, str):
            raise ProviderError("chat response content is not text")
        if not json_response:
            return {"content": content}
        return parse_json_object(content)

    def _request_json(self, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        last_error: Exception | None = None
        for attempt in range(self.settings.openrouter_retry_attempts):
            try:
                response = self._client.post(path, json=payload)
                if response.status_code == 429 or response.status_code >= 500:
                    raise httpx.HTTPStatusError(
                        f"retryable provider status {response.status_code}",
                        request=response.request,
                        response=response,
                    )
                response.raise_for_status()
                body = response.json()
                if not isinstance(body, dict):
                    raise ProviderError("provider response body is not an object")
                return body
            except (httpx.HTTPError, ValueError, ProviderError) as exc:
                last_error = exc
                if attempt + 1 >= self.settings.openrouter_retry_attempts:
                    break
                time.sleep(min(4.0, 0.5 * (2**attempt)))
        logger.warning("OpenRouter request failed", extra={"path": path, "error_type": type(last_error).__name__})
        raise ProviderError(f"OpenRouter request failed: {type(last_error).__name__}") from last_error


def parse_json_object(content: str) -> dict[str, Any]:
    normalized = content.strip()
    if normalized.startswith("```"):
        normalized = normalized.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    try:
        parsed = json.loads(normalized)
    except json.JSONDecodeError as exc:
        raise ProviderError("model response is not valid JSON") from exc
    if not isinstance(parsed, dict):
        raise ProviderError("model JSON response is not an object")
    return parsed


def sanitize_planned_filters(
    filters: MetadataFilters,
    vocabulary: dict[str, list[str]],
) -> MetadataFilters:
    return MetadataFilters(
        **{
            field: value if value in vocabulary.get(field, []) else None
            for field in type(filters).model_fields
            if (value := getattr(filters, field)) is not None
        }
    )
