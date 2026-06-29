"""Validate Explain.fm Obsidian source notes before ingestion."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED_STATUSES = {"inbox", "reviewed", "accepted", "rejected"}
REQUIRED_FIELDS = (
    "title",
    "source_url",
    "source_type",
    "accessed",
    "authority",
    "license",
    "usage_rights",
)
REQUIRED_HEADINGS = (
    "## Why this source matters",
    "## Scope",
    "## Key claims and evidence",
    "## Limitations and uncertainty",
    "## Raw artifact",
    "## Derived notes",
    "## Review",
)
REVIEW_ITEMS = (
    "Provenance verified",
    "Authority assessed",
    "Usage rights recorded",
    "Claims trace to evidence",
    "Noise and duplication excluded",
)


def _frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, ["missing opening YAML frontmatter delimiter"]

    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, ["missing closing YAML frontmatter delimiter"]

    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values, []


def validate_source_note(text: str) -> list[str]:
    metadata, errors = _frontmatter(text)
    if errors:
        return errors

    if metadata.get("type") != "source":
        errors.append("type must be source")

    status = metadata.get("status", "")
    if status not in ALLOWED_STATUSES:
        errors.append(f"status must be one of: {', '.join(sorted(ALLOWED_STATUSES))}")

    for field in REQUIRED_FIELDS:
        value = metadata.get(field, "")
        if not value or "{{" in value:
            errors.append(f"{field} is required")

    accessed = metadata.get("accessed", "")
    if accessed and "{{" not in accessed and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", accessed):
        errors.append("accessed must use YYYY-MM-DD")

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"missing section: {heading}")

    if status == "accepted":
        for item in REVIEW_ITEMS:
            if not re.search(rf"^- \[[xX]\] {re.escape(item)}$", text, re.MULTILINE):
                errors.append(f"accepted source has incomplete review: {item}")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python packages/core/source_note.py <source-note.md>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    try:
        errors = validate_source_note(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        print(f"{path}: {exc}", file=sys.stderr)
        return 2

    if errors:
        for error in errors:
            print(f"{path}: {error}", file=sys.stderr)
        return 1

    print(f"{path}: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
