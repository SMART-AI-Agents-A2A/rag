from pathlib import Path

from rag.models import MetadataFilters, QueryRequest
from rag.service import RagService


def test_ingestion_is_idempotent_and_does_not_repeat_embeddings(service: RagService, monkeypatch) -> None:
    first = service.ingest()
    assert first.documents_indexed == 2
    assert first.chunks_indexed == 2
    count = service.store.client.count(service.settings.collection_name, exact=True).count

    def unexpected_embeddings(_: list[str]) -> list[list[float]]:
        raise AssertionError("unchanged corpus must not be embedded again")

    monkeypatch.setattr(service.provider, "embed", unexpected_embeddings)
    second = service.ingest()
    assert second.documents_unchanged == 2
    assert second.chunks_indexed == 0
    assert service.store.client.count(service.settings.collection_name, exact=True).count == count


def test_document_update_and_removal_are_synchronized(service: RagService, sample_corpus: Path) -> None:
    service.ingest()
    document = sample_corpus / "en" / "irrigation.md"
    previous = service.store.point_ids_for_document("en/irrigation.md")
    document.write_text(
        document.read_text(encoding="utf-8") + "\nUpdated water management passage.\n", encoding="utf-8"
    )
    (sample_corpus / "pt-BR" / "fenologia.md").unlink()
    result = service.ingest()
    current = service.store.point_ids_for_document("en/irrigation.md")
    assert result.documents_indexed == 1
    assert result.documents_removed == 1
    assert current and not current.intersection(previous)
    assert service.store.point_ids_for_document("pt-BR/fenologia.md") == set()
    response = service.query(QueryRequest(query="water management", filters=MetadataFilters(language="en")))
    assert len(response.evidence) == 1
    assert "Updated water management passage" in response.evidence[0].content


def test_full_reset_rebuilds_collection(service: RagService) -> None:
    first = service.ingest()
    rebuilt = service.ingest(reset=True)
    assert rebuilt.reset
    assert rebuilt.documents_indexed == first.documents_total
    assert rebuilt.chunks_indexed == first.chunks_indexed
    assert service.store.client.count(service.settings.collection_name, exact=True).count == first.chunks_indexed
