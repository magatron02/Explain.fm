# DNS Lexical Retrieval Baseline

- Date: 2026-06-29
- Corpus slice: three accepted RFC source notes
- Retrieval: dependency-free lexical baseline
- Benchmark policy: cases were authored before the first measurement and retained unchanged

## Results

| Benchmark | Recall | Top-1 | MRR |
| --- | --- | --- | --- |
| Exact terminology | 11/11 | 11/11 | 1.000 |
| Paraphrase challenge | 5/10 | 0/10 | 0.183 |

## Interpretation

The baseline preserves exact accepted-source paths and lines and is reliable when a query shares source vocabulary. It is not reliable enough for natural listener questions: half of the paraphrases miss the expected citation entirely, and none rank it first.

Do not tune synonyms or query wording against this small set. Keep it as the transparent comparison baseline for a future provider-neutral retrieval candidate.
