"""Render retrieval hits as an evidence-only Markdown handoff."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
sys.path.insert(0, str(REPO_ROOT))

from packages.research.search import DEFAULT_SOURCE_DIR, search_sources


def build_evidence_pack(query: str, repo_root: Path = REPO_ROOT, limit: int = 5) -> str:
    source_dir = repo_root / DEFAULT_SOURCE_DIR
    hits = search_sources(query, source_dir, limit)
    lines = [
        "# Evidence Pack",
        "",
        f"**Question:** {query}",
        "",
        "This artifact contains retrieved accepted-note text only. It makes no generated claims.",
        "",
        "## Retrieved evidence",
        "",
    ]
    if not hits:
        lines.append("No accepted evidence found.")
        return "\n".join(lines) + "\n"

    lines.extend(("| Citation | Score | Accepted note text |", "| --- | ---: | --- |"))
    for hit in hits:
        relative = hit.path.resolve().relative_to(repo_root.resolve()).as_posix()
        snippet = hit.snippet.replace("|", "\\|")
        lines.append(f"| `{relative}:{hit.line}` | {hit.score} | {snippet} |")
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print('usage: python packages/research/evidence_pack.py "question"', file=sys.stderr)
        return 2
    pack = build_evidence_pack(argv[1], Path.cwd())
    print(pack, end="")
    return 1 if "No accepted evidence found." in pack else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
