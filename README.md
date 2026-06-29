# Explain.fm

**Where knowledge becomes conversation.**

Explain.fm is an AI-native Knowledge Storytelling Platform. It transforms trusted knowledge sources into accurate, natural, podcast-style conversations for people learning while working, driving, walking, or exercising.

It is not a generic AI podcast generator, summarizer, or chatbot. The product exists to create better explanations: grounded in evidence, structured as stories, and designed to be remembered.

## Repository status

Era 1 implementation has started with a dependency-free validator for Obsidian source notes. Broader application and infrastructure choices remain intentionally deferred until the knowledge slice proves them necessary.

Start with [BOOT.md](BOOT.md). Active delivery priorities live in [ROADMAP.md](ROADMAP.md); speculative ideas belong in [VISION_ROADMAP.md](VISION_ROADMAP.md).

Validate a populated source note with:

```bash
python packages/core/source_note.py knowledge/obsidian/inbox/example.md
```

Search accepted sources with line-level provenance:

```bash
python packages/research/search.py "provenance graph"
```

Search paraphrases through the local Ollama embedding route:

```bash
ollama pull nomic-embed-text
python packages/research/semantic_search.py "Where is note metadata physically written?"
python packages/evaluation/semantic_retrieval.py
```

The semantic benchmark is a local integration check and is not part of CI because it requires Ollama. Its recorded result is in [the local semantic baseline](evaluation/metrics/semantic-local-baseline.md).

Build an evidence-only handoff for research:

```bash
python packages/research/evidence_pack.py "How does Cognee preserve provenance?"
```

Validate a research brief and every cited source line:

```bash
python packages/research/brief.py docs/research/cognee-evaluation-brief.md
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

The rejected local Cognee experiment and its reproducible model route are recorded in [RFC 0001](docs/rfc/0001-cognee-retrieval-spike.md). Copy `.env.example` to `.env` only when reproducing that spike; Cognee is not an adopted runtime dependency.

Check Obsidian knowledge links directly:

```bash
python packages/core/wiki_links.py
```

## License

This repository is available under the existing [MIT License](LICENSE).
