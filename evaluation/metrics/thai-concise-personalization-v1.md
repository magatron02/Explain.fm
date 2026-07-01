# Thai Concise Personalization Result v1

- Date: 2026-07-01
- Experiment: `evaluation/personalization/thai-concise-dns-v1.md`
- Result: Preference fit passed; learning improvement unmeasured

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

## Decision

The experiment demonstrates successful request-level preference fit without profiling or a new dependency. It does not demonstrate improved understanding or retention because the comprehension prompt received no answer. Era 4 remains active.
