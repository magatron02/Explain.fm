# DNS Audio Automated Review

- Date: 2026-06-30
- Artifact: `evaluation/golden-episodes/dns-resolution-v1.mp3`
- Manifest: `evaluation/golden-episodes/dns-resolution-v1.manifest.json`
- Script: `evaluation/golden-episodes/dns-resolution-script.md`
- Rubric: `evaluation/rubrics/audio-v1.md`
- Status: Automated gates passed; listening gates pending

## Automated result

| Check | Result |
| --- | --- |
| Script coverage | Pass: 40/40 speaker turns in order |
| Declared transformations | Pass: DNS → D N S; TTL → T T L; AAAA → quad A |
| Speaker mapping | Pass: two synthetic seed voices reused through controllable cloning |
| Duration | 303.974 seconds |
| Format | MP3, 48 kHz, mono, 192 kbps |
| Integrated loudness | -18.7 LUFS |
| Loudness range | 2.8 LU |
| Peak | -2.2 dB |
| Artifact SHA-256 | `e836c0aa9c6c7183ea080ea656270335f28fa98bea5b5ea238671bd953834fc6` |

## Renderer traceability

The episode was rendered through the official public `openbmb/VoxCPM-Demo` Space at revision `466abca91d371190950871c97d34ea7da6e2a0f1`. The Space identifies the backend as VoxCPM2 but does not expose the hidden backend model revision. Submitted text was already public in this repository; the Space records request text in its service log.

## Listening gate

The artifact is open in Audacity for human review. Do not mark Era 2 complete until a listener confirms intelligibility, meaning preservation, speaker distinction, pronunciation, naturalness, and complete-episode listenability.
