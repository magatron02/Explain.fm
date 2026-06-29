"""Validate Obsidian links in the Explain.fm knowledge tree."""

from __future__ import annotations

import re
import sys
from pathlib import Path

WIKILINK = re.compile(r"!?\[\[([^\]]+)\]\]")


def validate_knowledge_links(repo_root: Path) -> list[str]:
    notes = list(repo_root.rglob("*.md"))
    by_stem: dict[str, list[Path]] = {}
    for note in notes:
        by_stem.setdefault(note.stem.casefold(), []).append(note)

    errors: list[str] = []
    for note in (repo_root / "knowledge").rglob("*.md"):
        for raw in WIKILINK.findall(note.read_text(encoding="utf-8")):
            target = raw.split("|", 1)[0].split("#", 1)[0].strip()
            if not target:
                continue
            if "/" in target or "\\" in target:
                candidate = repo_root / target
                if candidate.suffix.lower() != ".md":
                    candidate = candidate.with_suffix(".md")
                if not candidate.is_file():
                    errors.append(f"{note.relative_to(repo_root)}: missing link {raw}")
                continue
            matches = by_stem.get(Path(target).stem.casefold(), [])
            if not matches:
                errors.append(f"{note.relative_to(repo_root)}: missing link {raw}")
            elif len(matches) > 1:
                errors.append(f"{note.relative_to(repo_root)}: ambiguous link {raw}")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) not in (1, 2):
        print("usage: python packages/core/wiki_links.py [repo-root]", file=sys.stderr)
        return 2
    root = Path(argv[1]) if len(argv) == 2 else Path.cwd()
    errors = validate_knowledge_links(root)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print("knowledge wikilinks: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
