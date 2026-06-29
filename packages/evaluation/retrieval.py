"""Evaluate retrieval against exact source-line expectations."""

from __future__ import annotations

import json
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
sys.path.insert(0, str(REPO_ROOT))

from packages.research.search import search_sources

DEFAULT_BENCHMARK = Path("evaluation/benchmarks/cognee-retrieval.json")


@dataclass(frozen=True)
class EvaluationResult:
    passed: int
    total: int
    failures: tuple[str, ...]


def evaluate(
    benchmark: dict,
    repo_root: Path,
    search: Callable[[str, Path, int], list] = search_sources,
) -> EvaluationResult:
    source_dir = repo_root / "knowledge" / "obsidian" / "sources"
    limit = int(benchmark.get("limit", 5))
    failures: list[str] = []
    cases = benchmark.get("cases", [])

    for case in cases:
        hits = search(case["query"], source_dir, limit)
        actual = {(hit.path.resolve(), hit.line) for hit in hits}
        for expected in case.get("expected", []):
            target = ((repo_root / expected["path"]).resolve(), int(expected["line"]))
            if target not in actual:
                failures.append(f'{case["query"]}: missing {expected["path"]}:{expected["line"]}')

    total = len(cases)
    failed_cases = {failure.split(": missing ", 1)[0] for failure in failures}
    return EvaluationResult(passed=total - len(failed_cases), total=total, failures=tuple(failures))


def main(argv: list[str]) -> int:
    if len(argv) not in (1, 2):
        print("usage: python packages/evaluation/retrieval.py [benchmark.json]", file=sys.stderr)
        return 2
    benchmark_path = Path(argv[1]) if len(argv) == 2 else DEFAULT_BENCHMARK
    try:
        benchmark = json.loads(benchmark_path.read_text(encoding="utf-8"))
        result = evaluate(benchmark, Path.cwd())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"{benchmark_path}: {exc}", file=sys.stderr)
        return 2

    for failure in result.failures:
        print(f"FAIL {failure}")
    expected_passed = int(benchmark.get("expected_passed", result.total))
    print(f"retrieval cases: {result.passed}/{result.total} passed (expected {expected_passed})")
    return 0 if result.total and result.passed == expected_passed else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
