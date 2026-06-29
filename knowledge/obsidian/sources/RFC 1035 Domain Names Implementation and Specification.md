---
type: source
status: accepted
title: "RFC 1035: Domain Names — Implementation and Specification"
source_url: "https://www.rfc-editor.org/rfc/rfc1035.html"
source_type: "Internet Standard"
author: "Paul Mockapetris"
publisher: "RFC Editor"
published: "1987-11"
accessed: "2026-06-29"
authority: "Foundational DNS wire-format specification; STD 13 component"
license: "IETF Trust Legal Provisions and RFC publication notice"
usage_rights: "Cite and paraphrase factual content; do not reproduce the full RFC"
topics: [DNS, messages, transport]
tags: [source, standard, dns]
---

# RFC 1035: Domain Names — Implementation and Specification

## Why this source matters

This foundational standard defines DNS resource-record and message structures and the original transport behavior used by implementations.

## Scope

Base DNS formats, messages, transport, master files, server behavior, and resolver behavior. Later RFCs update many details, so claims here are limited to enduring base mechanisms.

## Key claims and evidence

| Claim | Evidence or location | Confidence |
| --- | --- | --- |
| DNS messages contain a header followed by question, answer, authority, and additional sections. | Section 4.1, “Format” | High |
| A DNS question identifies a domain name, query type, and query class. | Section 4.1.2, “Question section format” | High |
| Resource records carry a name, type, class, TTL, data length, and record data. | Section 4.1.3, “Resource record format” | High |
| The base specification defines DNS access over both UDP port 53 and TCP port 53. | Section 4.2, “Transport” | High for the base protocol |
| An A record stores a 32-bit Internet address. | Section 3.4.1, “A RDATA format” | High for IPv4 A records |
| TCP DNS messages are prefixed by a two-byte length field. | Section 4.2.2, “TCP usage” | High |

## Limitations and uncertainty

- RFC 1035 has many updating RFCs; its original UDP size and transport recommendations are not a complete modern rule set.
- AAAA records, EDNS, DNSSEC, encrypted DNS, and later TCP requirements are defined elsewhere.
- This note does not claim that all modern DNS traffic uses only the original transport behavior.

## Raw artifact

No local copy. Use the canonical RFC Editor HTML and consult its “Updated by” metadata before implementation decisions.

## Derived notes

- [[DNS Resolution]]
- [[RFC 9499 DNS Terminology]]
- [[RFC 1034 Domain Names Concepts and Facilities]]

## Review

- [x] Provenance verified
- [x] Authority assessed
- [x] Usage rights recorded
- [x] Claims trace to evidence
- [x] Noise and duplication excluded
