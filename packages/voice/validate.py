"""Validate a rendered episode against its script and manifest."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]


def _inside(repo_root: Path, relative: str, directory: str) -> Path | None:
    target = (repo_root / relative).resolve()
    try:
        target.relative_to((repo_root / directory).resolve())
    except ValueError:
        return None
    return target if target.is_file() else None


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_audio_manifest(manifest_path: Path, repo_root: Path = REPO_ROOT, probe_audio: bool = True) -> list[str]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    artifact = _inside(repo_root, manifest.get("artifact", ""), "evaluation/golden-episodes")
    script = _inside(repo_root, manifest.get("script", ""), "evaluation/golden-episodes")
    if artifact is None:
        errors.append("artifact must reference an existing golden-episode file")
    elif _sha256(artifact) != manifest.get("artifact_sha256"):
        errors.append("artifact SHA-256 does not match")
    if script is None:
        errors.append("script must reference an existing golden-episode script")
    elif _sha256(script) != manifest.get("script_sha256"):
        errors.append("script SHA-256 does not match")

    renderer = manifest.get("renderer", {})
    for field in ("provider", "space_sha", "model"):
        if not renderer.get(field):
            errors.append(f"renderer {field} is required")
    if not renderer.get("model_revision") and not renderer.get("limitation"):
        errors.append("unknown model revision requires an explicit limitation")

    turns = manifest.get("turns", [])
    results = manifest.get("automated_results", {})
    if not turns or results.get("turns_expected") != len(turns) or results.get("turns_rendered") != len(turns):
        errors.append("turn counts do not match")
    if script is not None:
        source_turns = re.findall(r"^\*\*(MAYA|NARIN):\*\*\s*(.+)$", script.read_text(encoding="utf-8"), re.MULTILINE)
        if len(source_turns) != len(turns):
            errors.append("manifest does not cover every script turn")
        transforms = manifest.get("declared_transformations", {})
        for index, ((speaker, text), turn) in enumerate(zip(source_turns, turns)):
            rendered = text
            for before, after in transforms.items():
                rendered = rendered.replace(before, after)
            if turn.get("index") != index or turn.get("speaker") != speaker or turn.get("script_text") != text:
                errors.append(f"turn {index} does not match the script")
            if turn.get("render_text") != rendered:
                errors.append(f"turn {index} has an undeclared text transformation")

    if probe_audio and artifact is not None:
        ffprobe = shutil.which("ffprobe")
        if not ffprobe:
            errors.append("ffprobe is required for local audio inspection")
        else:
            probe = json.loads(subprocess.check_output([
                ffprobe, "-v", "error", "-show_entries",
                "format=duration,size,bit_rate:stream=codec_name,sample_rate,channels",
                "-of", "json", str(artifact),
            ], text=True))
            stream = probe["streams"][0]
            checks = {
                "codec": stream["codec_name"],
                "sample_rate_hz": int(stream["sample_rate"]),
                "channels": int(stream["channels"]),
                "size_bytes": int(probe["format"]["size"]),
            }
            for field, actual in checks.items():
                if results.get(field) != actual:
                    errors.append(f"audio {field} does not match")
            if abs(float(probe["format"]["duration"]) - float(results.get("duration_seconds", 0))) > 0.05:
                errors.append("audio duration does not match")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) not in (2, 3):
        print("usage: python packages/voice/validate.py <manifest.json> [repo-root]", file=sys.stderr)
        return 2
    manifest = Path(argv[1])
    repo_root = Path(argv[2]) if len(argv) == 3 else Path.cwd()
    try:
        errors = validate_audio_manifest(manifest, repo_root)
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError, subprocess.SubprocessError) as exc:
        print(f"{manifest}: {exc}", file=sys.stderr)
        return 2
    for error in errors:
        print(f"{manifest}: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"{manifest}: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
