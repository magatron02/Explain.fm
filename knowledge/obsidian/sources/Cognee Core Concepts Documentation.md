---
type: source
status: accepted
title: "Cognee Core Concepts Documentation"
source_url: "https://docs.cognee.ai/core-concepts/overview"
source_type: "official documentation"
author: "Cognee documentation team"
publisher: "Cognee"
published: ""
accessed: "2026-06-29"
authority: "primary product documentation"
license: "not stated on source page"
usage_rights: "link and limited quotation with attribution; do not republish"
topics: [cognee, knowledge-graph, retrieval, provenance]
tags: [source]
---

# Cognee Core Concepts Documentation

## Why this source matters

The page describes Cognee's current storage roles and public operations. These boundaries are directly relevant to Explain.fm's need to keep provenance, semantic retrieval, and relationships inspectable.

## Scope

The core-concepts overview accessed on 2026-06-29. It describes architecture at a product level, not deployment guarantees or measured quality.

## Key claims and evidence

| Claim | Evidence or location | Confidence |
| --- | --- | --- |
| Cognee combines vector search with graph storage to support semantic search and connected relationships. | “Introduction” and “Architecture” | High for documented design |
| The relational store tracks documents, chunks, and provenance. | “Architecture” | High for documented responsibility |
| The vector store holds embeddings for semantic similarity. | “Architecture” | High for documented responsibility |
| The graph store captures entities and relationships. | “Architecture” | High for documented responsibility |
| Current main operations are `remember`, `recall`, `improve`, and `forget`. | “Main Operations” | High |

## Limitations and uncertainty

- This is first-party documentation, not an independent evaluation.
- The page does not prove that provenance survives every transformation or meets Explain.fm's citation contract.
- The page does not state a documentation-content license.

## Raw artifact

No local copy. Refer to the canonical URL and accessed date.

## Derived notes

- [[Cognee]]

## Review

- [x] Provenance verified
- [x] Authority assessed
- [x] Usage rights recorded
- [x] Claims trace to evidence
- [x] Noise and duplication excluded
