# Architecture

## Conceptual pipeline

`Sources → Collection → Cleaning → Obsidian Vault → Cognee Memory / Knowledge Graph → Research Agent → Story Planner → Script Generator → VoxCPM Voice → Audio Episode → Evaluation`

## Stage boundaries

- **Sources:** trusted origin material with provenance and usage constraints.
- **Collection:** acquisition without interpretation or loss of provenance.
- **Cleaning:** removal of noise while preserving meaning and traceability.
- **Obsidian Vault:** human-readable curated knowledge workspace.
- **Cognee Memory / Knowledge Graph:** concepts, relationships, and recall across material; Cognee remains unadopted after RFC 0001 and requires new evidence before reconsideration.
- **Research Agent:** evidence-grounded synthesis with explicit uncertainty.
- **Story Planner:** explanatory arc, teaching sequence, and episode intent.
- **Script Generator:** natural conversation grounded in the approved plan and evidence.
- **VoxCPM Voice:** speech rendering without changing factual meaning.
- **Audio Episode:** packaged listener artifact with source attribution, pending evaluation.
- **Evaluation:** quality gate and feedback for every upstream stage before publication.

Each stage must expose its inputs and outputs rather than absorbing neighboring responsibilities. Retrieval, reasoning, storytelling, voice, and evaluation remain separable so they can be tested independently.

## Current status

This is a conceptual architecture, not a commitment to a framework, deployment model, or implementation language. Component names identify intended capabilities and may require an ADR before adoption.
