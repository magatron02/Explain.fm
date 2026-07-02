---
type: source
status: accepted
title: "Anthropic Building Effective Agents"
source_url: "https://www.anthropic.com/engineering/building-effective-agents"
source_type: "Official engineering article"
author: "Erik Schluntz and Barry Zhang"
publisher: "Anthropic"
published: "2024-12-19"
accessed: "2026-07-02"
authority: "Primary engineering guidance from an AI-agent developer"
license: "Copyright; no open-content license identified"
usage_rights: "Brief paraphrase and citation with link; no copied article body"
topics: [AI Agents]
tags: [source, ai-agents]
---

# Anthropic Building Effective Agents

## Why this source matters

Anthropic distinguishes fixed LLM workflows from agents that dynamically choose their own process and tool use.

## Scope

The article describes composable agentic-system patterns and when their extra cost and complexity are justified. It is engineering guidance, not a formal taxonomy.

## Key claims and evidence

| Claim | Evidence or location | Confidence |
| --- | --- | --- |
| A workflow follows predefined code paths, while an agent lets the model dynamically direct process and tool usage. | “What are agents?” section | High |
| An augmented language model may have retrieval, tools, and memory, but those capabilities alone do not require a fully autonomous agent. | “Building block: The augmented LLM” section | High |
| Agentic systems trade latency and cost for flexibility and task performance. | “When (and when not) to use agents” section | High |
| Fixed workflows are preferable for predictable tasks; agents fit work requiring flexible model-driven decisions. | “When (and when not) to use agents” section | High |
| Start with the simplest design and add agent complexity only when outcomes justify it. | “Summary” section | High |

## Limitations and uncertainty

The recommendations come from Anthropic's deployments and customer experience. Terms remain contested, and the article does not establish one industry-wide autonomy threshold.

## Raw artifact

No page copy is stored. The source URL, publication date, and section names preserve provenance.

## Derived notes

- [[AI Agents]]
- [[ai-agents-brief]]

## Review

- [x] Provenance verified
- [x] Authority assessed
- [x] Usage rights recorded
- [x] Claims trace to evidence
- [x] Noise and duplication excluded
