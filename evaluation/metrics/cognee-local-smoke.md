# Cognee Local Smoke Test

- Date: 2026-06-29
- Result: Rejected for now
- Cognee: 1.2.2
- Ollama: 0.30.11
- Generation model: `llama3.1:8b`
- Embedding model: `nomic-embed-text:latest` (768 dimensions)
- Hardware: 31.4 GB RAM, NVIDIA RTX 3060 Laptop GPU (4 GB)
- Reproduction dependency: `docs/rfc/cognee-local-requirements.txt`

## Checks

| Check | Result | Evidence |
| --- | --- | --- |
| Ollama embedding endpoint | Pass | Returned two 768-dimensional embeddings. |
| Ollama structured JSON | Pass | Returned the requested JSON object. |
| Cognee `remember` → `recall` → `forget` | Pass with warnings | Workflow completed in about 204 seconds; deletion command completed. |
| Exact source provenance after recall | Fail | Input citation `[source-a.md:33]` was absent; recall returned only generated text. |
| Structured-output reliability | Fail | The 8B model required repeated schema retries. |
| Runtime cleanup | Fail | Process exit reported unclosed HTTP client sessions. |

## Decision

Do not adopt Cognee for Explain.fm retrieval. The smoke test crossed the RFC rejection boundary because provenance was lost, and its latency and retry behavior are too costly for the measured result.

The next bounded experiment is direct semantic retrieval with the already-running local embedding model. It must return exact accepted-source paths and line numbers and run against the unchanged paraphrase benchmark.
