"""Validate grounded story plans and episode scripts."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
sys.path.insert(0, str(REPO_ROOT))

from packages.research.brief import CITATION, _metadata, validate_research_brief, validate_source_citation

REQUIRED_BEATS = (
    "Hook",
    "Motivation",
    "Problem",
    "Explanation",
    "Examples",
    "Comparison",
    "Common mistakes",
    "Recap",
    "Takeaway",
)
ALLOWED_STATUSES = {"draft", "reviewed", "revise", "blocked"}


def _artifact_path(relative: str, repo_root: Path, directory: str) -> Path | None:
    target = (repo_root / relative).resolve()
    allowed = (repo_root / directory).resolve()
    try:
        target.relative_to(allowed)
    except ValueError:
        return None
    return target if target.is_file() else None


def validate_story_artifact(text: str, repo_root: Path = REPO_ROOT) -> list[str]:
    metadata = _metadata(text)
    artifact_type = metadata.get("type")
    errors: list[str] = []
    if artifact_type not in {"story-plan", "episode-script"}:
        errors.append("type must be story-plan or episode-script")
    if metadata.get("status") not in ALLOWED_STATUSES:
        errors.append(f"status must be one of: {', '.join(sorted(ALLOWED_STATUSES))}")
    if not metadata.get("audience"):
        errors.append("audience is required")

    brief = _artifact_path(metadata.get("research_brief", ""), repo_root, "docs/research")
    if brief is None:
        errors.append("research_brief must reference an existing research brief")
    else:
        for error in validate_research_brief(brief.read_text(encoding="utf-8"), repo_root):
            errors.append(f"research_brief {error}")

    if artifact_type == "story-plan" and not metadata.get("duration"):
        errors.append("duration is required for a story plan")
    if artifact_type == "episode-script":
        plan = _artifact_path(metadata.get("story_plan", ""), repo_root, "docs/design")
        if plan is None:
            errors.append("story_plan must reference an existing story plan")
        speakers = set(re.findall(r"^\*\*([^*\n:]+):\*\*", text, re.MULTILINE))
        if len(speakers) < 2:
            errors.append("episode script requires at least two speakers")

    for beat in REQUIRED_BEATS:
        match = re.search(
            rf"^## {re.escape(beat)}\s*$\n(.*?)(?=^## |\Z)",
            text,
            re.MULTILINE | re.DOTALL,
        )
        if not match:
            errors.append(f"missing beat: {beat}")
            continue
        citations = CITATION.findall(match.group(1))
        if not citations:
            errors.append(f"beat has no evidence citation: {beat}")
            continue
        for relative, line_text in citations:
            error = validate_source_citation(relative, int(line_text), repo_root)
            if error:
                errors.append(f"{beat} {error}")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) not in (2, 3):
        print("usage: python packages/story/validate.py <artifact.md> [repo-root]", file=sys.stderr)
        return 2
    artifact = Path(argv[1])
    repo_root = Path(argv[2]) if len(argv) == 3 else Path.cwd()
    try:
        errors = validate_story_artifact(artifact.read_text(encoding="utf-8"), repo_root)
    except (OSError, UnicodeError) as exc:
        print(f"{artifact}: {exc}", file=sys.stderr)
        return 2
    for error in errors:
        print(f"{artifact}: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"{artifact}: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
