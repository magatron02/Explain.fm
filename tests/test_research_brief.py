import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "packages" / "research"))

from brief import validate_research_brief


def brief(citation: str) -> str:
    return f'''---
type: research-brief
status: draft
question: "What is supported?"
audience: "Explain.fm team"
---

## Findings

| Claim | Evidence | Source quality | Uncertainty |
| --- | --- | --- | --- |
| A supported claim. | `{citation}` | Primary | None noted |

## Disagreements and uncertainty

None.

## Open questions

None.
'''


class ResearchBriefTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.sources = self.root / "knowledge" / "obsidian" / "sources"
        self.sources.mkdir(parents=True)

    def tearDown(self):
        self.temporary.cleanup()

    def write_source(self, status: str = "accepted") -> str:
        relative = "knowledge/obsidian/sources/source.md"
        (self.root / relative).write_text(f"---\nstatus: {status}\n---\nEvidence line.\n", encoding="utf-8")
        return relative

    def test_valid_claim_level_citation(self):
        source = self.write_source()
        self.assertEqual(validate_research_brief(brief(f"{source}:4"), self.root), [])

    def test_missing_source_fails(self):
        errors = validate_research_brief(brief("knowledge/obsidian/sources/missing.md:4"), self.root)
        self.assertTrue(any("missing source" in error for error in errors))

    def test_invalid_line_fails(self):
        source = self.write_source()
        errors = validate_research_brief(brief(f"{source}:99"), self.root)
        self.assertTrue(any("invalid line" in error for error in errors))

    def test_unaccepted_source_fails(self):
        source = self.write_source(status="inbox")
        errors = validate_research_brief(brief(f"{source}:4"), self.root)
        self.assertTrue(any("unaccepted source" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
