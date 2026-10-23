import hashlib
import json
import os
import re
import warnings
from collections.abc import Iterator
from pathlib import Path
from uuid import uuid4

import httpx
import pytest
from dotenv import dotenv_values
from qdrant_client import QdrantClient

from rag.api import app, get_service
from rag.providers import OpenRouterClient
from rag.service import RagService
from rag.settings import Settings, get_settings
from rag.store import QdrantStore

ROOT = Path(__file__).resolve().parents[1]
SERVER_API_KEY = os.environ.get("RAG_QDRANT_API_KEY") or dotenv_values(ROOT / ".env").get("RAG_QDRANT_API_KEY") or None


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--qdrant-url", help="Run Qdrant server tests against this HTTP URL")
    parser.addoption("--live-provider", action="store_true", help="Run authenticated OpenRouter requests")


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    for item in items:
        if "qdrant" in item.keywords and not config.getoption("--qdrant-url"):
            item.add_marker(pytest.mark.skip(reason="requires --qdrant-url"))
        if "live" in item.keywords and not config.getoption("--live-provider"):
            item.add_marker(pytest.mark.skip(reason="requires --live-provider"))


@pytest.fixture(autouse=True)
def isolated_configuration(monkeypatch: pytest.MonkeyPatch, tmp_path: Path, request: pytest.FixtureRequest):
    if "live" not in request.keywords:
        for key in list(os.environ):
            if key.startswith("RAG_"):
                monkeypatch.delenv(key)
    monkeypatch.chdir(tmp_path)
    get_settings.cache_clear()
    get_service.cache_clear()
    app.dependency_overrides.clear()
    yield
    app.dependency_overrides.clear()
    get_settings.cache_clear()
    get_service.cache_clear()


@pytest.fixture
def sample_corpus(tmp_path: Path) -> Path:
    root = tmp_path / "corpus"
    for language, stem, text in (
        ("en", "irrigation", "Drip irrigation delivers water to the root zone."),
        ("pt-BR", "fenologia", "A disponibilidade hídrica influencia o desenvolvimento da cultura."),
    ):
        directory = root / language
        directory.mkdir(parents=True)
        (directory / f"{stem}.md").write_text(
            "---\n"
            f"title: {stem}\nsource: {stem}.pdf\nyear: 2024\nlanguage: {language}\n"
            "crop: agriculture\nregion: global\ntopic: irrigation\n"
            "document_type: technical_manual\nreview_status: approved\n"
            f"---\n\n# {stem}\n\n## Water management\n\n{text}\n",
            encoding="utf-8",
        )
    return root


@pytest.fixture
def settings(sample_corpus: Path) -> Settings:
    return Settings(
        _env_file=None,
        documents_dir=sample_corpus,
        openrouter_api_key="test-credential",
        embedding_dimension=8,
        collection_name=f"pytest_{uuid4().hex}",
        vector_score_threshold=0.0,
        query_planning_enabled=False,
        rerank_enabled=False,
        answer_enabled=False,
    )


@pytest.fixture
def provider(settings: Settings) -> Iterator[OpenRouterClient]:
    def handler(request: httpx.Request) -> httpx.Response:
        payload = json.loads(request.content)
        if request.url.path.endswith("/embeddings"):
            data = []
            for index, text in enumerate(payload["input"]):
                digest = hashlib.sha256(text.encode()).digest()
                vector = [(value + 1) / 256 for value in digest[:8]]
                data.append({"index": index, "embedding": vector})
            return httpx.Response(200, json={"data": data})
        if request.url.path.endswith("/rerank"):
            results = [{"index": index, "relevance_score": 0.9} for index in range(len(payload["documents"]))]
            return httpx.Response(200, json={"results": results})
        prompt = payload["messages"][0]["content"]
        if "Plan retrieval" in prompt:
            content = json.dumps({"breadth": "focused", "subqueries": ["water management"], "filters": {}})
        elif "sufficiency judge" in prompt:
            content = json.dumps({"sufficient": True})
        else:
            evidence_id = re.search(r"\[(rag:[^\]]+)\]", payload["messages"][1]["content"])
            assert evidence_id is not None
            content = f"Water management is documented [{evidence_id.group(1)}]."
        return httpx.Response(200, json={"choices": [{"message": {"content": content}}]})

    with OpenRouterClient(settings, transport=httpx.MockTransport(handler)) as client:
        yield client


@pytest.fixture
def store(settings: Settings) -> Iterator[QdrantStore]:
    client = QdrantClient(":memory:", force_disable_check_same_thread=True)
    instance = QdrantStore(settings, client=client)
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message="Payload indexes have no effect in the local Qdrant.*")
        yield instance
    instance.close()


@pytest.fixture
def service(settings: Settings, store: QdrantStore, provider: OpenRouterClient) -> RagService:
    return RagService(settings, store=store, provider=provider)


@pytest.fixture
def server_store(settings: Settings, request: pytest.FixtureRequest) -> Iterator[QdrantStore]:
    url = request.config.getoption("--qdrant-url")
    client = QdrantClient(url=url, api_key=SERVER_API_KEY, timeout=10)
    instance = QdrantStore(settings, client=client)
    ready = False
    try:
        assert instance.health()
        ready = True
        yield instance
    finally:
        if ready and instance.collection_exists():
            client.delete_collection(settings.collection_name)
        instance.close()
