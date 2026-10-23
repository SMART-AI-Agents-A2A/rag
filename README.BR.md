# RAG

[English](README.md)

Serviço de geração aumentada por recuperação (Retrieval-Augmented Generation, RAG) utilizado no projeto para consultar documentos técnicos e produzir respostas fundamentadas em evidências documentais. O repositório contém o serviço HTTP, a interface de linha de comando, o corpus textual, as fontes em PDF, a configuração de execução e os testes automatizados.

## Tipo de RAG e processamento

A implementação se enquadra como **RAG modular com recuperação vetorial densa e recuperação em dois estágios (*retrieve-and-rerank*)**. O planejamento de consultas permite decomposição em múltiplas buscas. Planejamento, reranking, avaliação de suficiência e geração são módulos configuráveis; a busca vetorial é a etapa central de recuperação.

| Propriedade | Implementação |
| --- | --- |
| Unidade de recuperação | Trecho textual (*chunk*) associado ao documento e à seção |
| Representação | Vetor denso gerado por `baai/bge-m3`, com 1.024 dimensões na configuração fornecida |
| Primeiro estágio | Busca por similaridade de cosseno no Qdrant |
| Segundo estágio | Reordenação dos candidatos por `cohere/rerank-v3.5`, habilitada por padrão |
| Planejamento | Uma ou mais subconsultas; no máximo quatro por requisição |
| Restrições | Filtros exatos por idioma, cultura, região, tópico e tipo documental |
| Seleção | Limiar de pontuação, remoção de candidatos repetidos e limite de trechos por documento |
| Geração | Contexto composto pelas evidências selecionadas, com identificadores de citação |
| Avaliação de suficiência | Módulo opcional; desabilitado por padrão |
| Escopo arquitetural | Pipeline documental; sem busca lexical/BM25, grafo de conhecimento ou ciclo autônomo de ferramentas |

| Etapa | Operação | Resultado |
| --- | --- | --- |
| 1. Leitura | Valida metadados YAML e exige `review_status: approved` | Documentos elegíveis à indexação |
| 2. Segmentação | Divide por títulos Markdown e janelas de texto com sobreposição | Trechos com caminho de seção, SHA-256 e UUIDv5 |
| 3. Indexação | Gera embeddings em lotes e sincroniza o Qdrant | Índice vetorial persistente |
| 4. Planejamento | Decompõe a pergunta e restringe filtros ao vocabulário do corpus | Plano de recuperação |
| 5. Recuperação | Gera embeddings das subconsultas e busca candidatos | Passagens ordenadas por similaridade |
| 6. Reranking | Reavalia a relação entre a pergunta e as passagens | Ordenação por relevância |
| 7. Seleção | Aplica os limites de pontuação, quantidade e diversidade documental | Evidências identificadas como `rag:<uuid>` |
| 8. Resposta | Gera texto usando as passagens e verifica os identificadores citados | Resposta, evidências, avaliação de cobertura e metadados |

Se o planejamento falhar, a pergunta original é utilizada. Se o reranking falhar, as pontuações vetoriais são preservadas; elas também são utilizadas quando nenhum resultado do reranking ultrapassa o limiar e há candidatos vetoriais elegíveis. Falhas na geração preservam as evidências e retornam `answer: null`. A verificação de citações exige ao menos um identificador recuperado e rejeita identificadores `rag:` desconhecidos; ela não equivale à verificação semântica de cada afirmação.

## Tecnologias e versões

As dependências diretas estão fixadas em [pyproject.toml](pyproject.toml). As dependências de execução e de testes, incluindo as transitivas, estão em [requirements.lock](requirements.lock) e [requirements-dev.lock](requirements-dev.lock).

| Tecnologia | Versão adotada | Função |
| --- | --- | --- |
| Serviço Python `rag` | `1.0.0` | API, ingestão e recuperação |
| Python | `3.12.x`; imagem `3.12.15-slim` | Runtime; testes locais também executados com `3.12.3` |
| FastAPI | `0.161.1` | Endpoints HTTP e OpenAPI |
| Uvicorn | `0.54.0` | Servidor ASGI |
| Pydantic | `2.14.1` | Contratos de dados |
| Pydantic Settings | `2.16.1` | Configuração por ambiente e `.env` |
| HTTPX | `0.28.1` | Cliente HTTP do provedor |
| PyYAML | `6.0.3` | Leitura dos metadados YAML |
| Qdrant Server | `1.18.0` | Persistência e busca vetorial; imagem `qdrant/qdrant:v1.18.0` |
| Qdrant Client | `1.19.1` | Comunicação com o índice vetorial |
| NumPy | `2.5.4` | Dependência numérica do cliente vetorial |
| PyTest | `9.1.1` | Testes automatizados |
| Ruff | `0.17.2` | Verificação estática e formatação |
| Docker Engine | `29.9.1` no ambiente de execução dos testes | Execução dos contêineres Linux |
| Docker Compose | Plugin `5.6.0` nos testes; requer `2.24.0` ou superior | Serviços, dependências, perfis e volumes |

