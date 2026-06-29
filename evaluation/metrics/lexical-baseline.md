# Lexical Retrieval Baseline

Measured on 2026-06-29 against the first two accepted Cognee source notes.

| Benchmark | Result | Meaning |
| --- | --- | --- |
| Exact terminology | 5/5 | Finds source lines when the query shares source vocabulary. |
| Paraphrase challenge | 0/4 | Does not reliably connect a natural-language question to differently worded evidence. |

The linear lexical search is useful as a transparent citation baseline, not as the final retrieval system. A semantic or graph-based candidate must improve paraphrase recall while preserving exact `file:line` provenance.
