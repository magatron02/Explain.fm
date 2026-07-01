# DNS TTL Follow-up Planning A/B v1

- Date: 2026-07-01
- Status: Complete; Candidate B accepted
- Context benchmark: `evaluation/metrics/dns-memory-continuity-v1.md`

## Question

Does episode memory improve the planning decision for a proposed follow-up, not merely make historical context retrievable?

## Setup

Both candidates receive the same request and reviewed DNS research brief. Candidate B additionally receives the validated `context-only` DNS episode memory. Neither candidate may use memory as factual evidence.

## Comparison

| Check | Candidate A | Candidate B |
| --- | --- | --- |
| Factual claims retain accepted-source citations | Yes | Yes |
| Detects overlap with prior listener coverage | No episode history available | Yes |
| Avoids repeating the prior mental model | No | Yes; rejects the scope |
| Respects uncovered-topic boundaries | Unknown | Yes |
| Invents unsupported new scope | No | No |

## Planning consequence

Every proposed Candidate A beat substantially repeats reviewed material:

| Candidate A beat | Prior episode coverage |
| --- | --- |
| Hook | Permanent reuse question: `evaluation/golden-episodes/dns-resolution-script.md:26` |
| Motivation | Speed and expiry from bounded reuse: `evaluation/golden-episodes/dns-resolution-script.md:28`, `evaluation/golden-episodes/dns-resolution-script.md:30` |
| Problem | TTL is not a truth guarantee: `evaluation/golden-episodes/dns-resolution-script.md:102`, `evaluation/golden-episodes/dns-resolution-script.md:104` |
| Explanation | Cache-first response and TTL boundary: `evaluation/golden-episodes/dns-resolution-script.md:72`, `evaluation/golden-episodes/dns-resolution-script.md:104` |
| Example | First journey versus cached reuse: `evaluation/golden-episodes/dns-resolution-script.md:68`, `evaluation/golden-episodes/dns-resolution-script.md:72` |
| Comparison | Reuse boundary versus proof: `evaluation/golden-episodes/dns-resolution-script.md:104` |
| Common mistake | Unexpired means guaranteed correct: `evaluation/golden-episodes/dns-resolution-script.md:102` |
| Recap | Reuse only within TTL: `evaluation/golden-episodes/dns-resolution-script.md:114` |
| Takeaway | Not a permanent answer: `evaluation/golden-episodes/dns-resolution-script.md:122`, `evaluation/golden-episodes/dns-resolution-script.md:124` |

Candidate A has 9/9 substantially repeated beats. Candidate B prevents all nine from becoming a redundant episode while retaining the source boundary for any future topic.

## Decision

The Founding AI Tech Lead accepts **Candidate B** under the repository product gate: the proposed episode does not add a new mental model and therefore should not be built. The user's instruction to continue to completion authorizes execution of the recommended default; it is not represented as a blind Founder preference vote.

## Interpretation boundary

The 9/9 review is a documented planning comparison, not a listener-retention experiment. It shows that memory improved this planning decision by detecting and preventing a wholly repeated explanation. It does not establish that every future repetition is harmful or that listener outcomes improved.
