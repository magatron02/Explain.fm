import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from packages.research.evidence_pack import build_evidence_pack


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


if __name__ == "__main__":
    unittest.main()
