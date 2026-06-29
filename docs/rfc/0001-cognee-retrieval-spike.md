# RFC 0001: Cognee Retrieval Spike

- Status: Rejected for now
- Date: 2026-06-29
- Owner: Founding AI Tech Lead

## Question

Can Cognee improve natural-language paraphrase retrieval while preserving Explain.fm's exact source provenance?

## Existing baseline

- Exact terminology: 5/5 cases.
- Paraphrase challenge: 0/4 cases.
- Retrieval output: accepted source path, line number, score, and source snippet.

The committed benchmarks are the comparison set. Do not rewrite queries to favor a candidate.

## Preconditions

- A supported local runtime or explicitly approved provider key.
- A pinned Cognee version and recorded model configuration.
- An isolated dataset containing only the two accepted Cognee source notes.
- No production database, cloud deployment, or listener data.

The project Codex setting (`gpt-5.5`, medium reasoning) controls the engineering agent only; it is not an Explain.fm runtime model route.

## Procedure

1. Ingest the accepted source-note bodies with source path and line metadata.
2. Run both committed retrieval benchmarks unchanged.
3. Record returned evidence, latency, configuration, and any lost provenance.
4. Delete the spike dataset and verify removal.
5. Compare results with `evaluation/metrics/lexical-baseline.md`.

## Acceptance criteria

- Exact terminology remains 5/5.
- Paraphrase retrieval reaches at least 3/4.
- Every returned claim resolves to a non-empty line in an accepted source note.
- No result cites frontmatter, rejected material, or generated text as evidence.
- Dataset deletion is verifiable.
- Setup and maintenance cost are documented.

## Rejection criteria

Reject or defer Cognee if provenance is lost, deletion cannot be verified, paraphrase recall remains below 3/4, or operational complexity is unjustified for the measured improvement.

## Outcome

The local smoke test completed `remember`, `recall`, and `forget`, but recall reduced cited evidence to generated text without its source path and line. Structured-output retries also made the two-item run take about 204 seconds. This fails the provenance and operational-cost criteria, so Cognee is not adopted. See [`evaluation/metrics/cognee-local-smoke.md`](../../evaluation/metrics/cognee-local-smoke.md).

## Non-goals

This spike does not select a production database, build a Research Agent, generate stories, or approve Cognee as an architecture dependency.
