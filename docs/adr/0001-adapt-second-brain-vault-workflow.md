# ADR-0001: Adapt second-brain workflow to the Explain.fm vault

- Status: Accepted
- Date: 2026-06-29
- Deciders: Founder; Founding AI Tech Lead

## Context

`NicholasSpisak/second-brain` demonstrates a useful LLM-maintained Obsidian pattern: raw inputs, curated pages, a master index, an operation log, query-first navigation, and periodic health checks. Explain.fm already has stricter source-note, provenance, citation, benchmark, and research-review boundaries.

The upstream repository has no root license file. Its implementation is therefore treated as design evidence, not code to copy.

## Decision

- Keep `ExplainFM_Project` as the single Obsidian vault.
- Preserve the existing `knowledge/raw`, source-note, topic, example, analogy, mental-model, and research-brief boundaries.
- Add `knowledge/index.md` as the reviewed entrypoint and `knowledge/log.md` as an append-only operation record.
- Query reviewed knowledge first and consult raw material only as a last resort.
- Extend deterministic health checks to cover index completeness in addition to link and provenance validation.
- Keep human review for contradictions, staleness, missing context, and promotion of new knowledge.

## Consequences

Agents gain a predictable entrypoint and handoff trail without creating a parallel `wiki/` tree. Index maintenance becomes part of source admission. Generated synthesis cannot silently become accepted knowledge.

## Alternatives considered

- Install the upstream skills directly: rejected because they assume a different schema and would weaken Explain.fm's evidence gates.
- Mirror `raw/wiki/output`: rejected because it duplicates existing repository boundaries.
- Add optional search and browser dependencies: deferred until corpus scale proves they are needed.

## Evidence and follow-up

- Source pattern: `https://github.com/NicholasSpisak/second-brain`
- Validate the adapted index and links in CI.
- Reassess search tooling only after measured corpus growth.
