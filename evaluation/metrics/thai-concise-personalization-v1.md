# Thai Concise Personalization Result v1

- Date: 2026-07-01
- Experiment: `evaluation/personalization/thai-concise-dns-v1.md`
- Result: Preference fit passed; comprehension failed

## Explicit preference

The user selected option A: a short, visual, low-jargon explanation. The preference remained request-scoped; no persistent listener profile or inferred trait was created.

## Measured adaptation

| Measure | Control | Personalized | Change |
| --- | ---: | ---: | ---: |
| Speaker turns | 6 | 4 | -33% |
| Thai-script characters | 454 | 285 | -37% |
| Introduced technical terms | 4 | 2 | -50% |
| Audio duration | 31.312 s | 20.340 s | -35% |

The personalized version retains the cache-reuse and expiry claims with accepted-source citations and adds a declared Post-it-note analogy.

## Audio review

The first render was revised because sentence endings were cut and NARIN sounded robotic. Version 2 preserved MAYA endings, rerendered NARIN from a passed reference with lower CFG, and shortened only measured silence. The Founder returned `Pass` for version 2.

## Comprehension result

The user selected the distractor “check again to make the audio louder.” The expected answer was “check again to avoid reusing old data indefinitely.” Preference fit therefore did not produce a demonstrated learning benefit.

After corrective feedback, a learning revision placed the expiry action and reason in one final turn. The audio passed preference-fit review, but the transfer check also failed: the user selected “must ask the source every time” rather than “may reuse the cached answer while TTL remains valid.”

## Decision

Option A is rejected. The experiment demonstrates successful request-level preference fit without profiling or a new dependency, but two failed comprehension checks show that shorter and lower-jargon did not improve learning in this case. Era 4 remains active; the next experiment should test a more detailed explanation rather than continue polishing this variant.
