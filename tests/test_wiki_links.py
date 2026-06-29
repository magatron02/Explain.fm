import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "packages" / "core"))

from wiki_links import validate_knowledge_links


class WikiLinkTests(unittest.TestCase):
    def test_valid_link_resolves_by_note_name(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            knowledge = root / "knowledge"
            knowledge.mkdir()
            (knowledge / "Source.md").write_text("[[Topic]]\n", encoding="utf-8")
            (knowledge / "Topic.md").write_text("# Topic\n", encoding="utf-8")
            self.assertEqual(validate_knowledge_links(root), [])

    def test_missing_link_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            knowledge = root / "knowledge"
            knowledge.mkdir()
            (knowledge / "Source.md").write_text("[[Missing]]\n", encoding="utf-8")
            self.assertTrue(any("missing link" in error for error in validate_knowledge_links(root)))

    def test_ambiguous_link_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            knowledge = root / "knowledge"
            (knowledge / "one").mkdir(parents=True)
            (knowledge / "two").mkdir()
            (knowledge / "Source.md").write_text("[[Topic]]\n", encoding="utf-8")
            (knowledge / "one" / "Topic.md").write_text("one\n", encoding="utf-8")
            (knowledge / "two" / "Topic.md").write_text("two\n", encoding="utf-8")
            self.assertTrue(any("ambiguous link" in error for error in validate_knowledge_links(root)))


if __name__ == "__main__":
    unittest.main()
