---
type: story-plan
status: reviewed
research_brief: "docs/research/dns-resolution-brief.md"
audience: "Curious general listeners without networking background"
duration: "5-6 minutes"
created: "2026-06-30"
---

# DNS Resolution Story Plan

## Listener change

Move the listener from “DNS is a single lookup that turns a name into an address” to a delegated-journey model: a resolver checks reusable knowledge, follows the hierarchy when needed, reaches authoritative data, and treats the answer as temporary.

## Hook

Open on the small pause after asking for a name online. Reveal that the answer may come from remembered data or from a chain of delegated questions rather than one global directory. Evidence: `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:32`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`.

## Motivation

Understanding the path explains why repeat lookups can avoid another authoritative consultation and why an answer has a reuse limit. Evidence: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`.

## Problem

Challenge the one-directory mental model. Distinguish the client-facing recursive role, referral-following iterative work, and authoritative local knowledge. Evidence: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:32`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:34`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:35`.

## Explanation

Build the model in order: a question names the domain, type, and class; the resolver checks local information; it follows referrals when needed; an authoritative server answers from its zone knowledge; the response returns through the resolver; cached data may be reused only within its TTL. Keep wire-format detail subordinate to this causal path. Evidence: `knowledge/obsidian/sources/RFC 1035 Domain Names Implementation and Specification.md:33`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:36`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:34`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`.

## Examples

Use an invented request for an address record. First play it with an empty cache, then replay it while cached data remains reusable. Do not claim a live domain value. Evidence: `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:37`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`.

## Comparison

Contrast recursive service (“bring back a final answer”), iterative resolution (“follow this referral”), and authoritative service (“answer from local zone knowledge”). Evidence: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:32`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:35`.

## Common mistakes

Correct three errors: every lookup goes straight to an authoritative server; authoritative servers search elsewhere for answers; and TTL proves an answer is true until expiry. TTL is a reuse boundary, not an accuracy guarantee. Evidence: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:35`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`.

## Recap

Return to five verbs: ask, check, follow, answer, reuse. Tie each verb to the responsible system role. Evidence: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:36`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:34`.

## Takeaway

DNS resolution is a temporary, delegated answer assembled through explicit roles—not a permanent fact fetched from one universal directory. Evidence: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:32`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`.

## Caveats

Do not generalize the 1987 RFCs into a complete modern operational guide. Exclude DNSSEC, encrypted DNS, privacy, policy filtering, attacks, and claims about live resolver latency or market behavior.
