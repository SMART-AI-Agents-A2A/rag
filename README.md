# SMART RAG

[Português](README.BR.md)

Standalone, auditable retrieval-augmented generation service for the SMART - AROMA technical corpus. This repository was extracted from Smart Coffee Fog Swarm and redesigned to run without its Supervisor, agents, MCP server, internal packages, or monorepo workspace.

The approved Markdown corpus is the source of truth. Qdrant is a derived index that can be rebuilt at any time.

## Capabilities

- Multilingual corpus in Brazilian Portuguese, English, and Spanish.
- Deterministic Markdown chunk identifiers and incremental ingestion.
- Dense embeddings through OpenRouter using `baai/bge-m3` by default.
- Optional query planning and multi-query retrieval.
- Metadata filters for language, crop, region, topic, and document type.
- Optional reranking through `cohere/rerank-v3.5`.
- Separate vector and rerank score thresholds.
- Per-document diversity limits and global evidence limits.
- Grounded answer generation with mandatory evidence identifiers.
- Conservative, optional retrieval-sufficiency judge.
- HTTP API, command-line interface, Docker image, and Docker Compose stack.

## Repository layout

```text
documents/rag/                 canonical approved corpus
documents/sources/raw/         original PDF sources for audit
documents/sources/             corpus provenance manifest
evaluation/                    RAG relevance judgments
src/smart_rag/corpus.py        frontmatter validation and chunking
src/smart_rag/providers.py     OpenRouter embeddings, planning, rerank, and answer generation
src/smart_rag/store.py         Qdrant persistence and vector search
src/smart_rag/service.py       ingestion and retrieval orchestration
src/smart_rag/api.py           FastAPI application
src/smart_rag/cli.py           command-line interface
tests/                         deterministic unit and corpus tests
```

The repository includes 11 approved documents: seven in `pt-BR`, three in English, and one in Spanish. Their 11 original PDFs and the provenance mapping are preserved under `documents/sources/` for independent audit. Raw PDFs are excluded from the runtime Docker image because retrieval uses only the approved corpus.

## Architecture

```text
POST /v1/query or smart-rag query
              │
              ▼
     query plan (fail-open)
              │
              ▼
     multilingual embedding
              │
              ▼
        Qdrant vector search
              │
              ▼
      rerank (optional/fail-open)
              │
              ▼
 threshold + deduplication + source diversity
              │
              ▼
 structured evidence and coverage assessment
              │
              ▼
 grounded answer with validated evidence citations
```

Failure of planning, reranking, sufficiency judgment, or answer generation does not discard valid retrieval evidence. An embedding or Qdrant failure is returned as a structured source error.

## Quick start with Docker

1. Create the local environment file and set `RAG_OPENROUTER_API_KEY`:

   ```bash
   cp .env.example .env
   ```

2. Start Qdrant:

   ```bash
   docker compose up -d qdrant
   ```

3. Build the vector index:

   ```bash
   docker compose --profile maintenance run --rm rag-ingest
   ```

4. Start the API:

   ```bash
   docker compose up -d rag-api
   ```

5. Verify the service:

   ```bash
   curl http://127.0.0.1:8080/health
   ```

The API is bound to `127.0.0.1` by default. Qdrant data is persisted in the Docker volume `rag_qdrant-storage` and is not part of the Git repository.

## Query example

```bash
curl -s http://127.0.0.1:8080/v1/query \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "Quais fases fenológicas do cafeeiro exigem maior atenção à disponibilidade hídrica?",
    "top_k": 4
  }'
```

To retrieve evidence without generating prose:

```json
{
  "query": "What supports drip irrigation management?",
  "generate_answer": false,
  "filters": {
    "crop": "coffee",
    "language": "en"
  }
}
```

## HTTP API

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/health` | Qdrant, collection, and corpus status |
| `GET` | `/v1/config` | Effective non-secret configuration |
| `GET` | `/v1/documents` | Canonical corpus inventory |
| `POST` | `/v1/ingest` | Incremental or full index rebuild |
| `POST` | `/v1/query` | Retrieval, assessment, and optional answer generation |
| `GET` | `/docs` | Interactive OpenAPI documentation |

Set `RAG_ADMIN_TOKEN` outside local development to protect `/v1/ingest`. Send it as `Authorization: Bearer <token>`.

## Command-line interface

```bash
smart-rag documents
smart-rag config
smart-rag ingest
smart-rag ingest --reset
smart-rag query "What documents discuss coffee irrigation?"
smart-rag query --no-answer "What documents discuss coffee irrigation?"
smart-rag serve
```

For a local installation:

```bash
python3.12 -m venv .venv
.venv/bin/pip install -e '.[dev]'
```

When running outside Compose, set `RAG_QDRANT_URL=http://127.0.0.1:6333`.

## Default retrieval configuration

| Parameter | Default |
| --- | --- |
| Embedding provider | OpenRouter |
| Embedding model | `baai/bge-m3` |
| Rerank model | `cohere/rerank-v3.5` |
| Query-planning model | `meta-llama/llama-3.1-8b-instruct` |
| Query-planning temperature / top-p | `0.1` / `1.0` |
| Answer model | `deepseek/deepseek-v4-flash` |
| Answer temperature / top-p | `0.4` / `1.0` |
| Sufficiency-judge model | `openai/gpt-4o-mini` |
| Sufficiency-judge temperature / top-p | `0.1` / `1.0` |
| Focused `top_k` / maximum `top_k` | `3` / `8` |
| Rerank candidates | `20` |
| Vector / rerank score threshold | `0.30` / `0.30` |
| Global evidence limit | `6` |
| Maximum chunks per document | `2` |
| Chunk size / overlap | `1000` / `150` characters |

Query planning and reranking are enabled by default. The sufficiency judge is disabled by default, so retrieved answers remain marked `partial` with `retrieval_sufficiency_not_validated` unless the judge is explicitly enabled and confirms complete coverage.

## Ingestion guarantees

- Only files with `review_status: approved` are accepted.
- Original PDFs remain immutable audit sources and are never indexed directly.
- File language must match its corpus subdirectory.
- Chunk IDs are UUIDv5 values derived from document path, heading path, chunk index, and content hash.
- New vectors are upserted before obsolete vectors are removed.
- Unchanged documents are not embedded again.
- Removed corpus documents are removed from Qdrant during synchronization.
- Embedding-dimension changes require `smart-rag ingest --reset`.

## Research reproducibility

Record the Git revision, corpus hashes, Qdrant collection name, embedding model and dimension, chunking parameters, query-planning configuration, rerank configuration, thresholds, answer model, and execution date for every experiment. The relevance judgments migrated from the source project are available in `evaluation/smart-coffee-rag-qrels-v1.json`.

Remote provider model aliases may change implementation over time. For publication-grade experiments, preserve the provider response metadata and use pinned model identifiers whenever the provider supports them.
