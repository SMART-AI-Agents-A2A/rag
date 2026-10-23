FROM python:3.12.15-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN addgroup --system --gid 10001 rag \
    && adduser --system --uid 10001 --ingroup rag --home /app rag

COPY pyproject.toml README.md requirements.lock ./
COPY src ./src
RUN pip install --requirement requirements.lock .

COPY --chown=rag:rag documents ./documents

FROM base AS test

COPY requirements-dev.lock ./
RUN pip install --requirement requirements-dev.lock
COPY --chown=rag:rag tests ./tests
COPY --chown=rag:rag evaluation ./evaluation
COPY --chown=rag:rag env.example docker-compose.yml Dockerfile ./

USER rag
CMD ["python", "-m", "pytest", "-p", "no:cacheprovider"]

FROM base AS runtime

USER rag
EXPOSE 8080

CMD ["rag", "serve"]

