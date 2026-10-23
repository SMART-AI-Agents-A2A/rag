from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from rag.api import app, get_service
from rag.service import RagService
from rag.settings import Settings, get_settings


@pytest.fixture
def client(service: RagService, settings: Settings) -> Iterator[TestClient]:
    app.dependency_overrides[get_service] = lambda: service
    app.dependency_overrides[get_settings] = lambda: settings
    with TestClient(app) as instance:
        yield instance


def test_health_and_openapi_are_available_before_ingestion(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "rag"
    assert response.json()["corpus_documents"] == 2
    assert response.json()["collection_exists"] is False
    schema = client.get("/openapi.json").json()
    assert schema["info"]["title"] == "RAG"
    assert {"/health", "/v1/query", "/v1/ingest", "/v1/documents", "/v1/config"} <= schema["paths"].keys()
    assert client.get("/docs").status_code == 200


def test_config_omits_credentials(client: TestClient, settings: Settings) -> None:
    settings.admin_token = "private-administrative-token"
    settings.qdrant_api_key = "private-qdrant-key"
    response = client.get("/v1/config")
    assert response.status_code == 200
    assert settings.openrouter_api_key not in response.text
    assert settings.admin_token not in response.text
    assert settings.qdrant_api_key not in response.text
    assert response.json()["answer_temperature"] is None


def test_index_and_query_through_http(client: TestClient) -> None:
    inventory = client.get("/v1/documents")
    assert inventory.status_code == 200
    assert len(inventory.json()) == 2
    missing = client.post("/v1/query", json={"query": "water management"})
    assert missing.json()["status"] == "not_available"
    first = client.post("/v1/ingest", json={})
    assert first.status_code == 200
    assert first.json()["documents_indexed"] == 2
    second = client.post("/v1/ingest", json={})
    assert second.json()["documents_unchanged"] == 2
    response = client.post(
        "/v1/query",
        json={"query": "water management", "generate_answer": True, "filters": {"language": "en"}},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["evidence"]
    assert all(item["language"] == "en" for item in body["evidence"])
    assert f"[{body['evidence'][0]['evidence_id']}]" in body["answer"]


def test_ingestion_requires_configured_admin_token(client: TestClient, settings: Settings) -> None:
    settings.admin_token = "secret-token"
    for headers in ({}, {"Authorization": "Bearer wrong"}, {"Authorization": "Basic secret-token"}):
        response = client.post("/v1/ingest", json={}, headers=headers)
        assert response.status_code == 401
        assert response.headers["WWW-Authenticate"] == "Bearer"
    response = client.post("/v1/ingest", json={}, headers={"Authorization": "Bearer secret-token"})
    assert response.status_code == 200


@pytest.mark.parametrize(
    "payload", [{"query": "  "}, {"query": "x"}, {"query": "water", "top_k": 0}, {"query": "water", "unknown": True}]
)
def test_query_rejects_invalid_requests(client: TestClient, payload: dict) -> None:
    assert client.post("/v1/query", json=payload).status_code == 422


def test_health_reports_503_when_qdrant_is_unavailable(
    client: TestClient, service: RagService, monkeypatch: pytest.MonkeyPatch
) -> None:
    def unavailable() -> bool:
        raise ConnectionError("Qdrant offline")

    monkeypatch.setattr(service.store, "health", unavailable)
    response = client.get("/health")
    assert response.status_code == 503
    assert response.json()["status"] == "degraded"
    assert response.json()["qdrant"] == "unavailable"


def test_query_returns_structured_source_error_when_qdrant_is_unavailable(
    client: TestClient, service: RagService, monkeypatch: pytest.MonkeyPatch
) -> None:
    def unavailable() -> bool:
        raise ConnectionError("Qdrant offline")

    monkeypatch.setattr(service.store, "collection_exists", unavailable)
    response = client.post("/v1/query", json={"query": "water management"})
    assert response.status_code == 200
    assert response.json()["status"] == "source_error"
    assert response.json()["evidence"] == []
