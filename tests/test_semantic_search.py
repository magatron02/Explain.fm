import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from packages.research.semantic_search import build_index, search_index


class SemanticSearchTests(unittest.TestCase):
    def test_indexes_accepted_lines_and_preserves_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "Trusted Note.md").write_text(
                "---\nstatus: accepted\n---\nEvidence lives here.\n", encoding="utf-8"
            )
            (root / "Rejected.md").write_text(
                "---\nstatus: inbox\n---\nIgnore this.\n", encoding="utf-8"
            )
            seen: list[str] = []

            def embed(texts: list[str]) -> list[list[float]]:
                seen.extend(texts)
                return [[1.0, 0.0] for _ in texts]

            index = build_index(root, embed)
            hits = search_index("Where is the evidence?", index, embedder=embed)

            self.assertEqual((hits[0].path.name, hits[0].line, hits[0].snippet), (
                "Trusted Note.md", 4, "Evidence lives here."
            ))
            self.assertIn("Document: Trusted Note. Content: Evidence lives here.", seen[0])
            self.assertTrue(seen[-1].startswith("search_query:"))
            self.assertFalse(any("Ignore this" in text for text in seen))

    def test_empty_index_returns_no_hits_without_embedding(self):
        self.assertEqual(search_index("query", [], embedder=lambda _: self.fail()), [])


if __name__ == "__main__":
    unittest.main()
