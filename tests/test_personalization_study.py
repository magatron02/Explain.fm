import re
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
STUDY = ROOT / "evaluation" / "studies" / "dns-cache-visual-v1"


class PersonalizationStudyTests(unittest.TestCase):
    def test_both_packets_preserve_the_same_learning_targets(self):
        required = ("ก่อน ทีทีแอล หมด", "เมื่อ ทีทีแอล หมด", "แหล่งข้อมูลอีกครั้ง", "ไม่ใช่", "ถูกต้องเสมอ")
        for name in ("packet-x.md", "packet-y.md"):
            text = (STUDY / name).read_text(encoding="utf-8")
            with self.subTest(packet=name):
                for phrase in required:
                    self.assertIn(phrase, text)

    def test_facilitator_source_references_resolve(self):
        text = (STUDY / "facilitator.md").read_text(encoding="utf-8")
        for relative, line_text in re.findall(r"`([^`\n]+):(\d+)`", text):
            target = (ROOT / relative).resolve()
            target.relative_to(ROOT.resolve())
            lines = target.read_text(encoding="utf-8").splitlines()
            line = int(line_text)
            self.assertTrue(1 <= line <= len(lines) and lines[line - 1].strip(), f"{relative}:{line}")


if __name__ == "__main__":
    unittest.main()
