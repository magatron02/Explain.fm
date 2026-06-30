# Explain.fm

**Where knowledge becomes conversation.**

Explain.fm is an AI-native Knowledge Storytelling Platform. It transforms trusted knowledge sources into accurate, natural, podcast-style conversations for people learning while working, driving, walking, or exercising.

It is not a generic AI podcast generator, summarizer, or chatbot. The product exists to create better explanations: grounded in evidence, structured as stories, and designed to be remembered.

## Repository status

Era 2 — Story is active. Era 1 passed its bounded knowledge exit review without adopting a retrieval dependency; the reviewed DNS slice is the first grounded story input. Broader application and infrastructure choices remain deferred until a tested slice proves them necessary.

Start with [BOOT.md](BOOT.md). Active delivery priorities live in [ROADMAP.md](ROADMAP.md); speculative ideas belong in [VISION_ROADMAP.md](VISION_ROADMAP.md).

Validate a populated source note with:

```bash
python packages/core/source_note.py knowledge/obsidian/inbox/example.md
```

Search accepted sources with line-level provenance:

```bash
python packages/research/search.py "provenance graph"
```

Build an evidence-only handoff for research:

```bash
python packages/research/evidence_pack.py "How does Cognee preserve provenance?"
python packages/research/evidence_pack.py --topic "DNS Resolution"
```

Validate a research brief and every cited source line:

```bash
python packages/research/brief.py docs/research/cognee-evaluation-brief.md
python packages/research/brief.py docs/research/dns-resolution-brief.md
```

Validate the first grounded story artifacts:

```bash
python packages/story/validate.py docs/design/dns-resolution-story-plan.md
python packages/story/validate.py evaluation/golden-episodes/dns-resolution-script.md
python packages/voice/validate.py evaluation/golden-episodes/dns-resolution-v1.manifest.json
```

Run the retrieval citation benchmark:

```bash
python packages/evaluation/retrieval.py
python packages/evaluation/retrieval.py evaluation/benchmarks/cognee-paraphrase-challenge.json
```

Run the complete local quality gate:

```bash
python -m unittest discover -s tests -v
```

The rejected Cognee experiment is recorded in [RFC 0001](docs/rfc/0001-cognee-retrieval-spike.md). Cognee is not an adopted runtime dependency.

Check Obsidian knowledge links directly:

```bash
python packages/core/wiki_links.py
```

## License

This repository is available under the existing [MIT License](LICENSE).
