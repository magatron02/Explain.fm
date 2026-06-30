import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))

from packages.story.validate import validate_story_artifact


class StoryArtifactTests(unittest.TestCase):
    def setUp(self):
        self.plan = (ROOT / "docs" / "design" / "dns-resolution-story-plan.md").read_text(encoding="utf-8")
        self.script = (
            ROOT / "evaluation" / "golden-episodes" / "dns-resolution-script.md"
        ).read_text(encoding="utf-8")

    def test_grounded_plan_and_script_are_valid(self):
        self.assertEqual(validate_story_artifact(self.plan, ROOT), [])
        self.assertEqual(validate_story_artifact(self.script, ROOT), [])

    def test_missing_required_beat_fails(self):
        broken = self.plan.replace("## Takeaway", "## Closing")
        self.assertIn("missing beat: Takeaway", validate_story_artifact(broken, ROOT))

    def test_invalid_source_line_fails(self):
        broken = self.plan.replace("DNS Terminology.md:32", "DNS Terminology.md:999", 1)
        self.assertTrue(any("invalid line" in error for error in validate_story_artifact(broken, ROOT)))

    def test_script_requires_two_speakers(self):
        broken = self.script.replace("**NARIN:**", "**MAYA:**")
        self.assertIn("episode script requires at least two speakers", validate_story_artifact(broken, ROOT))


if __name__ == "__main__":
    unittest.main()
