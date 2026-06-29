# Blueprint 008: User Profile

## Goal

Represent listener preferences and learning context transparently so future personalization can improve explanations without stereotyping users.

## Responsibilities

- Store explicit preferences with source and consent context.
- Distinguish user-provided facts from tentative inferences.
- Support inspection, correction, export, and deletion.
- Supply only relevant context to downstream stages.

## Inputs

Explicit settings, consented feedback, episode history, and bounded evaluation signals.

## Outputs

A minimal listener context containing relevant preferences, provenance, confidence, and expiry where applicable.

## Dependencies

Memory policy, identity and privacy boundaries, episode history, and personalization evaluation.

## Failure Cases

Over-inference, stale preference use, sensitive profiling, filter bubbles, cross-user leakage, or personalization that reduces accuracy.

## Future Ideas

Listener-owned learning goals, portable profiles, preference expiry controls, and transparent adaptation explanations.
