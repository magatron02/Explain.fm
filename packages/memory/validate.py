"""Validate attributable episode-memory records."""

from __future__ import annotations

import re
from hashlib import sha256
from pathlib import Path

CITATION = re.compile(r"`([^`\n]+):(\d+)`")
REQUIRED_METADATA = ("episode", "episode_sha256", "scope", "confidence", "evidence_role", "created")
REQUIRED_SECTIONS = (
    "## Listener mental model",
    "## Concepts already introduced",
    "## Open threads",
    "## Evaluation outcome",
    "## Provenance",
)


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


def _repository_file(relative: str, repo_root: Path) -> Path | None:
    target = (repo_root / relative).resolve()
    try:
        target.relative_to(repo_root.resolve())
    except ValueError:
        return None
    return target if target.is_file() else None


def validate_episode_memory(text: str, repo_root: Path) -> list[str]:
    errors: list[str] = []
    metadata = _metadata(text)
    if metadata.get("type") != "episode-memory":
        errors.append("type must be episode-memory")
    if metadata.get("status") not in {"active", "superseded"}:
        errors.append("status must be active or superseded")
    for field in REQUIRED_METADATA:
        if not metadata.get(field):
            errors.append(f"{field} is required")
    if metadata.get("scope") != "global":
        errors.append("episode memory scope must be global")
    if metadata.get("confidence") not in {"low", "medium", "high"}:
        errors.append("confidence must be low, medium, or high")
    if metadata.get("evidence_role") != "context-only":
        errors.append("evidence_role must be context-only")

    episode = metadata.get("episode", "")
    episode_file = _repository_file(episode, repo_root) if episode else None
    if episode and episode_file is None:
        errors.append("episode must reference an existing repository file")
    expected_hash = metadata.get("episode_sha256", "")
    if expected_hash and not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
        errors.append("episode_sha256 must be a lowercase SHA-256")
    elif episode_file and expected_hash and sha256(episode_file.read_bytes()).hexdigest() != expected_hash:
        errors.append("episode_sha256 does not match episode")

    if metadata.get("status") == "superseded":
        replacement = metadata.get("superseded_by", "")
        if not replacement or _repository_file(replacement, repo_root) is None:
            errors.append("superseded memory requires an existing superseded_by file")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing section: {section}")

    citations = CITATION.findall(text)
    if not citations:
        errors.append("at least one provenance citation is required")
    for relative, line_text in citations:
        target = _repository_file(relative, repo_root)
        if target is None:
            errors.append(f"invalid provenance path: {relative}")
            continue
        lines = target.read_text(encoding="utf-8").splitlines()
        line_number = int(line_text)
        if line_number < 1 or line_number > len(lines) or not lines[line_number - 1].strip():
            errors.append(f"invalid provenance line: {relative}:{line_number}")
    return errors
