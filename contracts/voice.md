# Voice Contract

## Purpose

Define the boundary between an approved script and generated audio.

## Accepts

Versioned speaker turns, speaker definitions, pronunciation guidance, pacing direction, and rendering constraints.

## Produces

Audio artifacts plus script version, voice configuration, timing metadata, warnings, and generation status.

## Invariants

- Voice rendering preserves the approved factual meaning.
- Speakers remain identifiable and consistent.
- Material text transformations are declared.
- Output can be traced to the exact script and configuration.

## Failure behavior

Return explicit failure or partial status for missing, clipped, corrupted, or noncompliant audio. Never present partial generation as a complete episode.

Audio format, provider API, and transport are intentionally unspecified.
