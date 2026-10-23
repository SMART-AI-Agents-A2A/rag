from pathlib import Path

import pytest

from rag.models import MetadataFilters, QueryRequest
from rag.providers import OpenRouterClient
from rag.service import RagService
from rag.settings import Settings
from rag.store import QdrantStore, StoreError

pytestmark = pytest.mark.qdrant
ROOT = Path(__file__).resolve().parents[1]


def test_server_ingestion_search_and_idempotence(
    settings: Settings, server_store: QdrantStore, provider: OpenRouterClient
) -> None:
    service = RagService(settings, store=server_store, provider=provider)
    first = service.ingest()
    assert first.documents_indexed == 2
    assert first.vector_size == 8
    second = service.ingest()
    assert second.documents_unchanged == 2
    assert second.chunks_indexed == 0
    result = service.query(QueryRequest(query="water management", filters=MetadataFilters(language="en")))
    assert result.evidence
    assert all(item.language == "en" for item in result.evidence)
    assert server_store.client.count(settings.collection_name, exact=True).count == first.chunks_indexed


def test_server_rejects_incompatible_vector_dimensions(server_store: QdrantStore) -> None:
    server_store.ensure_collection(8)
    with pytest.raises(StoreError, match="vector size"):
        server_store.ensure_collection(16)


def test_server_indexes_the_bundled_corpus(
    settings: Settings, server_store: QdrantStore, provider: OpenRouterClient
) -> None:
    settings.documents_dir = ROOT / "documents" / "rag"
    service = RagService(settings, store=server_store, provider=provider)
    indexed = service.ingest()
    assert indexed.documents_total == 11
    assert indexed.documents_indexed == 11
    assert indexed.chunks_indexed > 1000
    assert server_store.client.count(settings.collection_name, exact=True).count == indexed.chunks_indexed
    unchanged = service.ingest()
    assert unchanged.documents_unchanged == 11
    assert unchanged.chunks_indexed == 0
    result = service.query(QueryRequest(query="irrigação", filters=MetadataFilters(language="pt-BR")))
    assert result.evidence
    assert all(item.language == "pt-BR" for item in result.evidence)
