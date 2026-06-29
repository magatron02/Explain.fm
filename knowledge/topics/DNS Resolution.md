---
type: topic
status: reviewed
title: "DNS Resolution"
topics: [DNS, Internet infrastructure]
tags: [topic, dns]
---

# DNS Resolution

DNS resolution is the process that turns a question about a domain name and record type into a response. A recursive resolver can answer from cache or contact other servers, while authoritative servers provide zone data from local knowledge.

## Source notes

- [[RFC 9499 DNS Terminology]]
- [[RFC 1034 Domain Names Concepts and Facilities]]
- [[RFC 1035 Domain Names Implementation and Specification]]

## Explanation boundary

The first brief covers the hierarchy, resolver journey, caching, authoritative answers, and base message shape. DNSSEC, encrypted DNS, privacy, policy filtering, and operational attacks remain separate topics.
