# Local Semantic Retrieval Baseline

- Date: 2026-06-29
- Status: Accepted as an Era 1 prototype baseline
- Corpus: four accepted source notes
- Runtime: Ollama 0.30.11
- Model: `nomic-embed-text:latest` (768 dimensions)
- Storage: in-memory only

## Results

| Benchmark | Recall | Top-1 | MRR | Warm elapsed time |
| --- | --- | --- | --- | --- |
| Exact citation | 9/9 | 9/9 | 1.000 | 1.001 seconds |
| Paraphrase challenge | 15/18 | 10/18 | 0.659 | 1.478 seconds |

Every result retained its accepted source path, exact line number, and original source line. Documents use the model's `search_document:` prefix; queries use `search_query:`. The document title is included as retrieval context but is never returned as evidence.

## Decision

Use direct local semantic retrieval as the current comparison baseline. It closes the measured paraphrase gap without a vector database, generation model, or new Python dependency.

This is not a production selection. The corpus and 27 benchmark cases are small, English-only, and manually curated. Twelve paraphrase cases were added from previously uncovered accepted claims before running the expanded benchmark; their results were retained without tuning. Reassess indexing and storage only after corpus growth creates a measured latency or memory problem.

Do not add a reranker yet. The expanded set reduced paraphrase recall from 6/6 to 15/18 and exposed ambiguous but relevant alternatives. Independently review relevance judgments before optimizing ranking against these cases.
