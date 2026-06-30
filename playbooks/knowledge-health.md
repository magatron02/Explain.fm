# Playbook: Knowledge Health

Run after ten accepted ingests, monthly, and before relying on the vault for a major research brief.

## Deterministic checks

```bash
python packages/core/wiki_links.py
python -m unittest discover -s tests -v
```

These checks cover broken or ambiguous wikilinks, index completeness, source-note validity, citation validity, and recorded retrieval baselines.

## Reviewed checks

- Look for conflicting claims across sources and keep both positions visible.
- Flag claims whose source date or authority is no longer adequate.
- Identify isolated notes, missing cross-references, and topics the vault cannot answer.
- Do not auto-fix contradictions or promote inbox material.

Append a concise result to `knowledge/log.md` only after the check is complete.
