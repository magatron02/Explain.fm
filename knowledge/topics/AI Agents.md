---
type: topic
status: reviewed
title: "AI Agents"
tags: [topic, ai-agents]
---

# AI Agents

An AI agent is a software system in which a model pursues a user-defined goal by choosing and executing steps, often through tools, while checking whether the task is complete or needs human intervention.

## Core distinction

A chatbot mainly answers a turn. A fixed workflow follows steps selected in advance by code. An agent receives a goal and dynamically chooses at least part of the route. These categories overlap in products, so autonomy is a spectrum rather than a badge.

## Minimal mental model

1. Receive a goal and constraints.
2. Observe relevant context.
3. Choose the next action.
4. Use a tool or produce an intermediate result.
5. Inspect the outcome and repeat, stop, or hand control back.

## Boundaries

Tools, memory, and multiple models can extend an agent but are not proof that a system needs to be agentic. More autonomy adds cost, latency, and risk; deterministic software remains preferable when the steps are stable.

## Sources

- [[OpenAI Practical Guide to Building AI Agents]]
- [[Anthropic Building Effective Agents]]

## Derived work

- [[ai-agents-brief]]
