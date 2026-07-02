# Playbook: Listener Personalization Study

1. Choose one grounded episode whose control artifact already passes research, story, and audio gates.
2. Collect one explicit, non-sensitive preference that changes presentation but not factual scope.
3. Produce one personalized artifact; preserve the same claims and citations as control.
4. Pre-register the three target concepts, equivalent pre/post prompts, delayed-recall prompts, and scoring examples before recruiting listeners.
5. Follow `evaluation/rubrics/listener-comprehension-v1.md`; randomize assignment and blind scoring.
6. Keep participant identity outside the repository. Commit only aggregated scores, missing-data counts, method, decision, and limitations.
7. Reject the adaptation if accuracy regresses, the comprehension gate fails, or the cohort is too small. Do not tune prompts after seeing answers.
8. Create a listener profile only after a separate explicit consent step. A study preference is request-scoped by default and expires with the study.

Do not spend compute on personalized audio until the text version preserves every factual claim and its pre-registered comprehension prompts are answerable by an independent reviewer.
