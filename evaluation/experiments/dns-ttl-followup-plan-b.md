# DNS TTL Follow-up — Candidate B

- Status: Experimental memory-aware output
- Planning inputs: `docs/research/dns-resolution-brief.md`, `memory/episodes/dns-resolution-v1.md`
- Request: Plan a follow-up episode explaining why a resolver cannot keep cached DNS answers forever.

## Decision

Do not build this follow-up as scoped.

## Reason

The passed DNS episode already introduced cache and TTL, taught that reuse is bounded rather than permanent, and ended with the same distinction this request proposes to explain. The episode memory records those concepts as already introduced (`memory/episodes/dns-resolution-v1.md:18`, `memory/episodes/dns-resolution-v1.md:21`, `memory/episodes/dns-resolution-v1.md:28`) and traces them to the reviewed script (`memory/episodes/dns-resolution-v1.md:43`, `memory/episodes/dns-resolution-v1.md:44`).

Candidate A repeats the prior episode's problem, example, misconception, recap, and takeaway. Repackaging those beats would add an episode without adding a better mental model.

## Trust boundary

The memory record establishes prior coverage only; it is not factual authority (`memory/episodes/dns-resolution-v1.md:14`). The underlying cache and TTL claims remain grounded in accepted sources:

- Cache may answer first: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`
- TTL limits reuse: `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`

## Safe next move

Research one adjacent thread that the memory explicitly marks as not previously covered—such as negative caching, DNSSEC, or transport behavior—then plan only if authoritative evidence supports a genuinely new listener outcome (`memory/episodes/dns-resolution-v1.md:33`). Do not imply prior listener knowledge of any unrecorded topic.

No replacement episode outline is invented before that evidence exists.
