# Voice Contract

## Purpose

Define the boundary between an approved script and generated audio.

## Inputs

Versioned speaker turns, speaker definitions, pronunciation guidance, pacing direction, and rendering constraints.

## Outputs

Audio artifacts plus script version, voice configuration, timing metadata, warnings, and generation status.

## Dependencies

An approved script, validated speaker definitions, pronunciation guidance, voice capability, audio storage, and listenability evaluation.

## Success criteria

The complete audio is intelligible, speaker-consistent, traceable to its script and configuration, and preserves the approved meaning without undeclared transformations.

## Invariants

- Voice rendering preserves the approved factual meaning.
- Speakers remain identifiable and consistent.
- Material text transformations are declared.
- Output can be traced to the exact script and configuration.

## Failure behavior

Return explicit failure or partial status for missing, clipped, corrupted, or noncompliant audio. Never present partial generation as a complete episode.

Audio format, provider API, and transport are intentionally unspecified.
