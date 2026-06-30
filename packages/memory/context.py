"""Retrieve relevant, context-only episode memory."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from packages.memory.validate import validate_episode_memory

STOPWORDS = {"a", "an", "and", "episode", "for", "in", "of", "on", "the", "to", "what"}


@dataclass(frozen=True)
class EpisodeContextHit:
    path: Path
    score: int
    text: str


def _tokens(text: str) -> list[str]:
    return [
        token
        for token in re.findall(r"[^\W_]+(?:[-_][^\W_]+)*", text.lower(), re.UNICODE)
        if token not in STOPWORDS
    ]


def retrieve_episode_context(query: str, repo_root: Path, limit: int = 3) -> list[EpisodeContextHit]:
    query_tokens = set(_tokens(query))
    if not query_tokens or limit < 1:
        return []

    # ponytail: a linear scan is sufficient until the measured episode corpus makes it slow.
    hits: list[EpisodeContextHit] = []
    for path in sorted((repo_root / "memory" / "episodes").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        errors = validate_episode_memory(text, repo_root)
        if errors:
            raise ValueError(f"{path}: {'; '.join(errors)}")
        if not re.search(r"^status:\s*active\s*$", text, re.MULTILINE):
            continue
        words = _tokens(text)
        score = sum(words.count(token) for token in query_tokens)
        if score:
            hits.append(EpisodeContextHit(path=path, score=score, text=text))
    return sorted(hits, key=lambda hit: (-hit.score, str(hit.path)))[:limit]