## Modelos e parâmetros

Os modelos são acessados pelo OpenRouter, nos endpoints `https://openrouter.ai/api/v1/embeddings`, `/rerank` e `/chat/completions`. Os identificadores abaixo são valores de configuração do serviço. A execução das etapas remotas exige uma chave com acesso aos modelos correspondentes.

| Etapa | Provedor | Identificador do modelo | Temperatura | `top_p` | Estado padrão |
| --- | --- | --- | --- | --- | --- |
| Embeddings | OpenRouter | `baai/bge-m3` | Não se aplica | Não se aplica | Obrigatória para indexar e consultar |
| Planejamento | OpenRouter | `meta-llama/llama-3.1-8b-instruct` | `0.5` | `1.0` | Habilitado |
| Reranking | OpenRouter | `cohere/rerank-v3.5` | Não se aplica | Não se aplica | Habilitado |
| Geração | OpenRouter | `deepseek/deepseek-v4-flash` | `0.7` | `1.0` | Habilitada; máximo de 900 tokens de saída |
| Suficiência | OpenRouter | `openai/gpt-4o-mini` | `0.5` | `1.0` | Desabilitada |

Temperatura e `top_p` são enviados nas chamadas de geração de texto. Os endpoints de embeddings e reranking recebem seus próprios parâmetros de tarefa, sem parâmetros de amostragem textual. Esses valores são configurações operacionais, não resultados de otimização experimental. As interfaces do provedor estão descritas na [documentação de RAG do OpenRouter](https://openrouter.ai/docs/guides/evaluate-and-optimize/rag).

| Parâmetro de recuperação | Valor padrão | Interpretação |
| --- | --- | --- |
| Tamanho alvo do trecho | `1000` caracteres | Inclui o prefixo com documento e seção; não é uma contagem de tokens |
| Sobreposição | `150` caracteres | Reutiliza contexto entre janelas da mesma seção |
| Lote de embeddings | `32` textos | Quantidade máxima por chamada de ingestão |
| `top_k` / máximo solicitado | `3` / `8` | Número desejado de evidências e limite configurado |
| Limite global | `6` | Também restringe o total retornado, mesmo quando `top_k=8` |
| Trechos por documento | `2` | Limita a concentração em uma única fonte |
| Candidatos | `20` | Quantidade alvo distribuída entre as subconsultas |
| Subconsultas | Até `4` | Limite aplicado ao plano da pergunta |
| Limiar vetorial | `0.30` | Corte aplicado à similaridade de cosseno |
| Limiar do reranking | `0.30` | Corte aplicado à pontuação do reranker |

As duas pontuações têm escalas distintas. A resposta informa qual escala foi aplicada em `metadata.score_kind` e qual limiar foi usado em `metadata.score_threshold`.

## Organização dos documentos

O corpus contém **11 arquivos Markdown e 11 PDFs**, distribuídos em sete documentos textuais em português, três em inglês e um em espanhol. As pastas de idioma identificam a representação textual usada na recuperação.

| Artefato | Localização | Motivo e uso |
| --- | --- | --- |
| PDF original | [documents/sources/raw/](documents/sources/raw/) | Preserva paginação, tabelas, figuras e formatação para conferência das fontes; não é indexado diretamente |
| Markdown (`.md`) | [documents/rag/](documents/rag/) | Representação textual versionável; títulos e seções orientam a segmentação e permitem inspecionar o texto efetivamente recuperado |
| Frontmatter YAML | Início de cada `.md` | Define título, fonte, ano, idioma, cultura, região, tópico, tipo e estado de revisão |
| Texto (`.txt`) | Aceito em `documents/rag/` | Alternativa suportada pelo leitor; exige o mesmo frontmatter; não há arquivos `.txt` no corpus fornecido |
| Manifesto JSON | [documents/sources/manifest.json](documents/sources/manifest.json) | Associa cada PDF à sua representação Markdown e aos metadados bibliográficos |
| Julgamentos de relevância | [evaluation/qrels-v1.json](evaluation/qrels-v1.json) | Dois registros de referência com fontes e conceitos esperados; não constituem uma coleção completa de perguntas de avaliação |
| Índice vetorial | Volume Docker `qdrant-storage` | Artefato derivado dos textos e embeddings, reconstruído pela ingestão |

| PDF incluído | Representação Markdown | Idioma | Conteúdo utilizado na recuperação |
| --- | --- | --- | --- |
| [Fenologiadocafeeiro.pdf](documents/sources/raw/Fenologiadocafeeiro.pdf) | [fenologia-balanco-hidrico-cafeeiro.md](documents/rag/pt-BR/fenologia-balanco-hidrico-cafeeiro.md) | `pt-BR` | Fenologia, condições agrometeorológicas e balanço hídrico |
| [Cirtec32.pdf](documents/sources/raw/Cirtec32.pdf) | [coeficientes-tecnicos-irrigacao-cafeeiro-cerrado.md](documents/rag/pt-BR/coeficientes-tecnicos-irrigacao-cafeeiro-cerrado.md) | `pt-BR` | Coeficientes técnicos e manejo da irrigação no Cerrado |
| [admin_Biosci-2006-291.pdf](documents/sources/raw/admin_Biosci-2006-291.pdf) | [manejo-irrigacao-gotejamento-cafeeiro.md](documents/rag/pt-BR/manejo-irrigacao-gotejamento-cafeeiro.md) | `pt-BR` | Manejo da irrigação por gotejamento |
| [AP-Implantacao-agricultura-2024.pdf](documents/sources/raw/AP-Implantacao-agricultura-2024.pdf) | [agricultura-precisao-cafes-especiais-sul-minas.md](documents/rag/pt-BR/agricultura-precisao-cafes-especiais-sul-minas.md) | `pt-BR` | Agricultura de precisão e manejo diferenciado |
| [Cafe-na-AmazoniaDENIS.pdf](documents/sources/raw/Cafe-na-AmazoniaDENIS.pdf) | [irrigacao-cafeeiros-amazonia-rondonia.md](documents/rag/pt-BR/irrigacao-cafeeiros-amazonia-rondonia.md) | `pt-BR` | Necessidade hídrica e irrigação na Amazônia |
| [Coffea arabica L.pdf](documents/sources/raw/Coffea%20arabica%20L.pdf) | [coffea-arabica-fenologia-clima.md](documents/rag/pt-BR/coffea-arabica-fenologia-clima.md) | `pt-BR` | Fenologia e aptidão climática |
| [CarlosReisserdigitalizar0009.pdf](documents/sources/raw/CarlosReisserdigitalizar0009.pdf) | [vantagens-irrigacao-gotejamento.md](documents/rag/pt-BR/vantagens-irrigacao-gotejamento.md) | `pt-BR` | Gotejamento, fertirrigação, filtragem e limitações operacionais |
| [Manualagricultura.pdf](documents/sources/raw/Manualagricultura.pdf) | [manual-agricultura-precision.md](documents/rag/es/manual-agricultura-precision.md) | `es` | Diagnóstico e implantação de agricultura de precisão |
| [manual-for-arabica-cultivation-vs.pdf](documents/sources/raw/manual-for-arabica-cultivation-vs.pdf) | [manual-arabica-cultivation-vietnam.md](documents/rag/en/manual-arabica-cultivation-vietnam.md) | `en` | Práticas de cultivo de arábica |
| [smart_project_final.pdf](documents/sources/raw/smart_project_final.pdf) | [smart-sustainable-management-agriculture-computing-continuum.md](documents/rag/en/smart-sustainable-management-agriculture-computing-continuum.md) | `en` | Agricultura sustentável, sensoriamento e computação distribuída |
| [FAOIrrigation andDrainagePaperNo56.pdf](documents/sources/raw/FAOIrrigation%20andDrainagePaperNo56.pdf) | [fao-irrigation-drainage-paper-56-crop-evapotranspiration.md](documents/rag/en/fao-irrigation-drainage-paper-56-crop-evapotranspiration.md) | `en` | Evapotranspiração, coeficientes de cultura e necessidade hídrica |

O carregador verifica a estrutura e o estado declarado dos documentos. O PDF permite conferir diferenças de extração, OCR, tradução e representação de tabelas. Alterações nos arquivos Markdown passam a integrar o índice na ingestão seguinte. Alterações no modelo de embedding, dimensão ou parâmetros de segmentação exigem reconstrução com `rag ingest --reset`.

## Configuração do ambiente

```bash
cp env.example .env
```

Substitua `RAG_OPENROUTER_API_KEY` pela chave do provedor e `RAG_ADMIN_TOKEN` pelo token escolhido para a ingestão HTTP. O arquivo [env.example](env.example) contém todos os parâmetros do serviço e as duas portas publicadas pelo Compose. O `.env` não é versionado.

| Variáveis | Valores fornecidos | Uso |
| --- | --- | --- |
| `RAG_HOST`, `RAG_PORT` | `0.0.0.0`, `8080` | Endereço e porta do processo HTTP |
| `RAG_API_PORT`, `RAG_QDRANT_PORT` | `8080`, `6333` | Portas do host publicadas pelo Compose |
| `RAG_LOG_LEVEL` | `INFO` | Nível de logs |
| `RAG_ADMIN_TOKEN` | Substituir o marcador | Bearer token de `/v1/ingest`; vazio desabilita essa autenticação |
| `RAG_QDRANT_URL` | `http://127.0.0.1:6333` | URL para execução local; no Compose é definida como `http://qdrant:6333` |
| `RAG_QDRANT_API_KEY` | Vazio | Credencial opcional do Qdrant; o Compose aplica o mesmo valor ao servidor |
| `RAG_QDRANT_TIMEOUT_SECONDS` | `20` | Timeout das operações vetoriais |
| `RAG_COLLECTION_NAME` | `rag_documents` | Coleção vetorial |
| `RAG_DOCUMENTS_DIR` | `documents/rag` | Diretório do corpus; no contêiner, `/app/documents/rag` |
| `RAG_DEFAULT_LANGUAGE`, `RAG_ALLOWED_LANGUAGES` | `pt-BR`, `pt-BR,en,es` | Idioma de arquivos sem subpasta e idiomas aceitos |
| `RAG_OPENROUTER_API_KEY` | Substituir o marcador | Credencial para embeddings, reranking e geração |
| `RAG_OPENROUTER_BASE_URL` | `https://openrouter.ai/api/v1` | Base HTTP do provedor |
| `RAG_OPENROUTER_TIMEOUT_SECONDS`, `RAG_OPENROUTER_RETRY_ATTEMPTS` | `45`, `3` | Timeout e número máximo de tentativas |
| `RAG_EMBEDDING_MODEL`, `RAG_EMBEDDING_DIMENSION` | `baai/bge-m3`, `1024` | Modelo e dimensão esperada |
| `RAG_QUERY_PLANNING_ENABLED`, `RAG_QUERY_MODEL`, `RAG_QUERY_TEMPERATURE`, `RAG_QUERY_TOP_P` | `true`, modelo da tabela, `0.5`, `1.0` | Planejamento |
| `RAG_RERANK_ENABLED`, `RAG_RERANK_MODEL`, `RAG_RERANK_CANDIDATES` | `true`, modelo da tabela, `20` | Reranking |
| `RAG_ANSWER_ENABLED`, `RAG_ANSWER_MODEL`, `RAG_ANSWER_TEMPERATURE`, `RAG_ANSWER_TOP_P`, `RAG_ANSWER_MAX_TOKENS` | `true`, modelo da tabela, `0.7`, `1.0`, `900` | Geração da resposta |
| `RAG_SUFFICIENCY_JUDGE_ENABLED`, `RAG_SUFFICIENCY_JUDGE_MODEL`, `RAG_SUFFICIENCY_JUDGE_TEMPERATURE`, `RAG_SUFFICIENCY_JUDGE_TOP_P` | `false`, modelo da tabela, `0.5`, `1.0` | Avaliação opcional de suficiência |
| `RAG_TOP_K`, `RAG_MAX_TOP_K`, `RAG_GLOBAL_EVIDENCE_LIMIT`, `RAG_MAX_CHUNKS_PER_DOCUMENT`, `RAG_MAX_SUBQUERIES` | `3`, `8`, `6`, `2`, `4` | Limites de recuperação |
| `RAG_VECTOR_SCORE_THRESHOLD`, `RAG_RERANK_SCORE_THRESHOLD` | `0.30`, `0.30` | Limiares de seleção |
| `RAG_CHUNK_SIZE`, `RAG_CHUNK_OVERLAP`, `RAG_EMBEDDING_BATCH_SIZE` | `1000`, `150`, `32` | Segmentação e ingestão |

## Docker e Docker Compose

O [Dockerfile](Dockerfile) possui os alvos `runtime` e `test`. A imagem contém o pacote instalado, o corpus Markdown e os PDFs. O [docker-compose.yml](docker-compose.yml) configura a API, o Qdrant, a ingestão e a execução dos testes.

```bash
docker compose build rag-api rag-ingest
docker compose up -d --wait qdrant
docker compose --profile maintenance run --rm rag-ingest
docker compose up -d --wait rag-api
curl --fail http://127.0.0.1:8080/health
```

A ingestão utiliza a chave OpenRouter do `.env`. A API pode iniciar antes da ingestão para expor o inventário e a configuração; consultas retornam `not_available` enquanto a coleção não existir.

| Serviço | Endereço no host | Endereço na rede Compose | Persistência e função |
| --- | --- | --- | --- |
| `rag-api` | `127.0.0.1:8080` | `rag-api:8080` | API; montagem de `./documents` somente para leitura |
| `qdrant` HTTP | `127.0.0.1:6333` | `qdrant:6333` | Índice no volume `qdrant-storage` |
| `qdrant` gRPC | Não publicado | `qdrant:6334` | Disponível na imagem; o serviço utiliza HTTP |
| `rag-ingest` | Nenhuma porta | Acessa `qdrant:6333` | Processo de ingestão no perfil `maintenance` |
| `rag-tests` | Nenhuma porta fixa | Acessa `qdrant:6333` | PyTest no perfil `test`; servidor de teste usa porta efêmera |
| OpenRouter | HTTPS de saída na porta `443` | `openrouter.ai:443` | Serviço remoto de modelos |

Se as portas do host estiverem ocupadas, altere `RAG_API_PORT` e `RAG_QDRANT_PORT` no `.env`; os endereços internos permanecem os da tabela. Na execução local, ajuste também `RAG_QDRANT_URL` quando mudar a porta publicada do Qdrant.

```bash
docker compose ps
docker compose logs --tail=100 rag-api
docker compose down
```

`docker compose down` encerra os serviços e preserva o volume do índice.

## Execução local e CLI

Execute os comandos a partir da raiz do repositório:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.lock -e '.[dev]'
docker compose up -d --wait qdrant
.venv/bin/rag documents
.venv/bin/rag config
.venv/bin/rag ingest
.venv/bin/rag serve
```

| Comando | Operação |
| --- | --- |
| `rag documents` | Lista documentos e metadados |
| `rag config` | Exibe os parâmetros públicos, sem credenciais |
| `rag ingest` | Indexa documentos novos ou alterados e remove documentos excluídos |
| `rag ingest --reset` | Recria a coleção e todos os vetores |
| `rag query "pergunta"` | Recupera evidências e gera resposta conforme configuração |
| `rag query --no-answer "pergunta"` | Executa recuperação sem gerar resposta |
| `rag serve` | Inicia o servidor HTTP |
| `python -m rag` | Ponto de entrada equivalente ao comando `rag` |

A ingestão não recalcula embeddings de documentos com hash inalterado. Na atualização, grava novos trechos antes de remover os identificadores obsoletos.

## API HTTP

| Método | Caminho | Entrada e retorno |
| --- | --- | --- |
| `GET` | `/health` | `200` com Qdrant e corpus acessíveis; `503` em estado degradado; informa separadamente a existência da coleção |
| `GET` | `/v1/config` | Configuração pública dos modelos, limites e segmentação |
| `GET` | `/v1/documents` | Inventário do corpus com metadados e SHA-256 |
| `POST` | `/v1/ingest` | Corpo `{"reset": false}`; exige Bearer token quando configurado |
| `POST` | `/v1/query` | Pergunta, filtros e opções; retorna evidências, plano, avaliação e resposta opcional |
| `GET` | `/docs` | Interface interativa da API |
| `GET` | `/openapi.json` | Especificação OpenAPI |

```bash
curl --fail http://127.0.0.1:8080/v1/query \
  -H 'Content-Type: application/json' \
  -d '{"query":"Quais documentos abordam o manejo da irrigação?","top_k":3,"generate_answer":true,"filters":{"language":"pt-BR"}}'
```

| Campo da consulta | Tipo | Comportamento |
| --- | --- | --- |
| `query` | Texto, 2 a 4.000 caracteres | Obrigatório; espaços são normalizados |
| `top_k` | Inteiro opcional, 1 a 20 | Sujeito a `RAG_MAX_TOP_K` e ao limite global |
| `generate_answer` | Booleano opcional | Sobrescreve a opção global de geração para esta requisição |
| `filters` | Objeto opcional | `language`, `crop`, `region`, `topic`, `document_type`; valores exatos do inventário |

Os filtros enviados explicitamente prevalecem sobre filtros de planejamento. Omissão do filtro de idioma permite recuperação entre idiomas.

| Estado da resposta | Significado |
| --- | --- |
| `ok` | O juiz de suficiência confirmou cobertura completa |
| `partial` | Há evidências, mas a cobertura completa não foi confirmada |
| `collection_gap` | Nenhum candidato ultrapassou o limiar de seleção |
| `not_available` | A coleção ainda não existe |
| `source_error` | Falha no acesso ao índice ou na recuperação de embeddings |

Com o juiz desabilitado, respostas com evidências permanecem `partial`, com a indicação `retrieval_sufficiency_not_validated`. O estado documental é retornado no corpo JSON, inclusive quando o HTTP é `200`.

## Testes automatizados

```bash
.venv/bin/python -m pytest
.venv/bin/ruff check src tests
.venv/bin/ruff format --check src tests
```

| Arquivo | Comportamento verificado | Dependências externas |
| --- | --- | --- |
| `tests/test_startup.py` | Inicia `python -m rag serve` em processo real e consulta os endpoints | Socket HTTP local; sem chave de modelos |
| `tests/test_api.py` | OpenAPI, inventário, ingestão, consulta, autenticação, validação e estados de erro | Qdrant em memória e transporte HTTP controlado |
| `tests/test_cli.py` | Instalação do comando `rag`, módulo Python e configuração | Sem rede |
| `tests/test_ingestion.py` | Idempotência, atualização, exclusão e reconstrução | Qdrant em memória e transporte controlado |
| `tests/test_corpus.py` | Corpus, identificadores estáveis, presença e cabeçalho dos PDFs, manifesto e qrels | Arquivos incluídos no repositório |
| `tests/test_providers.py` | Contratos de embeddings, JSON e filtros | Transporte HTTP controlado |
| `tests/test_service.py` | Seleção, diversidade de fontes e citações | Clientes de teste |
| `tests/test_settings.py` | Carregamento integral do `env.example` e restrições de configuração | Sem rede |
| `tests/test_qdrant.py` | Ingestão e busca no servidor, idempotência e dimensão vetorial | Qdrant real; ativado por `--qdrant-url` |
| `tests/test_live_provider.py` | Embeddings, planejamento, reranking e geração nos modelos configurados | OpenRouter real; ativado por `--live-provider` |

Para executar os testes com Qdrant real pelo Compose, sem credenciais de modelos:

```bash
docker compose --profile test run --build --rm rag-tests
```

Ou, com o PyTest local:

```bash
docker compose up -d --wait qdrant
.venv/bin/python -m pytest --qdrant-url=http://127.0.0.1:6333
```

Os testes de servidor utilizam coleções temporárias `pytest_<uuid>` e as removem ao terminar. Os testes locais controlam o transporte das chamadas de modelos; não medem qualidade semântica ou desempenho dos modelos remotos. Os testes externos ficam marcados como `skipped` quando suas opções não são fornecidas.

Para testar o provedor com a chave do `.env` e realizar chamadas faturáveis aos modelos configurados:

```bash
.venv/bin/python -m pytest --live-provider -m live
```

Esse teste utiliza dois documentos de teste e Qdrant em memória. Ele exige evidências, resposta com citações e sucesso das etapas habilitadas; a execução falha se as credenciais, os modelos ou seus endpoints estiverem indisponíveis.

## Estrutura do código

| Caminho | Responsabilidade |
| --- | --- |
| `src/rag/api.py` | Rotas HTTP e autenticação administrativa |
| `src/rag/cli.py` | Comandos de execução |
| `src/rag/settings.py` | Parâmetros e validações |
| `src/rag/models.py` | Contratos de requisição, resposta e documentos |
| `src/rag/corpus.py` | Leitura, metadados, hashes e segmentação |
| `src/rag/providers.py` | Cliente dos endpoints de modelos |
| `src/rag/store.py` | Coleções, vetores, filtros e busca no Qdrant |
| `src/rag/service.py` | Pipeline de ingestão, recuperação e geração |

Para registrar uma execução, preserve a revisão Git, o conteúdo de `/v1/config`, os hashes retornados por `/v1/documents`, a dimensão vetorial, a consulta, os filtros e a resposta completa. Os identificadores de modelos são remotos; a data da execução e os metadados do provedor devem acompanhar resultados experimentais.
