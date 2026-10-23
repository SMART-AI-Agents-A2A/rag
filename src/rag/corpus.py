import hashlib
import re
from collections.abc import Iterable
from pathlib import Path
from uuid import NAMESPACE_URL, uuid5

import yaml

from rag.models import Chunk, CorpusDocument, DocumentMetadata, DocumentSummary

FRONTMATTER_BOUNDARY = "---"
SUPPORTED_SUFFIXES = {".md", ".txt"}
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
REQUIRED_METADATA = {
    "title",
    "source",
    "year",
    "crop",
    "region",
    "topic",
    "document_type",
    "language",
    "review_status",
}


class CorpusError(ValueError):
    """Raised when a corpus artifact violates the indexing contract."""


def load_corpus(
    corpus_dir: Path,
    *,
    default_language: str,
    allowed_languages: Iterable[str],
) -> list[CorpusDocument]:
    root = corpus_dir.resolve()
    if not root.is_dir():
        raise CorpusError(f"Corpus directory does not exist: {root}")

    allowed = set(allowed_languages)
    paths = sorted(path for path in root.rglob("*") if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES)
    if not paths:
        raise CorpusError(f"No Markdown or text documents found in {root}")

    documents: list[CorpusDocument] = []
    for path in paths:
        relative_path = path.relative_to(root).as_posix()
        raw = path.read_text(encoding="utf-8")
        frontmatter, content = parse_frontmatter(raw, relative_path=relative_path)
        language = resolve_language(path, root, default_language)
        declared_language = str(frontmatter.get("language", "")).strip()
        if declared_language != language:
            raise CorpusError(
                f"{relative_path}: frontmatter language {declared_language!r} does not match directory {language!r}"
            )
        if language not in allowed:
            raise CorpusError(f"{relative_path}: language {language!r} is not allowed")
        if str(frontmatter.get("review_status", "")).strip().lower() != "approved":
            raise CorpusError(f"{relative_path}: only review_status=approved documents may be indexed")

        metadata = DocumentMetadata.model_validate(frontmatter)
        normalized_content = content.strip()
        if not normalized_content:
            raise CorpusError(f"{relative_path}: document body is empty")
        document_hash = stable_hash(
            yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=True) + "\n" + normalized_content
        )
        documents.append(
            CorpusDocument(
                path=relative_path,
                document_hash=document_hash,
                metadata=metadata,
                content=normalized_content,
            )
        )
    return documents


def parse_frontmatter(raw: str, *, relative_path: str = "document") -> tuple[dict[str, object], str]:
    lines = raw.replace("\r\n", "\n").splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_BOUNDARY:
        raise CorpusError(f"{relative_path}: YAML frontmatter is required")
    try:
        boundary = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == FRONTMATTER_BOUNDARY)
    except StopIteration as exc:
        raise CorpusError(f"{relative_path}: YAML frontmatter is not closed") from exc

    loaded = yaml.safe_load("\n".join(lines[1:boundary]))
    if not isinstance(loaded, dict):
        raise CorpusError(f"{relative_path}: frontmatter must be an object")
    missing = sorted(REQUIRED_METADATA - set(loaded))
    if missing:
        raise CorpusError(f"{relative_path}: missing metadata: {', '.join(missing)}")
    return loaded, "\n".join(lines[boundary + 1 :])


def resolve_language(path: Path, corpus_dir: Path, default_language: str) -> str:
    relative = path.relative_to(corpus_dir)
    return relative.parts[0] if len(relative.parts) > 1 else default_language


def split_corpus(documents: list[CorpusDocument], *, chunk_size: int, chunk_overlap: int) -> list[Chunk]:
    chunks: list[Chunk] = []
    for document in documents:
        chunks.extend(split_document(document, chunk_size=chunk_size, chunk_overlap=chunk_overlap))
    return chunks


def split_document(document: CorpusDocument, *, chunk_size: int, chunk_overlap: int) -> list[Chunk]:
    sections = markdown_sections(document.content)
    chunks: list[Chunk] = []
    chunk_index = 0
    for heading_path, section_content in sections:
        prefix = f"Document: {document.metadata.title}\nSection: {heading_path or document.metadata.title}\n\n"
        available = max(100, chunk_size - len(prefix))
        for segment in split_text(section_content, chunk_size=available, overlap=chunk_overlap):
            content = (prefix + segment.strip()).strip()
            content_hash = stable_hash(content)
            chunk_id = str(
                uuid5(
                    NAMESPACE_URL,
                    f"{document.path}:{heading_path}:{chunk_index}:{content_hash}",
                )
            )
            chunks.append(
                Chunk(
                    id=chunk_id,
                    document_path=document.path,
                    document_hash=document.document_hash,
                    chunk_index=chunk_index,
                    heading_path=heading_path or document.metadata.title,
                    content_hash=content_hash,
                    content=content,
                    metadata=document.metadata,
                )
            )
            chunk_index += 1
    return chunks


def markdown_sections(content: str) -> list[tuple[str, str]]:
    headings: list[str] = []
    current_lines: list[str] = []
    current_path = ""
    sections: list[tuple[str, str]] = []

    def flush() -> None:
        text = "\n".join(current_lines).strip()
        if text:
            sections.append((current_path, text))

    for line in content.splitlines():
        match = HEADING_PATTERN.match(line)
        if match:
            flush()
            current_lines = []
            level = len(match.group(1))
            title = match.group(2).strip()
            headings = headings[: level - 1]
            headings.extend([""] * max(0, level - 1 - len(headings)))
            headings.append(title)
            current_path = " > ".join(value for value in headings if value)
            continue
        current_lines.append(line)
    flush()
    return sections or [("", content.strip())]


def split_text(text: str, *, chunk_size: int, overlap: int) -> list[str]:
    normalized = text.strip()
    if not normalized:
        return []
    if len(normalized) <= chunk_size:
        return [normalized]

    chunks: list[str] = []
    start = 0
    while start < len(normalized):
        hard_end = min(len(normalized), start + chunk_size)
        end = hard_end
        if hard_end < len(normalized):
            paragraph = normalized.rfind("\n\n", start + chunk_size // 2, hard_end)
            sentence = normalized.rfind(". ", start + chunk_size // 2, hard_end)
            space = normalized.rfind(" ", start + chunk_size // 2, hard_end)
            boundary = max(paragraph, sentence + 1 if sentence >= 0 else -1, space)
            if boundary > start:
                end = boundary
        chunk = normalized[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(normalized):
            break
        next_start = max(start + 1, end - overlap)
        start = next_start
    return chunks


def summarize_documents(documents: list[CorpusDocument]) -> list[DocumentSummary]:
    return [
        DocumentSummary(
            path=document.path,
            title=document.metadata.title,
            source=document.metadata.source,
            year=document.metadata.year,
            language=document.metadata.language,
            crop=document.metadata.crop,
            region=document.metadata.region,
            topic=document.metadata.topic,
            document_type=document.metadata.document_type,
            document_hash=document.document_hash,
        )
        for document in documents
    ]


def stable_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()
