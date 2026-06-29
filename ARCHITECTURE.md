# Architecture

## Conceptual pipeline

`Knowledge Sources → Collection → Cleaning → Obsidian Vault → Cognee Knowledge Graph → Research Agent → Story Planner → Script Generator → Voice (VoxCPM) → Evaluation → Podcast Episode`

## Stage boundaries

- **Knowledge Sources:** trusted origin material with provenance and usage constraints.
- **Collection:** acquisition without interpretation or loss of provenance.
- **Cleaning:** removal of noise while preserving meaning and traceability.
- **Obsidian Vault:** human-readable curated knowledge workspace.
- **Cognee Knowledge Graph:** concepts, relationships, and recall across material.
- **Research Agent:** evidence-grounded synthesis with explicit uncertainty.
- **Story Planner:** explanatory arc, teaching sequence, and episode intent.
- **Script Generator:** natural conversation grounded in the approved plan and evidence.
- **Voice (VoxCPM):** speech rendering without changing factual meaning.
- **Evaluation:** quality gate and feedback for every upstream stage before publication.
- **Podcast Episode:** packaged listener experience with source attribution after evaluation passes.

Each stage must expose its inputs and outputs rather than absorbing neighboring responsibilities. Retrieval, reasoning, storytelling, voice, and evaluation remain separable so they can be tested independently.

## Current status

This is a conceptual architecture, not a commitment to a framework, deployment model, or implementation language. Component names identify intended capabilities and may require an ADR before adoption.
