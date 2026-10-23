import os
import socket
import subprocess
import sys
import time
from pathlib import Path

import httpx
import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.startup
def test_application_starts_as_a_real_http_process(tmp_path: Path) -> None:
    with socket.socket() as candidate:
        candidate.bind(("127.0.0.1", 0))
        port = candidate.getsockname()[1]
    environment = {
        **os.environ,
        "RAG_HOST": "127.0.0.1",
        "RAG_PORT": str(port),
        "RAG_QDRANT_URL": "http://127.0.0.1:1",
        "RAG_QDRANT_TIMEOUT_SECONDS": "1",
        "RAG_DOCUMENTS_DIR": str(ROOT / "documents" / "rag"),
    }
    with (tmp_path / "server.log").open("w+") as log:
        process = subprocess.Popen(
            [sys.executable, "-m", "rag", "serve"],
            cwd=tmp_path,
            env=environment,
            stdout=log,
            stderr=subprocess.STDOUT,
        )
        try:
            with httpx.Client(base_url=f"http://127.0.0.1:{port}", timeout=2, trust_env=False) as client:
                deadline = time.monotonic() + 15
                while time.monotonic() < deadline:
                    if process.poll() is not None:
                        log.seek(0)
                        pytest.fail(f"HTTP server exited before startup:\n{log.read()}")
                    try:
                        response = client.get("/openapi.json")
                    except httpx.TransportError:
                        time.sleep(0.1)
                        continue
                    if response.status_code == 200:
                        break
                else:
                    log.seek(0)
                    pytest.fail(f"HTTP server startup timed out:\n{log.read()}")
                assert response.json()["info"]["title"] == "RAG"
                assert len(client.get("/v1/documents").json()) == 11
                assert client.get("/v1/config").json()["collection_name"] == "rag_documents"
                assert client.get("/health").status_code == 503
        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)
