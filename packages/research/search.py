"""Small, source-faithful retrieval baseline for accepted notes."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

DEFAULT_SOURCE_DIR = Path("knowledge/obsidian/sources")
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how", "in", "into",
    "is", "it", "of", "on", "or", "that", "the", "this", "to", "what", "where", "which", "who",
    "why", "with",
}


@dataclass(frozen=True)
class SearchHit:
    path: Path
    line: int
    score: int
    snippet: str


def _tokens(text: str) -> list[str]:
    return [token for token in re.findall(r"[a-z0-9][a-z0-9_-]+", text.lower()) if token not in STOPWORDS]


def _accepted_body_start(lines: list[str]) -> int | None:
    if not lines or lines[0].strip() != "---":
        return None
    accepted = False
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return index + 1 if accepted else None
        if line.strip() == "status: accepted":
            accepted = True
    return None


def search_sources(query: str, source_dir: Path = DEFAULT_SOURCE_DIR, limit: int = 5) -> list[SearchHit]:
    query_tokens = set(_tokens(query))
    if not query_tokens or limit < 1:
        return []

    # ponytail: linear scan keeps provenance obvious; add an index only when measured corpus size requires it.
    hits: list[SearchHit] = []
    for path in sorted(source_dir.rglob("*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        body_start = _accepted_body_start(lines)
        if body_start is None:
            continue
        for number, line in enumerate(lines[body_start:], start=body_start + 1):
            line_tokens = _tokens(line)
            score = sum(line_tokens.count(token) for token in query_tokens)
            if score:
                hits.append(SearchHit(path=path, line=number, score=score, snippet=line.strip()))

    return sorted(hits, key=lambda hit: (-hit.score, str(hit.path), hit.line))[:limit]


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print('usage: python packages/research/search.py "query" [source-dir]', file=sys.stderr)
        return 2

    source_dir = Path(argv[2]) if len(argv) > 2 else DEFAULT_SOURCE_DIR
    if not source_dir.is_dir():
        print(f"source directory not found: {source_dir}", file=sys.stderr)
        return 2

    hits = search_sources(argv[1], source_dir)
    for hit in hits:
        print(f"{hit.path}:{hit.line} [{hit.score}] {hit.snippet}")
    return 0 if hits else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
