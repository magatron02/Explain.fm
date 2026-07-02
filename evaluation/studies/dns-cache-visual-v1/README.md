# DNS Cache Visual Personalization Study v1

- Status: Ready for recruitment; no participant data collected
- Rubric: `evaluation/rubrics/listener-comprehension-v1.md`
- Topic: DNS cache reuse and TTL
- Explicit preference under test: “I prefer explanations that use a concrete visual analogy.”

## Research question

For listeners who explicitly choose a visual analogy, does the analogy improve learning gain without reducing delayed recall or factual accuracy?

## Conditions

- **Packet X — control:** plain-language sequence without an analogy.
- **Packet Y — personalized:** the same claims and sequence using a Post-it-note analogy.

Both packets teach exactly three targets: cached answers may be reused before TTL expiry, the information source should be consulted after expiry, and TTL is a reuse boundary rather than proof of correctness.

## Recruitment and assignment

1. Recruit at least eight consenting Thai readers who have not reviewed Explain.fm DNS material.
2. Include only listeners who explicitly select the visual-analogy preference before assignment.
3. Use shuffled sealed labels with four X and four Y assignments. For larger cohorts, keep condition sizes within one participant.
4. Keep the participant-to-study-ID mapping outside the repository and delete it after follow-up or withdrawal.
5. Do not replace withdrawals after opening their assignment. Report missing data.

## Run order

1. Read the consent script in `facilitator.md` and record consent outside the repository.
2. Ask the three pre-test prompts without showing either packet.
3. Give the assigned packet once, with a two-minute limit and no external lookup.
4. Remove the packet and ask the three post-test prompts.
5. Ask the two delayed-recall prompts 24–72 hours later without replay or rereading.
6. Give anonymized responses to a scorer who cannot see X/Y assignment.
7. Commit only the aggregate table and decision. Never commit responses or identity mappings.

Enter the aggregate table as JSON with `control` and `personalized` objects. Each object requires `assigned`, `completed_immediate`, `completed_delayed`, `withdrawn`, `median_gain`, `median_delayed`, `artifact_factual_errors`, `preference_responses`, and `preference_followed`. Then run:

```powershell
.\.venv\Scripts\python.exe packages\evaluation\listener_study.py <aggregate-results.json>
```

The input file remains outside the repository. The command returns `pass`, `fail`, or `inconclusive` using the pre-registered rubric thresholds.

## Stop conditions

- Stop if either packet contains a factual error, participants see both packets, assignment is not random, or the scorer learns condition labels before scoring.
- Mark the result inconclusive if fewer than four listeners complete each condition.
- Do not produce personalized audio until the text study passes.
