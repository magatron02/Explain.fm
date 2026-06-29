# Local Semantic Retrieval Baseline

- Date: 2026-06-29
- Status: Accepted as an Era 1 prototype baseline
- Corpus: four accepted source notes
- Runtime: Ollama 0.30.11
- Model: `nomic-embed-text:latest` (768 dimensions)
- Storage: in-memory only

## Results

| Benchmark | Result | Warm elapsed time |
| --- | --- | --- |
| Exact citation | 9/9 | 1.001 seconds |
| Paraphrase challenge | 6/6 | 1.042 seconds |

Every result retained its accepted source path, exact line number, and original source line. Documents use the model's `search_document:` prefix; queries use `search_query:`. The document title is included as retrieval context but is never returned as evidence.

## Decision

Use direct local semantic retrieval as the current comparison baseline. It closes the measured paraphrase gap without a vector database, generation model, or new Python dependency.

This is not a production selection. The corpus and 15 benchmark cases are small, English-only, and manually curated. Reassess indexing and storage only after corpus growth creates a measured latency or memory problem.
