# DNS Memory Continuity Benchmark v1

- Date: 2026-06-30
- Result: Context availability improved; Era 3 exit not met
- Benchmark: `evaluation/benchmarks/dns-memory-continuity.json`

## Question

Does an attributable episode-memory record give a later planner useful continuity context that source research alone does not contain?

## Conditions

- **Control:** the reviewed DNS research brief only.
- **Memory:** the same research brief plus the top active episode memory returned for `DNS resolution`.
- Both conditions use identical five exact-text checks covering prior mental model, introduced concepts, coverage boundaries, evaluation history, and the trust boundary.

## Result

| Condition | Passed | Change |
| --- | ---: | ---: |
| Control | 0/5 | — |
| Memory | 5/5 | +5 cases |

Run with:

```powershell
.\.venv\Scripts\python.exe packages\evaluation\continuity.py evaluation\benchmarks\dns-memory-continuity.json
```

## Interpretation

The research brief contains factual DNS evidence but does not record what the listener already heard, what nearby topics remain uncovered, or whether the prior episode passed. The episode-memory record supplies all five continuity signals while declaring itself `context-only` and retaining exact repository provenance.

This result shows that typed Markdown memory can make continuity context available at the current one-episode scale. It does not yet show that a memory-aware story plan is clearer, that a final episode improves understanding or retention, or that lexical scanning will scale.

## Decision

Keep the flat Markdown record and linear scan for the next paired story-planning experiment. Do not add Cognee, a vector database, a graph database, embeddings, or a reranker from this result. Reconsider indexing only after measured corpus size or retrieval failures justify it.
