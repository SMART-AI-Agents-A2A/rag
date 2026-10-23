from functools import lru_cache
from pathlib import Path
from typing import Any

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="RAG_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    host: str = "127.0.0.1"
    port: int = Field(default=8080, ge=1, le=65535)
    log_level: str = "INFO"
    admin_token: str | None = None

    qdrant_url: str = "http://127.0.0.1:6333"
    qdrant_api_key: str | None = None
    qdrant_timeout_seconds: float = Field(default=20.0, ge=1.0)
    collection_name: str = "coffee_documents"

    documents_dir: Path = Path("documents/rag")
    default_language: str = "pt-BR"
    allowed_languages: str = "pt-BR,en,es"

    openrouter_api_key: str | None = None
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    openrouter_timeout_seconds: float = Field(default=45.0, ge=1.0)
    openrouter_retry_attempts: int = Field(default=3, ge=1, le=8)
    embedding_model: str = "baai/bge-m3"
    embedding_dimension: int | None = Field(default=None, ge=1)

    top_k: int = Field(default=3, ge=1, le=20)
    max_top_k: int = Field(default=8, ge=1, le=20)
    rerank_enabled: bool = True
    rerank_model: str = "cohere/rerank-v3.5"
    rerank_candidates: int = Field(default=20, ge=1, le=100)
    vector_score_threshold: float = Field(default=0.30, ge=0.0, le=1.0)
    rerank_score_threshold: float = Field(default=0.30, ge=0.0, le=1.0)
    global_evidence_limit: int = Field(default=6, ge=1, le=20)
    max_chunks_per_document: int = Field(default=2, ge=1, le=20)
    max_subqueries: int = Field(default=4, ge=1, le=8)

    query_planning_enabled: bool = True
    query_model: str = "meta-llama/llama-3.1-8b-instruct"
    query_temperature: float = Field(default=0.1, ge=0.0, le=2.0)
    query_top_p: float = Field(default=1.0, gt=0.0, le=1.0)

    answer_enabled: bool = True
    answer_model: str = "deepseek/deepseek-v4-flash"
    answer_temperature: float = Field(default=0.4, ge=0.0, le=2.0)
    answer_top_p: float = Field(default=1.0, gt=0.0, le=1.0)
    answer_max_tokens: int = Field(default=900, ge=64, le=8192)

    sufficiency_judge_enabled: bool = False
    sufficiency_judge_model: str = "openai/gpt-4o-mini"
    sufficiency_judge_temperature: float = Field(default=0.1, ge=0.0, le=2.0)
    sufficiency_judge_top_p: float = Field(default=1.0, gt=0.0, le=1.0)

    chunk_size: int = Field(default=1000, ge=200)
    chunk_overlap: int = Field(default=150, ge=0)
    embedding_batch_size: int = Field(default=32, ge=1, le=256)

    @model_validator(mode="after")
    def validate_related_values(self) -> "Settings":
        if self.chunk_overlap >= self.chunk_size:
            raise ValueError("RAG_CHUNK_OVERLAP must be smaller than RAG_CHUNK_SIZE")
        if self.top_k > self.max_top_k:
            raise ValueError("RAG_TOP_K must not exceed RAG_MAX_TOP_K")
        if self.global_evidence_limit > self.max_top_k:
            raise ValueError("RAG_GLOBAL_EVIDENCE_LIMIT must not exceed RAG_MAX_TOP_K")
        return self

    @property
    def languages(self) -> tuple[str, ...]:
        return tuple(value.strip() for value in self.allowed_languages.split(",") if value.strip())

    @property
    def normalized_admin_token(self) -> str | None:
        value = (self.admin_token or "").strip()
        return value or None

    def public_configuration(self) -> dict[str, Any]:
        return {
            "collection_name": self.collection_name,
            "documents_dir": str(self.documents_dir),
            "allowed_languages": list(self.languages),
            "embedding_model": self.embedding_model,
            "embedding_dimension": self.embedding_dimension,
            "rerank_enabled": self.rerank_enabled,
            "rerank_model": self.rerank_model if self.rerank_enabled else None,
            "query_planning_enabled": self.query_planning_enabled,
            "query_model": self.query_model if self.query_planning_enabled else None,
            "query_temperature": self.query_temperature if self.query_planning_enabled else None,
            "query_top_p": self.query_top_p if self.query_planning_enabled else None,
            "answer_enabled": self.answer_enabled,
            "answer_model": self.answer_model if self.answer_enabled else None,
            "answer_temperature": self.answer_temperature if self.answer_enabled else None,
            "answer_top_p": self.answer_top_p if self.answer_enabled else None,
            "sufficiency_judge_enabled": self.sufficiency_judge_enabled,
            "sufficiency_judge_model": (self.sufficiency_judge_model if self.sufficiency_judge_enabled else None),
            "sufficiency_judge_temperature": (
                self.sufficiency_judge_temperature if self.sufficiency_judge_enabled else None
            ),
            "sufficiency_judge_top_p": self.sufficiency_judge_top_p if self.sufficiency_judge_enabled else None,
            "top_k": self.top_k,
            "max_top_k": self.max_top_k,
            "global_evidence_limit": self.global_evidence_limit,
            "max_chunks_per_document": self.max_chunks_per_document,
            "vector_score_threshold": self.vector_score_threshold,
            "rerank_score_threshold": self.rerank_score_threshold,
            "chunk_size": self.chunk_size,
            "chunk_overlap": self.chunk_overlap,
        }


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
