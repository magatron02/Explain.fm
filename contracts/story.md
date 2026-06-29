# Story Contract

## Purpose

Define the handoff from grounded research to conversational script writing.

## Inputs

A valid research brief, episode objective, audience context, duration constraint, and applicable podcast guidelines.

## Outputs

A story plan containing the central question, intended listener change, ordered episode beats, concepts, evidence references, examples, comparisons, misconceptions, caveats, recap, and takeaway.

## Dependencies

A valid research brief, podcast guidelines, listener context, quality criteria, and the project constitution.

## Success criteria

The plan forms a coherent teaching sequence, includes every required episode beat, preserves evidence and uncertainty, and is specific enough for script writing without new factual invention.

## Invariants

- Every factual beat maps to research evidence.
- All required podcast elements are present or explicitly marked inapplicable with rationale.
- Narrative framing does not distort uncertainty or manufacture conflict.
- New factual needs are returned to research rather than invented.

## Failure behavior

Return a revision request identifying missing evidence, audience context, or structural gaps. Do not silently weaken constitutional or quality requirements.

Serialization and implementation are intentionally unspecified.
