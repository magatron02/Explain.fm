# DNS TTL Follow-up — Candidate A

- Status: Experimental control output
- Planning input: `docs/research/dns-resolution-brief.md`
- Request: Plan a follow-up episode explaining why a resolver cannot keep cached DNS answers forever.

## Decision

Build the follow-up as a focused explanation of cache reuse and TTL.

## Proposed arc

1. **Hook:** A repeated lookup feels instant, so why not keep every answer forever?
2. **Motivation:** Reuse saves work, but an unlimited cache could retain old data indefinitely.
3. **Problem:** Separate “still reusable” from “guaranteed true.”
4. **Explanation:** A resolver may answer from cache before asking an authoritative server; TTL bounds how long that cached record may be reused.
5. **Example:** Contrast a first lookup, a repeated lookup inside the TTL window, and a lookup after the reuse window ends.
6. **Comparison:** TTL is a reuse boundary, not proof that the underlying claim is correct.
7. **Common mistake:** A record that has not reached its TTL is guaranteed to reflect current reality.
8. **Recap:** Cache saves a journey; TTL prevents reuse from becoming permanent.
9. **Takeaway:** DNS speed comes from bounded memory, not permanent answers.

## Evidence boundary

- Cache may answer first: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`
- TTL limits reuse: `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`

This plan is factually grounded, but the control condition has no episode-history context and cannot assess whether the listener already received this explanation.
