import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))

from packages.voice.validate import validate_audio_manifest

MANIFEST = ROOT / "evaluation" / "golden-episodes" / "dns-resolution-v1.manifest.json"


class VoiceArtifactTests(unittest.TestCase):
    def test_dns_audio_manifest_matches_script_and_artifact(self):
        self.assertEqual(validate_audio_manifest(MANIFEST, ROOT, probe_audio=False), [])

    def test_changed_artifact_hash_fails(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        manifest["artifact_sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertIn("artifact SHA-256 does not match", validate_audio_manifest(path, ROOT, False))

    def test_undeclared_spoken_text_change_fails(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        manifest["turns"][0]["render_text"] += " changed"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertIn("turn 0 has an undeclared text transformation", validate_audio_manifest(path, ROOT, False))

    def test_passed_audio_requires_human_review(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        manifest.pop("human_review")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertIn("passed audio requires a dated human Pass review", validate_audio_manifest(path, ROOT, False))


if __name__ == "__main__":
    unittest.main()
