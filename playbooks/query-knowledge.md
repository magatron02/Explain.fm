# Playbook: Query Knowledge

1. Start at `knowledge/index.md` and identify relevant reviewed topics and source notes.
2. For a reviewed topic, build its complete accepted-claim context with `packages/research/evidence_pack.py --topic "Topic Name"`.
3. Use `packages/research/search.py` only to narrow or inspect accepted sources; follow relevant `[[wikilinks]]`.
4. Use question-mode `packages/research/evidence_pack.py` when an exact lexical evidence subset is sufficient.
5. Consult `knowledge/raw/` only when reviewed material cannot answer the question.
6. Separate supported facts, interpretation, disagreement, and missing evidence.
7. Save valuable synthesis only as a reviewed research brief; never silently write generated answers back as established knowledge.

Return an explicit evidence gap when the vault cannot support an answer.
