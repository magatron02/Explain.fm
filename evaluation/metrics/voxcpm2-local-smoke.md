# VoxCPM2 Local Voice Smoke Test

- Date: 2026-06-30
- Result: Functional smoke test; rejected for full local episode on current hardware
- Runtime: `voxcpm` 2.0.3, PyTorch 2.12.1 CPU build, Python 3.11.15
- Hardware: 32 GB system RAM; NVIDIA RTX 3060 Laptop GPU with 6 GB total VRAM and about 3.5 GB free during the test
- Model: `openbmb/VoxCPM2`, denoiser disabled, 10 inference steps

## Official capability boundary

The official project documents Apache-2.0 code and weights, 30-language support including English and Thai, 48 kHz output, and about 8 GB VRAM for VoxCPM2. Its supported Python range includes 3.11 and its documented CPU fallback requires optimization to be disabled.

- Documentation: `https://voxcpm.readthedocs.io/en/latest/`
- Installation: `https://voxcpm.readthedocs.io/en/latest/installation.html`
- VRAM reference: `https://voxcpm.readthedocs.io/en/latest/faq.html`
- Repository: `https://github.com/OpenBMB/VoxCPM`

## Measured result

| Check | Result |
| --- | --- |
| Package import | Pass |
| First model fetch and load | Pass in 292.2 seconds |
| Cached model load | Pass in 18.7 seconds |
| Short voice-design render | Pass: 2.24 seconds of audio in 53.7 seconds |
| Output format | PCM 16-bit, mono, 48 kHz, 215,084 bytes |
| Real-time factor | Approximately 24.0 on CPU |
| Full 5-minute episode estimate | Approximately 2 hours of rendering before review |
| Audio quality review | Not performed; no listening judgment is fabricated |

The installed 2.0.3 API rejected the README's `seed` keyword; deterministic setup required `torch.manual_seed` instead. This compatibility difference must be pinned or handled before a reusable renderer is built.

## Decision

Do not render or commit the full episode through the current CPU route. Do not add VoxCPM as a repository dependency yet. The next voice test requires either at least 8 GB available CUDA VRAM or an explicitly approved hosted renderer, followed by human listening review against `evaluation/rubrics/audio-v1.md`.

The smoke WAV remains a machine-local temporary artifact and is not represented as an episode.
