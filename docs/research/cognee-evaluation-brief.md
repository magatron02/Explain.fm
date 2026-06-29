---
type: research-brief
status: draft
question: "Is Cognee ready to become Explain.fm's knowledge-graph dependency?"
audience: "Explain.fm engineering and product"
created: "2026-06-29"
---

# Cognee Evaluation Brief

## Scope

This brief records what Cognee's official repository and core-concepts documentation support. It does not evaluate runtime behavior or accept Cognee as a dependency.

## Findings

| Claim | Evidence | Source quality | Uncertainty |
| --- | --- | --- | --- |
| Cognee documents distinct relational, vector, and graph storage responsibilities. | `knowledge/obsidian/sources/Cognee Core Concepts Documentation.md:33`<br>`knowledge/obsidian/sources/Cognee Core Concepts Documentation.md:34`<br>`knowledge/obsidian/sources/Cognee Core Concepts Documentation.md:35` | Primary product documentation | Architecture is documented but not locally verified. |
| Cognee's current public workflow centers on `remember`, `recall`, `improve`, and `forget`. | `knowledge/obsidian/sources/Cognee Core Concepts Documentation.md:36`<br>`knowledge/obsidian/sources/Cognee Official Repository.md:33` | Two first-party descriptions | Both sources belong to the same project and are not independent confirmation. |
| The repository is published under Apache-2.0. | `knowledge/obsidian/sources/Cognee Official Repository.md:35` | Primary repository metadata | Dependency and notice obligations still require implementation review. |
| Suitability for Explain.fm's citation contract has not been demonstrated. | `knowledge/obsidian/sources/Cognee Core Concepts Documentation.md:41`<br>`knowledge/obsidian/sources/Cognee Official Repository.md:40` | Explicit limitations in reviewed source notes | Requires a local evaluation corpus and retrieval test. |

## Disagreements and uncertainty

The official sources are consistent at this level, but they are not independent. No evidence yet shows that claim-level provenance survives ingestion, graph construction, and retrieval.

## Open questions

- Can retrieved claims be traced to the exact source passage after graph construction?
- Does Cognee outperform the linear lexical baseline on a small Explain.fm corpus?
- What are the minimum storage, model, latency, and deletion requirements?

## Recommendation

Do not adopt Cognee yet. Run a bounded spike against the current source corpus and compare citation fidelity with `packages/research/search.py` before writing an ADR.
