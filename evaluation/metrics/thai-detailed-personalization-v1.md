# Thai Detailed Personalization Result v1

- Date: 2026-07-01
- Experiment: `evaluation/personalization/thai-detailed-dns-v1.md`
- Result: Rejected before audio rendering

## Change tested

After the concise option failed its learning gate, the detailed option explained DNS caching as three explicit states: first lookup, reuse before TTL expiry, and consultation after TTL expiry. The preference remained request-scoped and no listener profile was created.

## Comprehension result

| Check | Expected | Response | Result |
| --- | --- | --- | --- |
| Before TTL expires | May reuse cached answer | Must ask again every time | Fail |
| After TTL expires | Consult information source again | Reuse old answer | Fail |

## Decision

Do not render or promote option B. Both tested adaptations failed to demonstrate improved understanding, so Era 4 remains active. The next experiment must change the teaching method or evaluation setup rather than adjusting length, jargon, voice, or detail again.
