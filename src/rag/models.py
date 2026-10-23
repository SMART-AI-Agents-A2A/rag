from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class DataQualityStatus(StrEnum):
    OK = "ok"
    PARTIAL = "partial"
    COLLECTION_GAP = "collection_gap"
    NOT_AVAILABLE = "not_available"
    SOURCE_ERROR = "source_error"


class Answerability(StrEnum):
    COMPLETE = "complete"
    PARTIAL = "partial"
    NOT_ANSWERABLE = "not_answerable"


class QueryBreadth(StrEnum):
    FOCUSED = "focused"
    BROAD = "broad"


class MetadataFilters(StrictModel):
    language: str | None = None
    crop: str | None = None
    region: str | None = None
    topic: str | None = None
    document_type: str | None = None

    def merged_with(self, override: "MetadataFilters | None") -> "MetadataFilters":
        if override is None:
            return self
        return MetadataFilters(
            **{field: getattr(override, field) or getattr(self, field) for field in type(self).model_fields}
        )


class QueryPlan(StrictModel):
    original_query: str
    breadth: QueryBreadth = QueryBreadth.FOCUSED
    subqueries: list[str] = Field(min_length=1, max_length=8)
    filters: MetadataFilters = Field(default_factory=MetadataFilters)
    planning_degraded: bool = False

    @field_validator("subqueries")
    @classmethod
    def normalize_subqueries(cls, value: list[str]) -> list[str]:
        normalized = list(dict.fromkeys(" ".join(item.split()) for item in value if item.strip()))
        if not normalized:
            raise ValueError("at least one non-empty subquery is required")
        return normalized

    @model_validator(mode="after")
    def normalize_breadth(self) -> "QueryPlan":
        if len(self.subqueries) < 2 and self.breadth is QueryBreadth.BROAD:
            self.breadth = QueryBreadth.FOCUSED
        return self


class DocumentMetadata(StrictModel):
    title: str
    source: str
    year: int
    crop: str
    region: str
    topic: str
    document_type: str
    language: str
    review_status: str
    reference: str | None = None
    scope: str | None = None


class CorpusDocument(StrictModel):
    path: str
    document_hash: str
    metadata: DocumentMetadata
    content: str


class Chunk(StrictModel):
    id: str
    document_path: str
    document_hash: str
    chunk_index: int
    heading_path: str
    content_hash: str
    content: str
    metadata: DocumentMetadata


class EvidenceItem(StrictModel):
    evidence_id: str
    source: str
    title: str
    content: str
    score: float
    score_kind: str
    rank: int
    document_path: str
    heading_path: str
    language: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class RetrievalAssessment(StrictModel):
    answerability: Answerability
    limitations: list[str] = Field(default_factory=list)
    covered_subqueries: list[str] = Field(default_factory=list)
    missing_subqueries: list[str] = Field(default_factory=list)


class QueryRequest(StrictModel):
    query: str = Field(min_length=2, max_length=4000)
    top_k: int | None = Field(default=None, ge=1, le=20)
    filters: MetadataFilters | None = None
    generate_answer: bool | None = None

    @field_validator("query")
    @classmethod
    def normalize_query(cls, value: str) -> str:
        normalized = " ".join(value.split())
        if len(normalized) < 2:
            raise ValueError("query must contain at least two non-whitespace characters")
        return normalized


class QueryResponse(StrictModel):
    query: str
    status: DataQualityStatus
    answer: str | None
    evidence: list[EvidenceItem]
    plan: QueryPlan
    assessment: RetrievalAssessment
    metadata: dict[str, Any] = Field(default_factory=dict)


class IngestRequest(StrictModel):
    reset: bool = False


class IngestResponse(StrictModel):
    collection: str
    documents_total: int
    documents_indexed: int
    documents_unchanged: int
    documents_removed: int
    chunks_indexed: int
    reset: bool
    embedding_model: str
    vector_size: int


class DocumentSummary(StrictModel):
    path: str
    title: str
    source: str
    year: int
    language: str
    crop: str
    region: str
    topic: str
    document_type: str
    document_hash: str


class HealthResponse(StrictModel):
    status: str
    service: str = "rag"
    qdrant: str
    collection: str
    collection_exists: bool
    corpus_available: bool
    corpus_documents: int
