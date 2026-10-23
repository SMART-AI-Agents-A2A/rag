FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN addgroup --system --gid 10001 rag \
    && adduser --system --uid 10001 --ingroup rag --home /app rag

COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --upgrade pip \
    && pip install .

COPY --chown=rag:rag documents ./documents

USER rag
EXPOSE 8080

CMD ["smart-rag", "serve"]

