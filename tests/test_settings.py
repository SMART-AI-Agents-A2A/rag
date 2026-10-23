from pathlib import Path

import pytest
from pydantic import ValidationError

from rag.settings import Settings

ROOT = Path(__file__).resolve().parents[1]


def test_example_environment_loads_and_covers_all_service_parameters() -> None:
    path = ROOT / "env.example"
    settings = Settings(_env_file=path)
    keys = {line.split("=", 1)[0] for line in path.read_text().splitlines() if line and not line.startswith("#")}
    assert {f"RAG_{field.upper()}" for field in Settings.model_fields} <= keys
    assert {"RAG_API_PORT", "RAG_QDRANT_PORT"} <= keys
    assert settings.embedding_dimension == 1024
    assert settings.answer_temperature == 0.7
    assert settings.query_temperature == 0.5
    assert settings.sufficiency_judge_temperature == 0.5


@pytest.mark.parametrize("overrides", [{"chunk_overlap": 1000}, {"top_k": 9}, {"global_evidence_limit": 9}])
def test_invalid_related_parameters_are_rejected(overrides: dict) -> None:
    with pytest.raises(ValidationError):
        Settings(_env_file=None, **overrides)
