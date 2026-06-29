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
    top1: int
    mrr: float
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
    top1 = 0
    reciprocal_rank = 0.0
    passed = 0

    for case in cases:
        hits = search(case["query"], source_dir, limit)
        actual = [(hit.path.resolve(), hit.line) for hit in hits]
        actual_set = set(actual)
        expected_targets = {
            ((repo_root / expected["path"]).resolve(), int(expected["line"]))
            for expected in case.get("expected", [])
        }
        acceptable_targets = {
            ((repo_root / expected["path"]).resolve(), int(expected["line"]))
            for expected in case.get("acceptable_any", [])
        }
        relevant_targets = expected_targets | acceptable_targets
        ranks = [rank for rank, target in enumerate(actual, start=1) if target in relevant_targets]
        if ranks:
            top1 += min(ranks) == 1
            reciprocal_rank += 1 / min(ranks)
        if (expected_targets and expected_targets <= actual_set) or acceptable_targets & actual_set:
            passed += 1
        else:
            failures.append(f'{case["query"]}: no acceptable evidence returned')

    total = len(cases)
    return EvaluationResult(
        passed=passed,
        total=total,
        top1=top1,
        mrr=reciprocal_rank / total if total else 0.0,
        failures=tuple(failures),
    )


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
    print(f"top-1: {result.top1}/{result.total}; MRR: {result.mrr:.3f}")
    return 0 if result.total and result.passed == expected_passed else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
