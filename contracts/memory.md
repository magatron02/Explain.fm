# Memory Contract

## Purpose

Define how approved knowledge and listener context enter and leave memory.

## Accepts

Concepts, relationships, insights, mental models, listener preferences, episode history, or feedback that complies with `MEMORY_POLICY.md` and includes provenance.

## Produces

Stored-item references or retrieved context with type, provenance, confidence, scope, version, and listener boundary where applicable.

## Invariants

- Prohibited source noise is not stored.
- Uncertain inference is never returned as established fact.
- Listener-specific information is isolated and removable.
- Corrections and superseded knowledge remain auditable.

## Failure behavior

Reject invalid, unattributed, prohibited, or unauthorized material explicitly. Retrieval must report uncertainty or absence rather than inventing context.

Storage technology and schema are intentionally unspecified.
