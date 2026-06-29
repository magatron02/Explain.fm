---
type: source
status: accepted
title: "RFC 9499: DNS Terminology"
source_url: "https://www.rfc-editor.org/rfc/rfc9499.html"
source_type: "IETF Best Current Practice"
author: "Paul Hoffman; Kazunori Fujiwara"
publisher: "RFC Editor"
published: "2024-03"
accessed: "2026-06-29"
authority: "Primary standards terminology; BCP 219"
license: "IETF Trust Legal Provisions and RFC publication notice"
usage_rights: "Cite and paraphrase factual definitions; do not reproduce the full RFC"
topics: [DNS, resolution, caching]
tags: [source, standard, dns]
---

# RFC 9499: DNS Terminology

## Why this source matters

This Best Current Practice consolidates current DNS terminology and clarifies how modern usage differs from the original 1987 specifications.

## Scope

Current definitions for DNS records, resolvers, resolution modes, authoritative servers, caching, and related operational terms. It is a terminology reference, not a complete protocol tutorial.

## Key claims and evidence

| Claim | Evidence or location | Confidence |
| --- | --- | --- |
| DNS is a query-response protocol whose request and response messages share a format. | Section 1, “Introduction” | High |
| A resolver performs queries for a name, type, and class and receives responses. | Section 6, “Resolver” | High |
| In recursive mode, a server answers from local cache or queries other servers to obtain a final answer. | Section 6, “Recursive mode” | High |
| An authoritative server answers from local knowledge about a DNS zone without querying other servers. | Section 6, “Authoritative server” | High |
| A record TTL limits how long cached data may be used before the information source should be consulted again. | Section 5, “TTL” | High |
| Address records are currently records of type A or AAAA. | Section 5, “Address records” | High |

## Limitations and uncertainty

- Terminology alone does not describe every lookup step or deployment variation.
- The document incorporates and updates definitions from many RFCs; original protocol requirements remain distributed across those standards.
- Resolver policy, split DNS, encrypted transport, and DNSSEC can change what a user observes and are outside this first brief.

## Raw artifact

No local copy. Use the canonical RFC Editor HTML and preserve the RFC number and accessed date.

## Derived notes

- [[DNS Resolution]]
- [[RFC 1034 Domain Names Concepts and Facilities]]
- [[RFC 1035 Domain Names Implementation and Specification]]

## Review

- [x] Provenance verified
- [x] Authority assessed
- [x] Usage rights recorded
- [x] Claims trace to evidence
- [x] Noise and duplication excluded
