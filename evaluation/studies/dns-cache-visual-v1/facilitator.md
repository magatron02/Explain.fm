# Facilitator Guide

Keep this file hidden from participants until all study responses are complete.

## Consent script

“This voluntary Explain.fm prototype study compares two explanation styles. You may stop at any time. We record a random study ID, your explicit visual-analogy preference, assigned packet, scores, and completion state. We do not need your name, contact details, recording, or sensitive information. Raw responses and the ID mapping stay outside the repository and are deleted after scoring and follow-up. Only aggregated results may be committed. Do you consent?”

## Pre-test prompts

1. Before hearing the explanation, what may a system do when it already has a cached DNS answer whose reuse time has not expired?
2. What should happen after that reuse time expires?
3. Does TTL prove that a cached answer is factually correct? Explain briefly.

## Post-test prompts

1. A cached answer still has TTL time remaining. Must the system ask the information source again, or may it reuse the answer? Why?
2. A cached answer's TTL has ended. What should the system do next?
3. What does TTL limit, and what does it not guarantee?

## Delayed-recall prompts

1. Explain the difference between using a cached DNS answer before and after TTL expiry.
2. Why is TTL not the same as a guarantee that an answer is correct?

## Scoring key

Score each response using `evaluation/rubrics/listener-comprehension-v1.md`.

- **Before expiry:** 2 points for stating that the cached answer may be reused; 1 for recognizing reuse without the time boundary; 0 for requiring a new lookup every time or giving no relevant answer.
- **After expiry:** 2 points for consulting the information source again instead of reusing the old answer; 1 for saying “check again” without identifying what changes; 0 for continuing indefinite reuse or giving no relevant answer.
- **TTL boundary:** 2 points for saying TTL limits reuse duration and does not prove correctness; 1 for only one half; 0 for claiming TTL guarantees truth or giving no relevant answer.

Factual grounding: cache reuse is supported by `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`; the TTL boundary is supported by `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`.

## Aggregate report template

| Condition | Assigned | Completed immediate | Completed delayed | Withdrawn | Median pre (0–6) | Median post (0–6) | Median gain | Median delayed (0–4) | Factual errors | Preference followed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| X control |  |  |  |  |  |  |  |  |  |  |
| Y personalized |  |  |  |  |  |  |  |  |  |  |

Decision: Pass | Fail | Inconclusive

Limitations:
