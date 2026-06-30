import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))

from packages.memory.validate import validate_episode_memory

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


if __name__ == "__main__":
    unittest.main()
