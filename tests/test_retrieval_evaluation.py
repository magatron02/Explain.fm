import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from packages.evaluation.retrieval import evaluate


class RetrievalEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        source = self.root / "knowledge" / "obsidian" / "sources" / "source.md"
        source.parent.mkdir(parents=True)
        source.write_text("---\nstatus: accepted\n---\nGraph evidence.\n", encoding="utf-8")

    def tearDown(self):
        self.temporary.cleanup()

    def test_expected_citation_passes(self):
        benchmark = {
            "cases": [{
                "query": "graph",
                "expected": [{"path": "knowledge/obsidian/sources/source.md", "line": 4}],
            }]
        }
        result = evaluate(benchmark, self.root)
        self.assertEqual((result.passed, result.total, result.failures), (1, 1, ()))
        self.assertEqual((result.top1, result.mrr), (1, 1.0))

    def test_missing_citation_fails(self):
        benchmark = {
            "cases": [{
                "query": "absent",
                "expected": [{"path": "knowledge/obsidian/sources/source.md", "line": 4}],
            }]
        }
        result = evaluate(benchmark, self.root)
        self.assertEqual(result.passed, 0)
        self.assertEqual(len(result.failures), 1)

    def test_rank_metrics_expose_relevant_result_in_second_place(self):
        source = self.root / "knowledge" / "obsidian" / "sources" / "source.md"
        source.write_text(
            "---\nstatus: accepted\n---\nGraph graph decoy.\nGraph evidence.\n",
            encoding="utf-8",
        )
        benchmark = {
            "cases": [{
                "query": "graph",
                "expected": [{"path": "knowledge/obsidian/sources/source.md", "line": 5}],
            }]
        }

        result = evaluate(benchmark, self.root)

        self.assertEqual((result.passed, result.top1, result.mrr), (1, 0, 0.5))


if __name__ == "__main__":
    unittest.main()
