---
type: source
status: accepted
title: "RFC 1034: Domain Names — Concepts and Facilities"
source_url: "https://www.rfc-editor.org/rfc/rfc1034.html"
source_type: "Internet Standard"
author: "Paul Mockapetris"
publisher: "RFC Editor"
published: "1987-11"
accessed: "2026-06-29"
authority: "Foundational DNS specification; STD 13 component"
license: "RFC publication copyright terms in effect in 1987; legacy rights administered by the IETF Trust"
usage_rights: "Cite and paraphrase factual content; do not reproduce the full RFC"
topics: [DNS, resolution, hierarchy]
tags: [source, standard, dns]
---

# RFC 1034: Domain Names — Concepts and Facilities

## Why this source matters

This foundational standard explains why DNS is distributed and how resolvers, name servers, zones, referrals, and caches cooperate.

## Scope

DNS concepts and resolver behavior defined in 1987. Later RFCs update parts of the system, so this note uses the document for enduring architecture and identifies current terminology through RFC 9499.

## Key claims and evidence

| Claim | Evidence or location | Confidence |
| --- | --- | --- |
| Recursive resolution has the first server pursue the query for the client; iterative resolution returns a referral for the client to follow. | Section 2.3, “Conventions” | High for the core distinction |
| DNS combines a tree-structured name space and resource records, name servers, and resolvers. | Section 2.4, “Elements of the DNS” | High |
| Authoritative information is organized into zones, while resolvers extract information from name servers for clients. | Section 2.4, “Elements of the DNS” | High |
| The domain name space is a tree, and a domain name lists labels on the path from a node toward the root. | Section 3.1, “Name space specifications and terminology” | High |
| A resolver first checks local information, then chooses servers, sends queries, and analyzes a response. | Section 5.3.3, “Algorithm” | High for the specified resolver model |
| Cached data can answer a request before an authoritative server is consulted. | Section 5.3.3, “Algorithm” | High for the specified resolver model |

## Limitations and uncertainty

- The RFC dates from 1987 and has been updated by later standards.
- Examples, terminology, transport assumptions, and operational guidance may not reflect modern deployments.
- This note does not treat the original text as a complete current implementation guide.

## Raw artifact

No local copy. Use the canonical RFC Editor HTML and its update metadata.

## Derived notes

- [[DNS Resolution]]
- [[RFC 9499 DNS Terminology]]
- [[RFC 1035 Domain Names Implementation and Specification]]

## Review

- [x] Provenance verified
- [x] Authority assessed
- [x] Usage rights recorded
- [x] Claims trace to evidence
- [x] Noise and duplication excluded
