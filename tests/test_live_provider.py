from pathlib import Path

import pytest

from rag.models import QueryRequest
from rag.providers import OpenRouterClient
from rag.service import RagService
from rag.settings import Settings
from rag.store import QdrantStore

ROOT = Path(__file__).resolve().parents[1]
pytestmark = pytest.mark.live


def test_configured_provider_retrieves_and_generates(sample_corpus: Path, store: QdrantStore) -> None:
    settings = Settings(
        _env_file=ROOT / ".env",
        documents_dir=sample_corpus,
        collection_name=store.collection_name,
        vector_score_threshold=0.0,
        rerank_score_threshold=0.0,
    )
    if not settings.openrouter_api_key or settings.openrouter_api_key.startswith("replace-with-"):
        pytest.fail("--live-provider requires RAG_OPENROUTER_API_KEY in the environment or .env")
    with OpenRouterClient(settings) as provider:
        service = RagService(settings, store=store, provider=provider)
        assert service.ingest().documents_indexed == 2
        result = service.query(QueryRequest(query="How does drip irrigation deliver water?", generate_answer=True))
        assert result.evidence
        assert result.answer
        assert result.metadata["answer_error_type"] is None
        if settings.query_planning_enabled:
            assert result.plan.planning_degraded is False
        if settings.rerank_enabled:
            assert result.metadata["rerank_degraded"] is False
            assert result.metadata["score_kind"] == "rerank"
        if settings.sufficiency_judge_enabled:
            assert "retrieval_sufficiency_not_validated" not in result.assessment.limitations
