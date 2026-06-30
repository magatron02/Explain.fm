import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from packages.research.evidence_pack import build_evidence_pack, build_topic_evidence_pack


class EvidencePackTests(unittest.TestCase):
    def test_pack_preserves_exact_source_location_and_text(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "knowledge" / "obsidian" / "sources" / "source.md"
            source.parent.mkdir(parents=True)
            source.write_text("---\nstatus: accepted\n---\nGraph evidence.\n", encoding="utf-8")

            pack = build_evidence_pack("graph", root)

            self.assertIn("`knowledge/obsidian/sources/source.md:4`", pack)
            self.assertIn("Graph evidence.", pack)
            self.assertIn("retrieved accepted-note text only", pack)

    def test_pack_reports_missing_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            pack = build_evidence_pack("unknown", Path(directory))
            self.assertIn("No accepted evidence found.", pack)

    def test_topic_pack_includes_every_linked_accepted_claim(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            topics = root / "knowledge" / "topics"
            sources = root / "knowledge" / "obsidian" / "sources"
            topics.mkdir(parents=True)
            sources.mkdir(parents=True)
            (topics / "Test Topic.md").write_text(
                "---\nstatus: reviewed\n---\n# Test Topic\n\n- [[Trusted Source]]\n",
                encoding="utf-8",
            )
            (sources / "Trusted Source.md").write_text(
                "---\nstatus: accepted\n---\n## Key claims and evidence\n"
                "| Claim | Evidence | Confidence |\n| --- | --- | --- |\n"
                "| Graph evidence. | Section 1 | High |\n",
                encoding="utf-8",
            )

            pack = build_topic_evidence_pack("Test Topic", root)

            self.assertIn("`knowledge/obsidian/sources/Trusted Source.md:7`", pack)
            self.assertIn("Graph evidence.", pack)

    def test_topic_pack_rejects_unreviewed_topic(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            topic = root / "knowledge" / "topics" / "Draft.md"
            topic.parent.mkdir(parents=True)
            topic.write_text("---\nstatus: draft\n---\n", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "not reviewed"):
                build_topic_evidence_pack("Draft", root)


if __name__ == "__main__":
    unittest.main()
