"""Validate claim-level citations in Explain.fm research briefs."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
sys.path.insert(0, str(REPO_ROOT))

from packages.research.search import _accepted_body_start, _searchable

CITATION = re.compile(r"`([^`\n]+\.md):(\d+)`")
REQUIRED_METADATA = ("status", "question", "audience")
ALLOWED_STATUSES = {"draft", "reviewed", "superseded", "blocked"}


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


def validate_source_citation(relative: str, line_number: int, repo_root: Path) -> str | None:
    source_root = (repo_root / "knowledge" / "obsidian" / "sources").resolve()
    source = (repo_root / relative).resolve()
    try:
        source.relative_to(source_root)
    except ValueError:
        return f"cites outside accepted sources: {relative}"
    if not source.is_file():
        return f"cites missing source: {relative}"
    source_text = source.read_text(encoding="utf-8")
    if not _accepted(source_text):
        return f"cites unaccepted source: {relative}"
    lines = source_text.splitlines()
    body_start = _accepted_body_start(lines)
    if line_number < 1 or line_number > len(lines) or not lines[line_number - 1].strip():
        return f"cites invalid line: {relative}:{line_number}"
    if body_start is None or line_number <= body_start or not _searchable(lines[line_number - 1]):
        return f"cites non-evidence line: {relative}:{line_number}"
    return None


def validate_research_brief(text: str, repo_root: Path) -> list[str]:
    errors: list[str] = []
    metadata = _metadata(text)
    if metadata.get("type") != "research-brief":
        errors.append("type must be research-brief")
    for field in REQUIRED_METADATA:
        if not metadata.get(field):
            errors.append(f"{field} is required")
    status = metadata.get("status")
    if status and status not in ALLOWED_STATUSES:
        errors.append(f"status must be one of: {', '.join(sorted(ALLOWED_STATUSES))}")
    if status == "superseded":
        replacement = metadata.get("superseded_by", "")
        target = (repo_root / replacement).resolve()
        try:
            target.relative_to(repo_root.resolve())
        except ValueError:
            errors.append("superseded_by must stay inside the repository")
        else:
            if not replacement or not target.is_file():
                errors.append("superseded_by must reference an existing repository file")

    rows = _finding_rows(text)
    if not rows:
        errors.append("at least one finding is required")

    for index, cells in enumerate(rows, start=1):
        if len(cells) != 4:
            errors.append(f"finding {index} must have four columns")
            continue
        citations = CITATION.findall(cells[1])
        if not citations:
            errors.append(f"finding {index} has no citation")
            continue
        for relative, line_text in citations:
            error = validate_source_citation(relative, int(line_text), repo_root)
            if error:
                errors.append(f"finding {index} {error}")

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
