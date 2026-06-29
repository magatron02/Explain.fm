# Lexical Retrieval Baseline

Measured on 2026-06-29 against four accepted Cognee and Obsidian source notes.

| Benchmark | Recall | Top-1 | MRR | Meaning |
| --- | --- | --- | --- | --- |
| Exact terminology | 9/9 | 9/9 | 1.000 | Finds source lines when the query shares source vocabulary. |
| Paraphrase challenge | 7/18 | 4/18 | 0.306 | Shared vocabulary helps some cases, but differently worded evidence remains unreliable. |

The linear lexical search is useful as a transparent citation baseline, not as the final retrieval system. A semantic or graph-based candidate must improve paraphrase recall while preserving exact `file:line` provenance.
