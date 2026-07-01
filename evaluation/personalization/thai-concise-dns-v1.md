---
type: personalization-experiment
status: complete-option-a-rejected
preference_scope: request-only
preference: "Short, visual, low-jargon Thai explanation"
retention: "Evaluation artifact only; no listener profile created"
created: "2026-07-01"
---

# Thai Concise DNS Personalization v1

## Control

The control is the passed six-turn, 31.312-second `evaluation/voice-smoke/thai-dns-dialogue-v2.mp3`. It introduces resolver, cache, and TTL directly.

## Personalized script

**MAYA:** ลองนึกภาพว่า ดีเอ็นเอสเป็นคนช่วยหาที่อยู่ของเว็บไซต์ แต่ไม่ต้องออกไปถามใหม่ทุกครั้ง

**NARIN:** เพราะจำคำตอบเดิมไว้ เหมือนจดไว้บนโพสต์อิทใช่ไหม

**MAYA:** ใช่ค่ะ แต่โพสต์อิทใบนั้นมีเวลาหมดอายุที่เรียกว่า ทีทีแอล พอหมดเวลา ระบบต้องตรวจคำตอบใหม่

**NARIN:** สรุปคือ จำไว้เพื่อให้เร็ว แต่เช็กใหม่เพื่อไม่ให้ใช้ข้อมูลเก่าตลอดไป

## Evidence

- Cached data may answer before a new authoritative lookup: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`
- TTL limits how long cached data may be reused: `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`

The Post-it note is a declared teaching analogy, not a factual claim about DNS storage.

## Evaluation

- Control: 6 turns, 454 Thai-script characters, 4 introduced technical terms
- Personalized: 4 turns, 285 Thai-script characters, 2 introduced technical terms
- Structural change: 33% fewer turns, 37% fewer characters, and 50% fewer technical terms while retaining cache reuse and expiry
- Audio artifact: `thai-concise-dns-v1.mp3` (rejected; deleted after review)
- Audio output: 19.909 seconds, MP3 192 kbps, mono, 48 kHz
- Audio SHA-256: `2c7dc1e536826cf3280cdd978c10d3d1354b2fa28a8cce0a85dcdc708a706ca5`
- Duration change: 31.312 seconds to 19.909 seconds, 36% shorter
- Renderer: local `openbmb/VoxCPM2`, cached snapshot `bffb3df5a29440629464e5e839f4d214c8714c3d`, CPU, 10 inference steps, denoiser disabled
- Assembly: FFmpeg silence cap, MAYA clarity EQ, -18 LUFS per-turn target, and 0.22-second planned turn gaps
- Automated silence check: no interval of at least 0.45 seconds detected at -40 dB
- Render history: the official Space remained queue-full even after HF login; the local route succeeded after freeing commit memory
- Provider decision: no paid or alternative renderer was added
- Human preference-fit review: **Revise** — MAYA sounded natural, but some sentence endings were cut; NARIN sounded robotic
- Comparative understanding review: Not evaluated on rejected audio
- Comprehension prompt: Why should the system check the answer again after the remembered answer expires?

## Audio revision v2

`thai-concise-dns-v2.mp3` preserves both accepted MAYA raw turns and removes the stop-silence filter that cut low-amplitude sentence endings. Both NARIN turns were rerendered locally with CFG 1.5 from the passed NARIN segment in `thai-dns-dialogue-v2.mp3`, replacing the longer reference and CFG 2.0 used in v1.

Two measured pauses inside the final NARIN turn were shortened from 0.431 and 0.554 seconds to 0.22 seconds by trimming silence at exact boundaries; speech boundaries were not filtered.

- Duration: 20.340 seconds
- Format: MP3, 192 kbps, mono, 48 kHz
- SHA-256: `70a8f5f39d2ca15efb58f8019e876cfb60170168c9b3cb9eca541ff48b762ef7`
- Automated silence check: no interval of at least 0.45 seconds detected at -40 dB
- Human preference-fit review: **Pass** — Founder, 2026-07-01
- Comparative understanding review: **Fail** — the user selected distractor 2 (“to make the audio louder”) instead of the supported reason

## Corrective check

After explicit corrective feedback, the user correctly selected “ask the information source again” rather than “keep using the old answer.” This confirms the correction was understood, but it is not attributed to the v2 audio.

## Learning revision v3

The final NARIN turn is revised to make the action and reason adjacent:

**NARIN-V3:** พอ ทีทีแอล หมด ระบบจะไม่ใช้โพสต์อิทใบเดิมต่อ แต่จะถามแหล่งข้อมูลใหม่ เพื่อไม่ให้ข้อมูลเก่าถูกใช้ตลอดไป

Only this turn is rerendered. All passed MAYA audio and the first NARIN turn remain unchanged.

- Audio artifact: `thai-concise-dns-v3.mp3`
- Duration: 22.466 seconds
- Format: MP3, 192 kbps, mono, 48 kHz
- SHA-256: `2187953a17e61641e3784a75cf73c7c4359d33cce910d97d4c5a13c272a4f52d`
- Automated silence check: no interval of at least 0.45 seconds detected at -40 dB
- Human preference-fit review: **Pass** — Founder, 2026-07-01
- Transfer comprehension review: **Fail** — the user selected “must ask the information source every time” instead of “may reuse the cached answer while TTL remains valid”
- Retention: v3 audio deleted after the failed learning gate; hash retained for traceability

## Final decision

Option A is rejected. It met the explicit brevity and audio preferences but failed both the initial and transfer comprehension checks. Do not promote this concise adaptation as effective personalization.
