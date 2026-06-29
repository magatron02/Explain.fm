"""Validate claim-level citations in Explain.fm research briefs."""

from __future__ import annotations

import re
import sys
from pathlib import Path

CITATION = re.compile(r"`([^`\n]+\.md):(\d+)`")
REQUIRED_METADATA = ("status", "question", "audience")


def _metadata(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    values: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return values
        if line and not line[0].isspace() and ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"\'')
    return {}


def _finding_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    in_findings = False
    for line in text.splitlines():
        if line == "## Findings":
            in_findings = True
            continue
        if in_findings and line.startswith("## "):
            break
        if not in_findings or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        if cells and cells[0].lower() != "claim" and not all(set(cell) <= {"-", ":"} for cell in cells):
            rows.append(cells)
    return rows


def _accepted(text: str) -> bool:
    return _metadata(text).get("status") == "accepted"


def validate_research_brief(text: str, repo_root: Path) -> list[str]:
    errors: list[str] = []
    metadata = _metadata(text)
    if metadata.get("type") != "research-brief":
        errors.append("type must be research-brief")
    for field in REQUIRED_METADATA:
        if not metadata.get(field):
            errors.append(f"{field} is required")

    rows = _finding_rows(text)
    if not rows:
        errors.append("at least one finding is required")

    source_root = (repo_root / "knowledge" / "obsidian" / "sources").resolve()
    for index, cells in enumerate(rows, start=1):
        if len(cells) != 4:
            errors.append(f"finding {index} must have four columns")
            continue
        citations = CITATION.findall(cells[1])
        if not citations:
            errors.append(f"finding {index} has no citation")
            continue
        for relative, line_text in citations:
            source = (repo_root / relative).resolve()
            try:
                source.relative_to(source_root)
            except ValueError:
                errors.append(f"finding {index} cites outside accepted sources: {relative}")
                continue
            if not source.is_file():
                errors.append(f"finding {index} cites missing source: {relative}")
                continue
            source_text = source.read_text(encoding="utf-8")
            if not _accepted(source_text):
                errors.append(f"finding {index} cites unaccepted source: {relative}")
                continue
            line_number = int(line_text)
            lines = source_text.splitlines()
            if line_number < 1 or line_number > len(lines) or not lines[line_number - 1].strip():
                errors.append(f"finding {index} cites invalid line: {relative}:{line_number}")

    for heading in ("## Disagreements and uncertainty", "## Open questions"):
        if heading not in text:
            errors.append(f"missing section: {heading}")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) not in (2, 3):
        print("usage: python packages/research/brief.py <brief.md> [repo-root]", file=sys.stderr)
        return 2
    brief = Path(argv[1])
    repo_root = Path(argv[2]) if len(argv) == 3 else Path.cwd()
    try:
        errors = validate_research_brief(brief.read_text(encoding="utf-8"), repo_root)
    except (OSError, UnicodeError) as exc:
        print(f"{brief}: {exc}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"{brief}: {error}", file=sys.stderr)
        return 1
    print(f"{brief}: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
