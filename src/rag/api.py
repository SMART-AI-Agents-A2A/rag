import hmac
import logging
from contextlib import asynccontextmanager
from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, Response, status

from rag import __version__
from rag.corpus import CorpusError
from rag.models import (
    DocumentSummary,
    HealthResponse,
    IngestRequest,
    IngestResponse,
    QueryRequest,
    QueryResponse,
)
from rag.providers import ProviderError
from rag.service import RagService
from rag.settings import Settings, get_settings
from rag.store import StoreError

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def get_service() -> RagService:
    return RagService(get_settings())


@asynccontextmanager
async def lifespan(_: FastAPI):
    yield
    if get_service.cache_info().currsize:
        get_service().close()
        get_service.cache_clear()


app = FastAPI(
    title="RAG",
    description="Documentary retrieval and evidence-grounded generation service.",
    version=__version__,
    lifespan=lifespan,
)

SettingsDependency = Annotated[Settings, Depends(get_settings)]
ServiceDependency = Annotated[RagService, Depends(get_service)]


def require_admin(
    settings: SettingsDependency,
    authorization: Annotated[str | None, Header()] = None,
) -> None:
    expected = settings.normalized_admin_token
    if expected is None:
        return
    scheme, _, credential = (authorization or "").partition(" ")
    if scheme.lower() != "bearer" or not hmac.compare_digest(credential, expected):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="A valid administrative bearer token is required.",
            headers={"WWW-Authenticate": "Bearer"},
        )


@app.get("/health", response_model=HealthResponse, tags=["operations"])
def health(response: Response, service: ServiceDependency) -> HealthResponse:
    try:
        qdrant_ok = service.store.health()
        collection_exists = service.store.collection_exists() if qdrant_ok else False
    except Exception:
        qdrant_ok = False
        collection_exists = False
    try:
        documents = service.load_documents()
        corpus_available = True
    except Exception:
        documents = []
        corpus_available = False
    healthy = qdrant_ok and corpus_available
    if not healthy:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return HealthResponse(
        status="ok" if healthy else "degraded",
        qdrant="ok" if qdrant_ok else "unavailable",
        collection=service.settings.collection_name,
        collection_exists=collection_exists,
        corpus_available=corpus_available,
        corpus_documents=len(documents),
    )


@app.get("/v1/config", tags=["operations"])
def configuration(settings: SettingsDependency) -> dict[str, object]:
    return settings.public_configuration()


@app.get("/v1/documents", response_model=list[DocumentSummary], tags=["corpus"])
def documents(service: ServiceDependency) -> list[DocumentSummary]:
    try:
        return service.list_documents()
    except CorpusError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post(
    "/v1/ingest",
    response_model=IngestResponse,
    dependencies=[Depends(require_admin)],
    tags=["index"],
)
def ingest(payload: IngestRequest, service: ServiceDependency) -> IngestResponse:
    try:
        return service.ingest(reset=payload.reset)
    except (CorpusError, ProviderError, StoreError) as exc:
        logger.exception("ingestion failed")
        raise HTTPException(status_code=503, detail=f"Ingestion failed: {type(exc).__name__}") from exc


@app.post("/v1/query", response_model=QueryResponse, tags=["retrieval"])
def query(payload: QueryRequest, service: ServiceDependency) -> QueryResponse:
    return service.query(payload)
