import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "packages" / "research"))

from search import search_sources


class SearchTests(unittest.TestCase):
    def test_returns_citable_line_from_accepted_source_only(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "accepted.md").write_text(
                "---\nstatus: accepted\n---\nRelational storage preserves provenance.\n",
                encoding="utf-8",
            )
            (root / "inbox.md").write_text(
                "---\nstatus: inbox\n---\nGraph provenance should not appear.\n",
                encoding="utf-8",
            )

            hits = search_sources("provenance", root)

            self.assertEqual(len(hits), 1)
            self.assertEqual(hits[0].path.name, "accepted.md")
            self.assertEqual(hits[0].line, 4)

    def test_empty_query_returns_no_hits(self):
        self.assertEqual(search_sources(""), [])

    def test_frontmatter_is_not_searchable(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "source.md").write_text(
                "---\nstatus: accepted\ntopics: [provenance]\n---\nNo matching body term.\n",
                encoding="utf-8",
            )

            self.assertEqual(search_sources("provenance", root), [])

    def test_stopwords_do_not_create_false_hits(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "source.md").write_text(
                "---\nstatus: accepted\n---\nThe source is available.\n",
                encoding="utf-8",
            )

            self.assertEqual(search_sources("what is the", root), [])


if __name__ == "__main__":
    unittest.main()
