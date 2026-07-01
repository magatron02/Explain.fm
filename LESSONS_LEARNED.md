# Lessons Learned

Record evidence-backed lessons from completed work. Do not use this file for predictions or general advice.

## Entry template

- **Date:**
- **Context:**
- **Observation:**
- **Evidence:**
- **Lesson:**
- **Resulting change:**

## Lessons

- **Date:** 2026-07-01
- **Context:** First Era 3 episode-memory and follow-up planning experiment.
- **Observation:** Source research alone exposed 0/5 continuity signals, while one attributable episode-memory record exposed 5/5. Without episode history, a follow-up plan repeated 9/9 prior teaching beats.
- **Evidence:** `evaluation/metrics/dns-memory-continuity-v1.md` and `evaluation/metrics/dns-memory-planning-v1.md`.
- **Lesson:** At the current scale, typed Markdown plus a linear scan is enough to improve planning; adding a graph, vector database, reranker, or embedding service would solve no measured problem.
- **Resulting change:** Reject the duplicate TTL follow-up, retain memory as `context-only`, and reconsider indexing only after real retrieval failures or corpus growth.

- **Date:** 2026-07-01
- **Context:** First Era 4 request-scoped Thai personalization experiments.
- **Observation:** The concise option passed audio preference review but failed two comprehension checks. A more detailed three-state explanation then failed both text checks before rendering.
- **Evidence:** `evaluation/metrics/thai-concise-personalization-v1.md` and `evaluation/metrics/thai-detailed-personalization-v1.md`.
- **Lesson:** Shorter output, fewer terms, better audio, and greater detail are not substitutes for measured understanding.
- **Resulting change:** Require a text comprehension pass before spending compute on personalized audio, and do not create a persistent listener profile from failed experiments.
