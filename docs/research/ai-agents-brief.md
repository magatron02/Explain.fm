---
type: research-brief
status: reviewed
question: "What is an AI agent, how is it different from a chatbot or fixed workflow, and when is it useful?"
audience: "Thai general listeners learning while working"
created: "2026-07-02"
---

# AI Agents Brief

## Scope

This brief explains the smallest useful mental model of an AI agent: a model receives a goal, observes context, chooses and performs an action through tools, checks the result, and repeats or hands control back. It distinguishes agents from chatbots and fixed workflows. It does not claim human-like consciousness, guaranteed correctness, independent legal responsibility, or that every AI product needs autonomy.

## Findings

| Claim | Evidence | Source quality | Uncertainty |
| --- | --- | --- | --- |
| An agent pursues a user's goal by managing a multi-step workflow rather than only returning one response. | `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:32`<br>`knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:33` | Primary practitioner guidance from OpenAI | “Agent” has no single industry-wide autonomy threshold. |
| The practical core is a model making decisions under instructions and using tools to observe or act. | `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:34`<br>`knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:36` | Primary design guidance | Memory is useful in some systems but is not required for the minimal definition. |
| A fixed workflow follows code-selected paths; an agent dynamically chooses at least part of its process and tool use. | `knowledge/obsidian/sources/Anthropic Building Effective Agents.md:32` | Primary engineering guidance from Anthropic | Real products can combine fixed workflow sections with agentic sections. |
| Agentic systems cost more time and compute, so predictable tasks should remain deterministic when possible. | `knowledge/obsidian/sources/Anthropic Building Effective Agents.md:34`<br>`knowledge/obsidian/sources/Anthropic Building Effective Agents.md:35` | Direct deployment guidance | The break-even point depends on task ambiguity, failure cost, and model quality. |
| Autonomy must be bounded by guardrails, completion checks, error recovery, and human handoff. | `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:36` | Primary safety and reliability guidance | Specific controls depend on the tools and consequences involved. |
| Multiple agents and agent frameworks are optional complexity, not the starting definition. | `knowledge/obsidian/sources/Anthropic Building Effective Agents.md:36`<br>`knowledge/obsidian/sources/Anthropic Building Effective Agents.md:33` | Primary simplicity guidance | Some large tasks may later justify delegation or multiple specialists. |

## Disagreements and uncertainty

OpenAI frames agents around independent task completion and workflow control. Anthropic uses the broader term “agentic systems” but reserves “agent” for systems where the model dynamically controls its process. These views overlap on goal-directed decisions and tool use but do not establish a universal category boundary. The episode should describe a spectrum of autonomy rather than police the label.

## Open questions

- How much autonomy is acceptable when a tool can spend money, publish content, or delete data?
- Which actions should always require confirmation even if the agent is confident?
- When does adding memory improve continuity enough to justify privacy and staleness risks?

## Recommendation

Teach an agent as a loop, not a robot character: goal, observe, decide, act through a tool, inspect the result, then stop, retry, or ask a human. Contrast that loop with a chatbot's answer and a fixed workflow's predetermined route. End with the practical rule that autonomy is valuable only when flexibility outweighs extra cost and risk.
