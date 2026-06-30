---
type: episode-script
status: reviewed
story_plan: "docs/design/dns-resolution-story-plan.md"
research_brief: "docs/research/dns-resolution-brief.md"
audience: "Curious general listeners without networking background"
created: "2026-06-30"
---

# DNS Resolution: The Answer That Expires

## Hook

**MAYA:** You ask for a name online, and a moment later your device has somewhere to send the request. It feels like one quick lookup.

**NARIN:** As if the internet keeps one enormous directory?

**MAYA:** Exactly. But the useful mental model is not one directory. It is a delegated conversation—and sometimes that conversation does not happen at all because an earlier answer can still be reused.

**NARIN:** So the tiny pause hides either a journey or a memory.

Evidence: `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:32`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`.

## Motivation

**MAYA:** That distinction explains two everyday mysteries: why a repeated lookup can avoid going back to the original source, and why the answer is never something a resolver should remember forever.

**NARIN:** The speed and the expiry come from the same design?

**MAYA:** Right. Reuse saves work. A time limit prevents that reused data from becoming permanent truth.

Evidence: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`.

## Problem

**NARIN:** Let me try the simple version: my device asks DNS for a name, DNS returns an address, done.

**MAYA:** That sentence collapses several jobs into one. A resolver asks questions for a client. In recursive mode, the server takes responsibility for obtaining a final answer. During iterative resolution, the next response may instead be a referral telling the resolver where to continue.

**NARIN:** And the authoritative server?

**MAYA:** Different job. It answers from local knowledge about the zone it serves. It is not the part wandering around asking other servers.

Evidence: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:32`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:34`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:35`.

## Explanation

**MAYA:** Start with the question. It identifies a domain name, a query type, and a query class.

**NARIN:** So even the question is more precise than “where is this name?”

**MAYA:** Yes. Then the resolver checks local information first. If it cannot answer there, it chooses servers, sends queries, and examines the responses.

**NARIN:** Where does the hierarchy enter?

**MAYA:** DNS names form a tree. Information is organized into zones, and referrals let the resolver continue through that structure until it reaches relevant authoritative knowledge.

**NARIN:** Then the answer travels back through the resolver to the client.

**MAYA:** And the response has structure. The base message format has a header followed by question, answer, authority, and additional sections. That matters, but it is supporting machinery. The core idea is still: check, ask, follow, and return.

Evidence: `knowledge/obsidian/sources/RFC 1035 Domain Names Implementation and Specification.md:33`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:36`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:34`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:35`, `knowledge/obsidian/sources/RFC 1035 Domain Names Implementation and Specification.md:32`.

## Examples

**NARIN:** Give me a concrete run.

**MAYA:** Imagine asking for an address record for a made-up service name. On the first run, the resolver has no reusable answer. It checks local information, follows the needed referrals, and obtains an answer from authoritative data.

**NARIN:** And address answers use A, or quad-A, records.

**MAYA:** Correct. Now ask again while the cached record is still reusable. The resolver may answer from that cache before consulting an authoritative server again.

**NARIN:** Same question, shorter journey.

**MAYA:** Or no external journey at all.

Evidence: `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:37`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:36`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`.

## Comparison

**NARIN:** I want the three roles in one clean comparison.

**MAYA:** Recursive means: “Take responsibility for bringing me a final answer.” Iterative means: “Here is a referral; continue the search there.” Authoritative means: “I can answer from local knowledge for the zone I serve.”

**NARIN:** One accepts responsibility, one advances the route, and one holds the relevant local data.

**MAYA:** Exactly. Keeping those roles separate prevents the system from sounding like one mysterious DNS machine.

Evidence: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:32`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:35`.

## Common mistakes

**NARIN:** Mistake one: every lookup goes directly to an authoritative server.

**MAYA:** Cached data can answer first, so no.

**NARIN:** Mistake two: an authoritative server searches other servers until it finds something.

**MAYA:** Also no. Its defining role here is answering from local zone knowledge.

**NARIN:** Mistake three: if a record has not reached its TTL, the answer is guaranteed to be correct.

**MAYA:** TTL says how long cached data may be reused before the information source should be consulted again. It is a reuse boundary, not a proof that the underlying claim is true.

**NARIN:** And not every DNS question has to request an address, because the question carries a record type.

**MAYA:** Good. An address lookup is one useful example, not the definition of every DNS exchange.

Evidence: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:35`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`, `knowledge/obsidian/sources/RFC 1035 Domain Names Implementation and Specification.md:33`.

## Recap

**MAYA:** Five verbs. Ask: form a question with a name, type, and class. Check: inspect local information and cache. Follow: use referrals when the answer is not local. Answer: obtain relevant authoritative data. Reuse: keep cached data only within its TTL boundary.

**NARIN:** Ask, check, follow, answer, reuse. That is much easier to remember than a list of server names.

Evidence: `knowledge/obsidian/sources/RFC 1035 Domain Names Implementation and Specification.md:33`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:36`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:32`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`.

## Takeaway

**NARIN:** So DNS resolution is not a permanent answer fetched from one universal directory.

**MAYA:** It is a delegated answer assembled through distinct roles, sometimes shortened by memory, and always bounded by what the evidence and its reuse window actually support.

Evidence: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:32`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`.

## Pronunciation notes

- DNS: “dee-en-ess”
- TTL: “tee-tee-el”
- AAAA: “quad-A”

## Review flags

- Confirm pacing and pauses after the first synthesized read.
- Voice casting and renderer selection remain unapproved.
