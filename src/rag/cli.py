import argparse
import json
import logging
from collections.abc import Sequence

import uvicorn

from rag.models import QueryRequest
from rag.service import RagService
from rag.settings import get_settings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="rag", description="Documentary retrieval and generation service")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("serve", help="Start the HTTP API")

    ingest = subparsers.add_parser("ingest", help="Synchronize the approved corpus with Qdrant")
    ingest.add_argument("--reset", action="store_true", help="Recreate the collection before indexing")

    query = subparsers.add_parser("query", help="Retrieve evidence and optionally generate an answer")
    query.add_argument("query", help="Natural-language documentary question")
    query.add_argument("--top-k", type=int, default=None)
    query.add_argument("--no-answer", action="store_true", help="Return evidence without answer generation")

    subparsers.add_parser("documents", help="List canonical corpus documents")
    subparsers.add_parser("config", help="Print the effective non-secret configuration")
    return parser


def main(argv: Sequence[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    settings = get_settings()
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    if args.command == "serve":
        uvicorn.run(
            "rag.api:app",
            host=settings.host,
            port=settings.port,
            log_level=settings.log_level.lower(),
        )
        return

    if args.command == "config":
        print(json.dumps(settings.public_configuration(), ensure_ascii=False, indent=2))
        return

    service = RagService(settings)
    try:
        if args.command == "ingest":
            output = service.ingest(reset=args.reset)
        elif args.command == "query":
            output = service.query(
                QueryRequest(
                    query=args.query,
                    top_k=args.top_k,
                    generate_answer=False if args.no_answer else None,
                )
            )
        elif args.command == "documents":
            output = service.list_documents()
        else:  # argparse makes this unreachable
            raise RuntimeError(f"unsupported command: {args.command}")
        if isinstance(output, list):
            payload = [item.model_dump(mode="json") for item in output]
        else:
            payload = output.model_dump(mode="json")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    finally:
        service.close()


if __name__ == "__main__":
    main()
