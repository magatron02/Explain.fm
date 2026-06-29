---
type: topic
status: draft
title: "Obsidian Knowledge Organization"
updated: "2026-06-29"
tags: [knowledge-workspace, provenance]
---

# Obsidian Knowledge Organization

## Current understanding

Explain.fm uses Obsidian as the human-readable layer between cleaned sources and machine memory. Flat YAML properties carry compact ingest metadata, while internal links connect source notes to derived concepts and research artifacts.

## Working rules

- Keep properties atomic and flat so humans and the stdlib validator can read them.
- Keep factual evidence in accepted source notes with origin and usage metadata.
- Use links for navigation, not as a replacement for claim-level citations.
- Prefer portable repository paths for machine validation; use Obsidian links for human navigation.
- Treat block references as Obsidian-specific and avoid making core provenance depend on them.

## Sources

- [[Obsidian Properties Documentation]]
- [[Obsidian Internal Links Documentation]]
