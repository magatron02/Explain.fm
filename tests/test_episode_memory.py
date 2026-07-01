import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))

from packages.memory.validate import text_sha256, validate_episode_memory

MEMORY = ROOT / "memory" / "episodes" / "dns-resolution-v1.md"


class EpisodeMemoryTests(unittest.TestCase):
    def test_all_episode_memories_are_valid(self):
        memories = list((ROOT / "memory" / "episodes").glob("*.md"))
        self.assertTrue(memories)
        for memory in memories:
            with self.subTest(memory=memory):
                self.assertEqual(validate_episode_memory(memory.read_text(encoding="utf-8"), ROOT), [])

    def test_memory_cannot_claim_evidence_authority(self):
        text = MEMORY.read_text(encoding="utf-8").replace("evidence_role: context-only", "evidence_role: evidence")
        self.assertIn("evidence_role must be context-only", validate_episode_memory(text, ROOT))

    def test_invalid_provenance_line_fails(self):
        text = MEMORY.read_text(encoding="utf-8").replace("dns-resolution-script.md:6", "dns-resolution-script.md:9999")
        self.assertIn(
            "invalid provenance line: evaluation/golden-episodes/dns-resolution-script.md:9999",
            validate_episode_memory(text, ROOT),
        )

    def test_changed_episode_fails_hash_check(self):
        text = MEMORY.read_text(encoding="utf-8").replace(
            "d4b19716947a8ebb1aa53b0820a213eab53db22342014cc8fa16a7699573f722",
            "0" * 64,
        )
        self.assertIn("episode_sha256 does not match episode", validate_episode_memory(text, ROOT))

    def test_text_hash_ignores_platform_newlines(self):
        with tempfile.TemporaryDirectory() as directory:
            lf = Path(directory) / "lf.txt"
            crlf = Path(directory) / "crlf.txt"
            lf.write_bytes(b"one\ntwo\n")
            crlf.write_bytes(b"one\r\ntwo\r\n")
            self.assertEqual(text_sha256(lf), text_sha256(crlf))

    def test_superseded_memory_requires_replacement(self):
        text = MEMORY.read_text(encoding="utf-8").replace("status: active", "status: superseded")
        self.assertIn(
            "superseded memory requires an existing superseded_by file",
            validate_episode_memory(text, ROOT),
        )


if __name__ == "__main__":
    unittest.main()
