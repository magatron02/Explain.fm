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
| Duration | 305.246 seconds |
| Format | MP3, 48 kHz, mono, 192 kbps |
| Integrated loudness | -18.7 LUFS |
| Loudness range | 2.8 LU |
| Peak | -2.2 dB |
| ASR diagnostic | 2.5% word error rate: 18 edits across 719 reference words; 28/40 turns exact |
| Artifact SHA-256 | `4b46b5beebffc288811e618f1716bc2a2a940db2f831d36d6fe5201fb5267fde` |

## Renderer traceability

The episode was rendered through the official public `openbmb/VoxCPM-Demo` Space at revision `466abca91d371190950871c97d34ea7da6e2a0f1`. The Space identifies the backend as VoxCPM2 but does not expose the hidden backend model revision. Submitted text was already public in this repository; the Space records request text in its service log.

The same Space's `FunAudioLLM/SenseVoiceSmall` route was used as an intelligibility diagnostic. Its result has no predeclared acceptance threshold and does not replace listening. One unclear “quad-A” turn was regenerated and then transcribed correctly; remaining differences are retained in the manifest.

## Listening gate

The artifact is open in Audacity for human review. Do not mark Era 2 complete until a listener confirms intelligibility, meaning preservation, speaker distinction, pronunciation, naturalness, and complete-episode listenability.
