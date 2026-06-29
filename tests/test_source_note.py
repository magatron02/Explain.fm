import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "packages" / "core"))

from source_note import REVIEW_ITEMS, validate_source_note


def source_note(status: str = "inbox", accessed: str = "2026-06-29") -> str:
    checks = "\n".join(f"- [ ] {item}" for item in REVIEW_ITEMS)
    return f'''---
type: source
status: {status}
title: "Primary source"
source_url: "https://example.com/source"
source_type: "documentation"
accessed: "{accessed}"
authority: "official"
license: "all-rights-reserved"
usage_rights: "quotation with attribution"
---

## Why this source matters
## Scope
## Key claims and evidence
| Claim | Evidence or location | Confidence |
| --- | --- | --- |
| Supported fact. | Official section | High |
## Limitations and uncertainty
## Raw artifact
## Derived notes
## Review
{checks}
'''


class SourceNoteValidationTests(unittest.TestCase):
    def test_valid_inbox_note(self):
        self.assertEqual(validate_source_note(source_note()), [])

    def test_missing_provenance_fails(self):
        errors = validate_source_note(source_note().replace('source_url: "https://example.com/source"', 'source_url: ""'))
        self.assertIn("source_url is required", errors)

    def test_unresolved_template_date_fails(self):
        errors = validate_source_note(source_note(accessed="{{date:YYYY-MM-DD}}"))
        self.assertIn("accessed is required", errors)

    def test_impossible_date_fails(self):
        errors = validate_source_note(source_note(accessed="2026-02-30"))
        self.assertIn("accessed must be a real date in YYYY-MM-DD format", errors)

    def test_source_url_requires_supported_scheme(self):
        note = source_note().replace("https://example.com/source", "example.com/source")
        self.assertIn("source_url must use https, http, or file", validate_source_note(note))

    def test_accepted_note_requires_completed_review(self):
        errors = validate_source_note(source_note(status="accepted"))
        self.assertEqual(len([error for error in errors if "incomplete review" in error]), len(REVIEW_ITEMS))

    def test_accepted_note_with_completed_review_is_valid(self):
        note = source_note(status="accepted").replace("- [ ]", "- [x]")
        self.assertEqual(validate_source_note(note), [])


if __name__ == "__main__":
    unittest.main()
