# Research Contract

## Purpose

Define the boundary between knowledge retrieval and downstream story planning.

## Inputs

A bounded topic, audience context, approved source set or discovery constraints, and relevant attributable memory.

## Outputs

A research brief containing scope, key concepts, material claims, claim-level evidence references, source assessments, disagreements, uncertainty, and open questions.

## Dependencies

Trusted source access, cleaned source material, provenance metadata, the research guide, and relevant attributable memory.

## Success criteria

The brief is complete for its declared scope, every material claim is supported, source limitations are visible, and a story planner can use it without repeating source discovery.

## Invariants

- Every material factual claim is traceable to evidence.
- Facts, interpretations, and opinions are distinguishable.
- Source provenance survives the handoff.
- Missing evidence and conflicting sources remain visible.

## Failure behavior

Return an explicit incomplete or blocked result when source support is inadequate. Never fill evidence gaps with plausible text.

Implementation format and transport are intentionally unspecified.
