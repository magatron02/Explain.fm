"""Render accepted source evidence as a Markdown handoff."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
sys.path.insert(0, str(REPO_ROOT))

from packages.core.wiki_links import WIKILINK
from packages.research.brief import validate_source_citation
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


def build_topic_evidence_pack(topic: str, repo_root: Path = REPO_ROOT) -> str:
    topic_path = repo_root / "knowledge" / "topics" / f"{Path(topic).stem}.md"
    if not topic_path.is_file():
        raise ValueError(f"reviewed topic not found: {topic}")

    topic_text = topic_path.read_text(encoding="utf-8")
    frontmatter = topic_text.split("---", 2)[1] if topic_text.startswith("---") else ""
    if "status: reviewed" not in frontmatter.splitlines():
        raise ValueError(f"topic is not reviewed: {topic_path.name}")

    source_dir = repo_root / DEFAULT_SOURCE_DIR
    sources = {path.stem.casefold(): path for path in source_dir.glob("*.md")}
    linked_sources: list[Path] = []
    for raw in WIKILINK.findall(topic_text):
        target = Path(raw.split("|", 1)[0].split("#", 1)[0].strip()).stem.casefold()
        if target not in sources:
            raise ValueError(f"topic link is not an accepted source note: {raw}")
        linked_sources.append(sources[target])
    if not linked_sources:
        raise ValueError(f"topic has no source notes: {topic_path.name}")

    claims: list[tuple[str, int, str]] = []
    for source in linked_sources:
        relative = source.relative_to(repo_root).as_posix()
        in_claims = False
        for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), start=1):
            if line == "## Key claims and evidence":
                in_claims = True
                continue
            if in_claims and line.startswith("## "):
                break
            if not in_claims or not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.split("|")[1:-1]]
            if not cells or cells[0].casefold() == "claim" or all(set(cell) <= {"-", ":"} for cell in cells):
                continue
            error = validate_source_citation(relative, line_number, repo_root)
            if error:
                raise ValueError(error)
            claims.append((relative, line_number, cells[0]))

    if not claims:
        raise ValueError(f"topic sources contain no accepted claims: {topic_path.name}")

    lines = [
        "# Topic Evidence Pack",
        "",
        f"**Topic:** {topic_path.stem}",
        "",
        "This artifact contains every accepted claim linked by the reviewed topic. It makes no generated claims.",
        "",
        "| Citation | Accepted claim |",
        "| --- | --- |",
    ]
    for relative, line_number, claim in claims:
        escaped = claim.replace("|", "\\|")
        lines.append(f"| `{relative}:{line_number}` | {escaped} |")
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    if len(argv) not in (2, 3) or (len(argv) == 3 and argv[1] != "--topic"):
        print('usage: python packages/research/evidence_pack.py [--topic] "question-or-topic"', file=sys.stderr)
        return 2
    try:
        pack = (
            build_topic_evidence_pack(argv[2], Path.cwd())
            if len(argv) == 3
            else build_evidence_pack(argv[1], Path.cwd())
        )
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"evidence pack failed: {exc}", file=sys.stderr)
        return 2
    print(pack, end="")
    return 1 if "No accepted evidence found." in pack else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
