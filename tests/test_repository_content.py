import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "packages" / "core"))
sys.path.insert(0, str(ROOT / "packages" / "research"))
sys.path.insert(0, str(ROOT))

from brief import validate_research_brief
from packages.evaluation.retrieval import evaluate
from source_note import validate_source_note
from wiki_links import validate_knowledge_links


class RepositoryContentTests(unittest.TestCase):
    def test_architecture_pipeline_matches_founder_contract(self):
        pipeline = (
            "Sources → Collection → Cleaning → Obsidian Vault → Cognee Memory / Knowledge Graph → "
            "Research Agent → Story Planner → Script Generator → VoxCPM Voice → Audio Episode → Evaluation"
        )
        self.assertIn(pipeline, (ROOT / "ARCHITECTURE.md").read_text(encoding="utf-8"))

    def test_knowledge_wikilinks_resolve_uniquely(self):
        self.assertEqual(validate_knowledge_links(ROOT), [])

    def test_all_accepted_source_notes_are_valid(self):
        source_dir = ROOT / "knowledge" / "obsidian" / "sources"
        notes = [path for path in source_dir.glob("*.md") if path.name != "README.md"]
        self.assertTrue(notes, "repository must contain an accepted source note")
        for path in notes:
            with self.subTest(path=path):
                self.assertEqual(validate_source_note(path.read_text(encoding="utf-8")), [])

    def test_all_research_briefs_have_valid_citations(self):
        brief_dir = ROOT / "docs" / "research"
        briefs = [path for path in brief_dir.glob("*.md") if path.name != "README.md"]
        self.assertTrue(briefs, "repository must contain a research brief")
        for path in briefs:
            with self.subTest(path=path):
                self.assertEqual(validate_research_brief(path.read_text(encoding="utf-8"), ROOT), [])

    def test_all_retrieval_benchmarks_match_recorded_baselines(self):
        benchmark_dir = ROOT / "evaluation" / "benchmarks"
        benchmarks = list(benchmark_dir.glob("*.json"))
        self.assertTrue(benchmarks, "repository must contain a retrieval benchmark")
        for path in benchmarks:
            with self.subTest(path=path):
                benchmark = json.loads(path.read_text(encoding="utf-8"))
                result = evaluate(benchmark, ROOT)
                expected = int(benchmark.get("expected_passed", result.total))
                self.assertEqual(result.passed, expected, result.failures)


if __name__ == "__main__":
    unittest.main()
