"""Evaluate the local semantic index against unchanged citation benchmarks."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
sys.path.insert(0, str(REPO_ROOT))

from packages.evaluation.retrieval import evaluate
from packages.research.semantic_search import build_index, search_index

DEFAULT_BENCHMARK = Path("evaluation/benchmarks/cognee-paraphrase-challenge.json")


def main(argv: list[str]) -> int:
    if len(argv) not in (1, 2):
        print("usage: python packages/evaluation/semantic_retrieval.py [benchmark.json]", file=sys.stderr)
        return 2
    benchmark_path = Path(argv[1]) if len(argv) == 2 else DEFAULT_BENCHMARK
    try:
        benchmark = json.loads(benchmark_path.read_text(encoding="utf-8"))
        source_dir = Path.cwd() / "knowledge" / "obsidian" / "sources"
        index = build_index(source_dir)
        result = evaluate(
            benchmark,
            Path.cwd(),
            search=lambda query, _source_dir, limit: search_index(query, index, limit),
        )
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"{benchmark_path}: {exc}", file=sys.stderr)
        return 2
    for failure in result.failures:
        print(f"FAIL {failure}")
    print(f"semantic retrieval cases: {result.passed}/{result.total} passed")
    print(f"top-1: {result.top1}/{result.total}; MRR: {result.mrr:.3f}")
    return 0 if result.total and result.passed == result.total else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
