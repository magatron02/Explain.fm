"""Local semantic retrieval that preserves accepted source lines."""

from __future__ import annotations

import json
import math
import os
import sys
import urllib.request
from collections.abc import Callable
from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
sys.path.insert(0, str(REPO_ROOT))

from packages.research.search import (
    DEFAULT_SOURCE_DIR,
    SearchHit,
    _accepted_body_start,
    _searchable,
)

DEFAULT_ENDPOINT = os.getenv("EMBEDDING_ENDPOINT", "http://127.0.0.1:11434/api/embed")
DEFAULT_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text:latest")
Embedder = Callable[[list[str]], list[list[float]]]
Index = list[tuple[SearchHit, list[float]]]


def ollama_embed(texts: list[str]) -> list[list[float]]:
    request = urllib.request.Request(
        DEFAULT_ENDPOINT,
        data=json.dumps({"model": DEFAULT_MODEL, "input": texts}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        embeddings = json.load(response).get("embeddings")
    if not isinstance(embeddings, list) or len(embeddings) != len(texts):
        raise ValueError("embedding endpoint returned an unexpected response")
    return embeddings


def build_index(source_dir: Path = DEFAULT_SOURCE_DIR, embedder: Embedder = ollama_embed) -> Index:
    hits: list[SearchHit] = []
    texts: list[str] = []
    for path in sorted(source_dir.rglob("*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        body_start = _accepted_body_start(lines)
        if body_start is None:
            continue
        for number, line in enumerate(lines[body_start:], start=body_start + 1):
            if _searchable(line):
                snippet = line.strip()
                hits.append(SearchHit(path, number, 0.0, snippet))
                texts.append(f"search_document: Document: {path.stem}. Content: {snippet}")
    return list(zip(hits, embedder(texts))) if texts else []


def _cosine(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("embedding dimensions do not match")
    denominator = math.sqrt(sum(value * value for value in left)) * math.sqrt(
        sum(value * value for value in right)
    )
    return sum(a * b for a, b in zip(left, right)) / denominator if denominator else 0.0


def search_index(query: str, index: Index, limit: int = 5, embedder: Embedder = ollama_embed) -> list[SearchHit]:
    if not query.strip() or limit < 1 or not index:
        return []
    query_vector = embedder([f"search_query: {query}"])[0]
    ranked = [
        SearchHit(hit.path, hit.line, _cosine(query_vector, vector), hit.snippet)
        for hit, vector in index
    ]
    return sorted(ranked, key=lambda hit: (-hit.score, str(hit.path), hit.line))[:limit]


def main(argv: list[str]) -> int:
    if len(argv) not in (2, 3):
        print('usage: python packages/research/semantic_search.py "query" [source-dir]', file=sys.stderr)
        return 2
    source_dir = Path(argv[2]) if len(argv) == 3 else DEFAULT_SOURCE_DIR
    try:
        hits = search_index(argv[1], build_index(source_dir))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"semantic search failed: {exc}", file=sys.stderr)
        return 2
    for hit in hits:
        print(f"{hit.path}:{hit.line} [{hit.score:.3f}] {hit.snippet}")
    return 0 if hits else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
