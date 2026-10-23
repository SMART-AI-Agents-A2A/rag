from dataclasses import dataclass
from typing import Any

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    FieldCondition,
    Filter,
    FilterSelector,
    MatchValue,
    PayloadSchemaType,
    PointIdsList,
    PointStruct,
    VectorParams,
)

from smart_rag.models import Chunk, MetadataFilters
from smart_rag.settings import Settings


class StoreError(RuntimeError):
    """Raised when vector-store state is incompatible with the configured RAG."""


@dataclass(frozen=True)
class SearchCandidate:
    id: str
    score: float
    content: str
    metadata: dict[str, Any]


class QdrantStore:
    def __init__(self, settings: Settings, *, client: QdrantClient | None = None) -> None:
        self.settings = settings
        self.collection_name = settings.collection_name
        self.client = client or QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key,
            timeout=int(settings.qdrant_timeout_seconds),
        )

    def close(self) -> None:
        close = getattr(self.client, "close", None)
        if callable(close):
            close()

    def collection_exists(self) -> bool:
        return bool(self.client.collection_exists(self.collection_name))

    def health(self) -> bool:
        self.client.get_collections()
        return True

    def ensure_collection(self, vector_size: int, *, reset: bool = False) -> None:
        exists = self.collection_exists()
        if reset and exists:
            self.client.delete_collection(self.collection_name)
            exists = False
        if exists:
            actual = self.vector_size()
            if actual is not None and actual != vector_size:
                raise StoreError(
                    f"collection vector size is {actual}, but the embedding provider returned {vector_size}; "
                    "run ingestion with --reset"
                )
            return
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )
        for field in (
            "metadata.document_path",
            "metadata.document_hash",
            "metadata.language",
            "metadata.crop",
            "metadata.region",
            "metadata.topic",
            "metadata.document_type",
        ):
            self.client.create_payload_index(
                collection_name=self.collection_name,
                field_name=field,
                field_schema=PayloadSchemaType.KEYWORD,
                wait=True,
            )

    def vector_size(self) -> int | None:
        if not self.collection_exists():
            return None
        info = self.client.get_collection(self.collection_name)
        vectors = info.config.params.vectors
        size = getattr(vectors, "size", None)
        if isinstance(size, int):
            return size
        if isinstance(vectors, dict) and vectors:
            first = next(iter(vectors.values()))
            named_size = getattr(first, "size", None)
            return named_size if isinstance(named_size, int) else None
        return None

    def indexed_document_hashes(self) -> dict[str, str]:
        if not self.collection_exists():
            return {}
        hashes: dict[str, str] = {}
        offset: Any = None
        while True:
            points, offset = self.client.scroll(
                collection_name=self.collection_name,
                limit=256,
                offset=offset,
                with_payload=True,
                with_vectors=False,
            )
            for point in points:
                metadata = nested_metadata(point.payload)
                path = metadata.get("document_path")
                document_hash = metadata.get("document_hash")
                if isinstance(path, str) and isinstance(document_hash, str):
                    hashes[path] = document_hash
            if offset is None:
                break
        return hashes

    def point_ids_for_document(self, document_path: str) -> set[str]:
        if not self.collection_exists():
            return set()
        point_filter = document_filter(document_path)
        ids: set[str] = set()
        offset: Any = None
        while True:
            points, offset = self.client.scroll(
                collection_name=self.collection_name,
                scroll_filter=point_filter,
                limit=256,
                offset=offset,
                with_payload=False,
                with_vectors=False,
            )
            ids.update(str(point.id) for point in points)
            if offset is None:
                break
        return ids

    def upsert(self, chunks: list[Chunk], vectors: list[list[float]], *, batch_size: int = 128) -> None:
        if len(chunks) != len(vectors):
            raise ValueError("chunk and vector counts differ")
        points = [
            PointStruct(
                id=chunk.id,
                vector=vector,
                payload={
                    "content": chunk.content,
                    "metadata": {
                        **chunk.metadata.model_dump(mode="json"),
                        "document_path": chunk.document_path,
                        "document_hash": chunk.document_hash,
                        "chunk_index": chunk.chunk_index,
                        "heading_path": chunk.heading_path,
                        "content_hash": chunk.content_hash,
                    },
                },
            )
            for chunk, vector in zip(chunks, vectors, strict=True)
        ]
        for start in range(0, len(points), batch_size):
            self.client.upsert(
                collection_name=self.collection_name,
                points=points[start : start + batch_size],
                wait=True,
            )

    def delete_point_ids(self, point_ids: set[str]) -> None:
        if not point_ids:
            return
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=PointIdsList(points=sorted(point_ids)),
            wait=True,
        )

    def delete_document(self, document_path: str) -> None:
        if not self.collection_exists():
            return
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=FilterSelector(filter=document_filter(document_path)),
            wait=True,
        )

    def search(
        self,
        *,
        vector: list[float],
        limit: int,
        filters: MetadataFilters,
    ) -> list[SearchCandidate]:
        if not self.collection_exists():
            return []
        response = self.client.query_points(
            collection_name=self.collection_name,
            query=vector,
            query_filter=metadata_filter(filters),
            limit=limit,
            with_payload=True,
            with_vectors=False,
        )
        candidates: list[SearchCandidate] = []
        for point in response.points:
            payload = point.payload or {}
            content = payload.get("content")
            metadata = nested_metadata(payload)
            if not isinstance(content, str) or not metadata:
                continue
            candidates.append(
                SearchCandidate(
                    id=str(point.id),
                    score=float(point.score),
                    content=content,
                    metadata=metadata,
                )
            )
        return candidates


def nested_metadata(payload: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return {}
    metadata = payload.get("metadata")
    return metadata if isinstance(metadata, dict) else {}


def document_filter(document_path: str) -> Filter:
    return Filter(must=[FieldCondition(key="metadata.document_path", match=MatchValue(value=document_path))])


def metadata_filter(filters: MetadataFilters) -> Filter | None:
    conditions = [
        FieldCondition(key=f"metadata.{field}", match=MatchValue(value=value))
        for field in type(filters).model_fields
        if (value := getattr(filters, field)) is not None
    ]
    return Filter(must=conditions) if conditions else None
