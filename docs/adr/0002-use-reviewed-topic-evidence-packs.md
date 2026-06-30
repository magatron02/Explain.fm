# ADR-0002: Use reviewed-topic evidence packs for bounded research

- Status: Accepted
- Date: 2026-06-30
- Deciders: Founder; Founding AI Tech Lead

## Context

The dependency-free lexical baseline preserves exact provenance but returns only 12 of 28 paraphrase targets. Thirteen of the sixteen misses have no token overlap with the expected evidence, so reranking cannot recover them. The Research Contract already requires a bounded topic and approved source set, and the current reviewed DNS topic contains only three accepted source notes.

## Decision

- Build a topic evidence pack from every accepted claim linked by a reviewed topic.
- Preserve each claim's exact source path and line in the handoff.
- Keep lexical search as a transparent navigation aid, not a listener-facing semantic interface.
- Do not add a reranker, synonym table, vector database, or model dependency for the current corpus.

## Consequences

The DNS Research Agent receives all 18 accepted claims, including every target in the DNS paraphrase benchmark, without trusting semantic ranking. Pack size grows linearly with a topic's approved evidence, so broad topics must be split before their context becomes hard to review.

## Alternatives considered

- Rerank lexical results: rejected because it cannot recover evidence absent from the candidate set.
- Tune synonyms against the benchmark: rejected because it would overfit the current questions.
- Add a local or hosted embedding route: deferred because no runtime route is approved, and the small reviewed corpus does not require one.

## Evidence and follow-up

- `evaluation/metrics/era-1-exit-review.md`
- `python packages/research/evidence_pack.py --topic "DNS Resolution"`
- Reconsider indexed or semantic retrieval only after measured topic-pack size, latency, or review quality becomes inadequate.
