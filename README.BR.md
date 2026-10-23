# SMART RAG

[English](README.md)

Serviço autônomo e auditável de geração aumentada por recuperação para o corpus técnico SMART - AROMA. Este repositório foi extraído do Smart Coffee Fog Swarm e reformulado para operar sem o Supervisor, agentes, servidor MCP, pacotes internos ou workspace do monorepo.

O corpus Markdown aprovado é a fonte de verdade. O Qdrant contém apenas um índice derivado, que pode ser reconstruído a qualquer momento.

## Capacidades

- Corpus multilíngue em português do Brasil, inglês e espanhol.
- IDs determinísticos de chunks e ingestão incremental.
- Embeddings densos pelo OpenRouter, usando `baai/bge-m3` por padrão.
- Planejamento opcional da consulta e recuperação por múltiplas subconsultas.
- Filtros por idioma, cultura, região, tópico e tipo documental.
- Rerank opcional com `cohere/rerank-v3.5`.
- Limiares separados para busca vetorial e rerank.
- Diversidade por documento e limite global de evidências.
- Geração de resposta fundamentada com identificadores obrigatórios de evidência.
- Juiz de suficiência opcional e conservador.
- API HTTP, interface de linha de comando, imagem Docker e Docker Compose.

## Estrutura do repositório

```text
documents/rag/                 corpus canônico aprovado
documents/sources/raw/         PDFs originais para auditoria
documents/sources/             manifesto de procedência do corpus
evaluation/                    julgamentos de relevância do RAG
src/smart_rag/corpus.py        validação de frontmatter e chunking
src/smart_rag/providers.py     embeddings, planejamento, rerank e geração no OpenRouter
src/smart_rag/store.py         persistência e busca vetorial no Qdrant
src/smart_rag/service.py       orquestração da ingestão e recuperação
src/smart_rag/api.py           aplicação FastAPI
src/smart_rag/cli.py           interface de linha de comando
tests/                         testes determinísticos e do corpus
```

O repositório contém 11 documentos aprovados: sete em `pt-BR`, três em inglês e um em espanhol. Os 11 PDFs originais e seu mapeamento de procedência ficam preservados em `documents/sources/` para auditoria independente. Os PDFs são excluídos da imagem Docker de execução, pois a recuperação utiliza apenas o corpus aprovado.

## Arquitetura

```text
POST /v1/query ou smart-rag query
              │
              ▼
 planejamento da consulta (fail-open)
              │
              ▼
 embedding multilíngue
              │
              ▼
 busca vetorial no Qdrant
              │
              ▼
 rerank opcional (fail-open)
              │
              ▼
 limiar + deduplicação + diversidade de fontes
              │
              ▼
 evidências estruturadas e avaliação de cobertura
              │
              ▼
 resposta fundamentada com citações validadas
```

Falhas no planejamento, rerank, juiz de suficiência ou geração da resposta não descartam evidências válidas. Falhas de embedding ou Qdrant são retornadas como erros estruturados da fonte.

## Inicialização com Docker

1. Crie o arquivo de ambiente e configure `RAG_OPENROUTER_API_KEY`:

   ```bash
   cp .env.example .env
   ```

2. Inicie o Qdrant:

   ```bash
   docker compose up -d qdrant
   ```

3. Construa o índice vetorial:

   ```bash
   docker compose --profile maintenance run --rm rag-ingest
   ```

4. Inicie a API:

   ```bash
   docker compose up -d rag-api
   ```

5. Verifique o serviço:

   ```bash
   curl http://127.0.0.1:8080/health
   ```

A API é publicada apenas em `127.0.0.1` por padrão. Os dados do Qdrant permanecem no volume Docker `rag_qdrant-storage` e não fazem parte do repositório Git.

## Exemplo de consulta

```bash
curl -s http://127.0.0.1:8080/v1/query \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "Quais fases fenológicas do cafeeiro exigem maior atenção à disponibilidade hídrica?",
    "top_k": 4
  }'
```

Para recuperar evidências sem gerar texto:

