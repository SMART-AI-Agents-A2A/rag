import json
from pathlib import Path

from smart_rag.corpus import load_corpus, split_document

ROOT = Path(__file__).resolve().parents[1]


def test_bundled_corpus_is_complete_and_approved() -> None:
    documents = load_corpus(
        ROOT / "documents" / "rag",
        default_language="pt-BR",
        allowed_languages=("pt-BR", "en", "es"),
    )

    assert len(documents) == 11
    assert {document.metadata.language for document in documents} == {"pt-BR", "en", "es"}
    assert all(document.metadata.review_status == "approved" for document in documents)
    assert len({document.path for document in documents}) == len(documents)


def test_chunk_ids_are_deterministic() -> None:
    document = load_corpus(
        ROOT / "documents" / "rag",
        default_language="pt-BR",
        allowed_languages=("pt-BR", "en", "es"),
    )[0]

    first = split_document(document, chunk_size=1000, chunk_overlap=150)
    second = split_document(document, chunk_size=1000, chunk_overlap=150)

    assert first
    assert [chunk.id for chunk in first] == [chunk.id for chunk in second]
    assert all(chunk.heading_path for chunk in first)
    assert all(chunk.document_hash == document.document_hash for chunk in first)


def test_provenance_manifest_resolves_every_original_pdf() -> None:
    sources_root = ROOT / "documents" / "sources"
    manifest = json.loads((sources_root / "technical-coffee-sources.json").read_text(encoding="utf-8"))
    entries = manifest["documents"]

    assert len(entries) == 11
    assert all((sources_root / "raw" / entry["pdf"]).is_file() for entry in entries)
