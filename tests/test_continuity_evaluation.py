import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))

from packages.evaluation.continuity import evaluate_continuity
from packages.memory.context import retrieve_episode_context

BENCHMARK = ROOT / "evaluation" / "benchmarks" / "dns-memory-continuity.json"


class ContinuityEvaluationTests(unittest.TestCase):
    def test_dns_query_returns_context_only_episode_memory(self):
        hits = retrieve_episode_context("DNS resolution", ROOT, 1)
        self.assertEqual(len(hits), 1)
        self.assertIn("evidence_role: context-only", hits[0].text)

    def test_unrelated_query_returns_no_episode_memory(self):
        self.assertEqual(retrieve_episode_context("photosynthesis chlorophyll", ROOT), [])

    def test_memory_adds_all_measured_continuity_context(self):
        benchmark = json.loads(BENCHMARK.read_text(encoding="utf-8"))
        result = evaluate_continuity(benchmark, ROOT)
        self.assertEqual((result.control_passed, result.memory_passed, result.total), (0, 5, 5))
        self.assertEqual(result.failures, ())

    def test_planning_experiment_references_resolve(self):
        references = re.compile(r"`([^`\n]+):(\d+)`")
        documents = (ROOT / "evaluation" / "experiments").glob("dns-ttl-followup-*.md")
        for document in documents:
            for relative, line_text in references.findall(document.read_text(encoding="utf-8")):
                target = (ROOT / relative).resolve()
                target.relative_to(ROOT.resolve())
                lines = target.read_text(encoding="utf-8").splitlines()
                line = int(line_text)
                self.assertTrue(1 <= line <= len(lines) and lines[line - 1].strip(), f"{relative}:{line}")


if __name__ == "__main__":
    unittest.main()
