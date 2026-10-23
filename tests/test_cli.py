import json
import subprocess
import sys
from pathlib import Path

from rag.cli import main
from rag.service import RagService
from rag.settings import Settings


def test_module_entrypoint_exposes_cli() -> None:
    result = subprocess.run([sys.executable, "-m", "rag", "--help"], capture_output=True, text=True, check=True)
    assert "ingest" in result.stdout
    assert "query" in result.stdout
    assert "serve" in result.stdout


def test_console_entrypoint_is_installed() -> None:
    executable = Path(sys.executable).parent / "rag"
    result = subprocess.run([str(executable), "--help"], capture_output=True, text=True, check=True)
    assert "serve" in result.stdout


def test_config_command_does_not_construct_network_clients(monkeypatch, capsys) -> None:
    def unexpected_client(_: Settings) -> RagService:
        raise AssertionError("config must not initialize external clients")

    monkeypatch.setattr("rag.cli.RagService", unexpected_client)
    main(["config"])
    assert json.loads(capsys.readouterr().out)["collection_name"] == "rag_documents"
