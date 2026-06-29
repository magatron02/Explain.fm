---
type: topic
status: draft
title: "Cognee"
updated: "2026-06-29"
tags: [knowledge-infrastructure, candidate]
---

# Cognee

## Current understanding

Cognee is a candidate memory and knowledge-graph component for Explain.fm. Its official materials describe a system combining relational storage for documents and provenance, vector storage for semantic retrieval, and graph storage for entities and relationships.

The current public workflow centers on four operations: `remember`, `recall`, `improve`, and `forget`.

## Why it may fit Explain.fm

- Its documented storage separation resembles Explain.fm's need to preserve source provenance while connecting concepts.
- It offers a path from local defaults to replaceable storage backends.
- Its graph and retrieval responsibilities can remain downstream of source cleaning.

## What is not yet proven

- Claim-level citation fidelity across ingestion and retrieval.
- Retrieval quality on Explain.fm's intended knowledge corpus.
- Cost, latency, deletion behavior, and operational complexity.
- Whether Cognee improves listener understanding compared with a simpler indexed corpus.

Cognee remains a candidate, not an accepted architecture dependency. Adoption requires a bounded evaluation and ADR.

## Sources

- [[Cognee Official Repository]]
- [[Cognee Core Concepts Documentation]]
