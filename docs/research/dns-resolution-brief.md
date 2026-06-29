---
type: research-brief
status: reviewed
question: "How does DNS turn a domain name into an address, and what makes the answer temporary?"
audience: "Curious general listeners without networking background"
created: "2026-06-29"
---

# DNS Resolution Brief

## Scope

This brief explains the core path from a user's domain-name question to a DNS response: the hierarchy, resolver roles, referrals, authoritative data, caching, TTL, address records, and base message transport. It does not claim that every query returns an address or cover DNSSEC, encrypted DNS, policy filtering, or attacks.

## Findings

| Claim | Evidence | Source quality | Uncertainty |
| --- | --- | --- | --- |
| DNS is a query-response protocol, and a question identifies a domain name, record type, and class. | `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:32`<br>`knowledge/obsidian/sources/RFC 1035 Domain Names Implementation and Specification.md:33` | Current IETF terminology plus the base wire specification | Later extensions add capabilities without changing this basic mental model. |
| A recursive server pursues a final answer for its client, while iterative resolution follows referrals between servers. | `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:32`<br>`knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:34` | Foundational standard corroborated by current terminology | Real clients often use a stub resolver and delegate this work to a recursive service. |
| DNS organizes names as a tree divided into zones; authoritative servers answer from local knowledge about zones they serve. | `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:34`<br>`knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:35`<br>`knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:35` | Foundational architecture plus current terminology | Split DNS and resolver policy can make observed answers context-dependent. |
| A resolver checks local information before asking servers, and cached data can avoid a new authoritative lookup. | `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:36`<br>`knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37` | Primary resolver algorithm | Implementations and cache policy vary. |
| TTL bounds how long cached record data may be reused before consulting the information source again. | `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36` | Current Best Current Practice terminology | Cache operators may shorten retention, so TTL is a maximum rather than a guarantee. |
| Address answers use A or AAAA records, while the base protocol defines DNS messages over both UDP and TCP port 53. | `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:37`<br>`knowledge/obsidian/sources/RFC 1035 Domain Names Implementation and Specification.md:35` | Current record terminology plus the base protocol | Modern DNS also uses later extensions and encrypted transports outside this brief. |

## Disagreements and uncertainty

The standards agree on the bounded core model. RFC 1034 and RFC 1035 are foundational documents from 1987 and have many updates, so their old operational recommendations should not be generalized into claims about all modern DNS traffic. The corpus describes standards, not measured resolver behavior on a specific network.

## Open questions

- Which concrete domain should a future explanation trace without implying that its live answer is stable?
- How should a later episode distinguish DNS authenticity from DNS confidentiality?
- Which modern transport details materially improve listener understanding without overwhelming the core lookup journey?

## Recommendation

Teach the lookup as a delegated journey: ask the local resolver, check the cache, follow the hierarchy when necessary, obtain an authoritative record, and reuse it only within its TTL boundary. Keep message-format and transport details subordinate to that mental model.