```json
{
  "query": "Quais documentos sustentam o manejo da irrigação por gotejamento?",
  "generate_answer": false,
  "filters": {
    "crop": "coffee",
    "language": "pt-BR"
  }
}
```

## API HTTP

| Método | Caminho | Finalidade |
| --- | --- | --- |
| `GET` | `/health` | Estado do Qdrant, da coleção e do corpus |
| `GET` | `/v1/config` | Configuração efetiva sem segredos |
| `GET` | `/v1/documents` | Inventário do corpus canônico |
| `POST` | `/v1/ingest` | Sincronização incremental ou reconstrução do índice |
| `POST` | `/v1/query` | Recuperação, avaliação e geração opcional de resposta |
| `GET` | `/docs` | Documentação OpenAPI interativa |

Configure `RAG_ADMIN_TOKEN` fora do desenvolvimento local para proteger `/v1/ingest`. Envie o valor em `Authorization: Bearer <token>`.

## Linha de comando

```bash
smart-rag documents
smart-rag config
smart-rag ingest
smart-rag ingest --reset
smart-rag query "Quais documentos discutem irrigação do cafeeiro?"
smart-rag query --no-answer "Quais documentos discutem irrigação do cafeeiro?"
smart-rag serve
```

Para instalação local:

```bash
python3.12 -m venv .venv
.venv/bin/pip install -e '.[dev]'
```

Fora do Compose, configure `RAG_QDRANT_URL=http://127.0.0.1:6333`.

## Configuração padrão da recuperação

| Parâmetro | Padrão |
| --- | --- |
| Provedor de embeddings | OpenRouter |
| Modelo de embeddings | `baai/bge-m3` |
| Modelo de rerank | `cohere/rerank-v3.5` |
| Modelo de planejamento | `meta-llama/llama-3.1-8b-instruct` |
| Temperatura / top-p do planejamento | `0.1` / `1.0` |
| Modelo de resposta | `deepseek/deepseek-v4-flash` |
| Temperatura / top-p da resposta | `0.4` / `1.0` |
| Modelo do juiz de suficiência | `openai/gpt-4o-mini` |
| Temperatura / top-p do juiz | `0.1` / `1.0` |
| `top_k` focado / `top_k` máximo | `3` / `8` |
| Candidatos para rerank | `20` |
| Limiar vetorial / rerank | `0.30` / `0.30` |
| Limite global de evidências | `6` |
| Máximo de chunks por documento | `2` |
| Tamanho / sobreposição dos chunks | `1000` / `150` caracteres |

O planejamento e o rerank estão habilitados por padrão. O juiz de suficiência fica desabilitado; por isso, as respostas recuperadas permanecem `partial`, com `retrieval_sufficiency_not_validated`, até que o juiz seja habilitado e confirme cobertura completa.

## Garantias da ingestão

- Apenas arquivos com `review_status: approved` são aceitos.
- Os PDFs originais permanecem como fontes imutáveis de auditoria e nunca são indexados diretamente.
- O idioma do arquivo deve corresponder à sua subpasta no corpus.
- IDs dos chunks são UUIDv5 derivados do caminho, cabeçalhos, índice e hash do conteúdo.
- Novos vetores são inseridos antes da remoção dos vetores obsoletos.
- Documentos inalterados não são processados novamente.
- Documentos removidos do corpus são retirados do Qdrant durante a sincronização.
- Mudanças na dimensão dos embeddings exigem `smart-rag ingest --reset`.

## Reprodutibilidade científica

Cada experimento deve registrar a revisão Git, hashes do corpus, coleção do Qdrant, modelo e dimensão dos embeddings, parâmetros de chunking, configuração do planejamento, rerank, limiares, modelo de resposta e data de execução. Os julgamentos de relevância migrados do projeto-fonte estão em `evaluation/smart-coffee-rag-qrels-v1.json`.

Aliases de modelos remotos podem mudar de implementação ao longo do tempo. Para experimentos destinados à publicação, preserve os metadados retornados pelo provedor e utilize identificadores fixos sempre que disponíveis.
