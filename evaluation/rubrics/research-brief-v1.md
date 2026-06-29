# Research Brief Rubric v1

Use this rubric after automated validation. Do not average away a failed trust gate.

## Automated gates

- Every cited file exists under `knowledge/obsidian/sources/`.
- Every cited source has `status: accepted`.
- Every cited line exists and is non-empty.
- Repository retrieval benchmarks match their recorded baselines.

Any automated-gate failure rejects the brief.

## Review criteria

Mark each criterion `Pass` or `Revise` and record evidence.

| Criterion | Pass condition |
| --- | --- |
| Claim support | Each material claim is no broader than its cited evidence. |
| Source quality | Authority, independence, currency, and usage limits are represented accurately. |
| Uncertainty | Disagreement, missing evidence, and unverified capability remain visible. |
| Scope | The brief answers its declared question without drifting into unsupported decisions. |
| Usefulness | A downstream planner can act without repeating source discovery or mistaking inference for fact. |

`Claim support`, `Source quality`, and `Uncertainty` are trust gates. Any `Revise` result on those criteria rejects the brief until corrected.

## Decision

- **Accepted:** all criteria pass.
- **Revise:** at least one criterion fails, with an owning correction recorded.
- **Blocked:** required evidence does not exist or cannot be used responsibly.
