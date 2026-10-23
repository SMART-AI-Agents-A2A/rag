import json

import httpx

from rag.models import MetadataFilters
from rag.providers import OpenRouterClient, parse_json_object, sanitize_planned_filters
from rag.settings import Settings


def test_embedding_response_is_restored_by_index() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path.endswith("/embeddings")
        return httpx.Response(
            200,
            json={
                "data": [
                    {"index": 1, "embedding": [0.0, 1.0]},
                    {"index": 0, "embedding": [1.0, 0.0]},
                ]
            },
        )

    client = OpenRouterClient(
        Settings(openrouter_api_key="test"),
        transport=httpx.MockTransport(handler),
    )
    try:
        assert client.embed(["a", "b"]) == [[1.0, 0.0], [0.0, 1.0]]
    finally:
        client.close()


def test_fenced_json_is_accepted() -> None:
    payload = {"breadth": "focused", "subqueries": ["coffee irrigation"], "filters": {}}
    assert parse_json_object(f"```json\n{json.dumps(payload)}\n```") == payload


def test_planned_filters_are_restricted_to_corpus_vocabulary() -> None:
    filters = sanitize_planned_filters(
        MetadataFilters(language="Portuguese", crop="coffee", region="unknown"),
        {
            "language": ["pt-BR", "en", "es"],
            "crop": ["coffee"],
            "region": ["brasil"],
        },
    )
    assert filters.language is None
    assert filters.crop == "coffee"
    assert filters.region is None
