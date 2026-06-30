"""Compare planning context with and without episode memory."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
sys.path.insert(0, str(REPO_ROOT))

from packages.memory.context import retrieve_episode_context

DEFAULT_BENCHMARK = Path("evaluation/benchmarks/dns-memory-continuity.json")


@dataclass(frozen=True)
class ContinuityResult:
    control_passed: int
    memory_passed: int
    total: int
    failures: tuple[str, ...]


def _read_repository_file(relative: str, repo_root: Path) -> str:
    path = (repo_root / relative).resolve()
    try:
        path.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise ValueError(f"context path leaves repository: {relative}") from exc
    if not path.is_file():
        raise ValueError(f"context file not found: {relative}")
    return path.read_text(encoding="utf-8")


def evaluate_continuity(benchmark: dict, repo_root: Path) -> ContinuityResult:
    query = benchmark.get("memory_query", "")
    if not query:
        raise ValueError("memory_query is required")
    baseline = "\n".join(_read_repository_file(path, repo_root) for path in benchmark.get("baseline_files", []))
    hits = retrieve_episode_context(query, repo_root, int(benchmark.get("memory_limit", 3)))
    treatment = baseline + "\n" + "\n".join(hit.text for hit in hits)

    control_passed = 0
    memory_passed = 0
    failures: list[str] = []
    cases = benchmark.get("cases", [])
    for case in cases:
        case_id = case.get("id", "")
        required = [text.lower() for text in case.get("required_text", [])]
        if not case_id or not required:
            raise ValueError("every continuity case needs id and required_text")
        control_ok = all(text in baseline.lower() for text in required)
        memory_ok = all(text in treatment.lower() for text in required)
        control_passed += control_ok
        memory_passed += memory_ok
        if not memory_ok:
            failures.append(f"{case_id}: memory context missing required information")

    return ContinuityResult(control_passed, memory_passed, len(cases), tuple(failures))


def main(argv: list[str]) -> int:
    if len(argv) not in (1, 2):
        print("usage: python packages/evaluation/continuity.py [benchmark.json]", file=sys.stderr)
        return 2
    benchmark_path = Path(argv[1]) if len(argv) == 2 else DEFAULT_BENCHMARK
    try:
        benchmark = json.loads(benchmark_path.read_text(encoding="utf-8"))
        result = evaluate_continuity(benchmark, Path.cwd())
    except (OSError, ValueError, TypeError) as exc:
        print(f"{benchmark_path}: {exc}", file=sys.stderr)
        return 2

    print(f"control: {result.control_passed}/{result.total}")
    print(f"memory: {result.memory_passed}/{result.total}")
    for failure in result.failures:
        print(f"FAIL {failure}")
    expected_control = int(benchmark.get("expected_control_passed", 0))
    expected_memory = int(benchmark.get("expected_memory_passed", result.total))
    return 0 if (result.control_passed, result.memory_passed) == (expected_control, expected_memory) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
