# DNS Memory Planning Result v1

- Date: 2026-07-01
- Experiment: `evaluation/experiments/dns-ttl-followup-ab-v1.md`
- Result: Candidate B accepted; duplicate episode rejected

## Measured consequence

The control plan proposed nine story beats. Review against the passed DNS script found substantial prior coverage for 9/9 beats. With episode memory, the planner detected that overlap, rejected the scope, retained accepted-source boundaries, and did not invent an unsupported replacement episode.

| Measure | Control | Memory-aware |
| --- | ---: | ---: |
| Proposed beats substantially repeating prior coverage | 9/9 | 0 shipped |
| Prior-coverage boundary available | No | Yes |
| Memory used as factual evidence | No | No |
| Unsupported replacement scope invented | No | No |

## Product effect

For this case, memory improved continuity and explanation planning by preventing a second episode from reteaching the same mental model. This supports listener understanding and maintainability without increasing feature or episode count.

## Limits

This is one topic with one prior episode and a technical-lead decision, not a blinded listener study. It does not prove retention gains, multi-episode retrieval quality, or scaling. Those claims remain out of scope until more real episodes exist.
