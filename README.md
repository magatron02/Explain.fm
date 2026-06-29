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

Validate a research brief and every cited source line:

```bash
python packages/research/brief.py docs/research/cognee-evaluation-brief.md
```

## License

This repository is available under the existing [MIT License](LICENSE).
