# Thai DNS Two-Speaker Smoke Script

- Status: Passed two-speaker Thai voice smoke test
- Source basis: `evaluation/golden-episodes/dns-resolution-script.md`
- Evidence: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:32`, `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`, `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`

## Voice seeds

**MAYA-SEED:** สวัสดีค่ะ ฉันจะช่วยเล่าเรื่องยากให้เห็นภาพชัดขึ้น ด้วยน้ำเสียงที่เป็นธรรมชาติและไว้ใจได้

**NARIN-SEED:** สวัสดีครับ ผมจะถามในจุดที่คนฟังอาจสงสัย เพื่อให้คำอธิบายชัดเจนและจำได้ง่ายขึ้น

**MAYA-V2-SEED:** ลองนึกภาพนะคะ เราพิมพ์ชื่อเว็บไซต์เพียงครั้งเดียว แต่เบื้องหลังมีทั้งการค้นหาและการจดจำคำตอบเดิม

## Dialogue

**MAYA:** เคยสังเกตไหมว่า พอเราพิมพ์ชื่อเว็บไซต์ เครื่องก็รู้แทบจะทันทีว่าต้องส่งคำขอไปที่ไหน

**NARIN:** งั้นดีเอ็นเอสก็คือสมุดโทรศัพท์กลางของอินเทอร์เน็ตใช่ไหม

**MAYA:** ไม่เสมอไปค่ะ รีโซลเวอร์อาจตอบจากข้อมูลในแคชก่อน หรือเดินตามลำดับชั้นไปหาเซิร์ฟเวอร์ที่มีข้อมูลต้นทาง

**NARIN:** แปลว่าการค้นหาบางครั้งเป็นการเดินทาง แต่บางครั้งเป็นการใช้ความจำ

**MAYA:** ใช่ค่ะ และความจำนั้นมีวันหมดอายุ ค่า ทีทีแอล กำหนดว่าข้อมูลในแคชนำกลับมาใช้ได้นานแค่ไหน

**NARIN:** จำง่าย ๆ คือ ถาม ตรวจ เดินตาม ตอบ แล้วค่อยใช้ซ้ำภายในเวลาที่กำหนด

## Declared pronunciation transformations

- DNS → `ดีเอ็นเอส`
- resolver → `รีโซลเวอร์`
- cache → `แคช`
- TTL → `ทีทีแอล`

## Render record

- Artifact: `thai-dns-dialogue-v1.mp3` (rejected and deleted after review)
- Renderer: OpenBMB official `openbmb/VoxCPM-Demo` Hugging Face Space, API `/generate`
- Model: VoxCPM2; the public Space does not expose its hidden backend model revision
- Method: voice-design seed per speaker, then controllable cloning per turn
- Configuration: CFG 2.0, normalization off, reference denoise off
- Assembly: FFmpeg 8.0, six turns in script order, 0.25-second planned turn gaps, -18 LUFS per-turn target, silence capped at -40 dB with 0.20-second detection and 0.05-second retained silence
- Output: MP3, 192 kbps, mono, 48 kHz, 50.299 seconds
- SHA-256: `c58d0983e8c6f056ffabc710f2fc6f038c263f74ceeadc58dc9d53f8ec00e47f`
- Long-silence check: no interval of at least 0.45 seconds detected at -40 dB
- Disclosure: the public Space logs submitted request text
- Human decision: **Revise** — Founder, 2026-06-30
- Reported defects: MAYA sounds robotic; 0:07–0:11 is distorted and unintelligible; intrusive noise remains across the dialogue
- Turn mapping: processed MAYA turn 0 ends at approximately 0:06.856, followed by the planned turn gap; 0:07–0:11 therefore falls within NARIN turn 1

This is a two-speaker capability smoke test, not a complete episode and not an Audio Rubric v1 pass.

## Listening checks

- All six turns are present in order and intelligible without reading.
- MAYA and NARIN remain distinct and internally consistent.
- Thai pronunciation and sentence rhythm sound natural.
- Turn gaps are comfortable, with no intrusive noise or dead air.
- Delivery preserves the grounded explanation.

## MAYA v2 candidate

`thai-maya-candidate-v2.mp3` isolates the first MAYA turn before another full render. It uses the `MAYA-V2-SEED`, a less formal voice direction, CFG 1.5, reference denoising during cloning, and the same accepted silence/loudness processing.

- Duration: 5.661 seconds
- Format: MP3, 192 kbps, mono, 48 kHz
- SHA-256: `2aa75ffa6c8e91bba6db74cf553c880373cf480d2da8967721291e2295543b26`
- Human decision: **Revise** — sentence and delivery are acceptable, but the voice sounds muffled
- Retention: standalone candidate deleted after rejection; hash retained for traceability

## MAYA v3 candidate

`thai-maya-candidate-v3.mp3` preserves the accepted v2 speech and changes only post-processing: an 80 Hz high-pass filter, a gentle +3 dB treble shelf from 3 kHz, and loudness normalization to restore clarity without regenerating the voice.

- Duration: 5.661 seconds
- Format: MP3, 192 kbps, mono, 48 kHz
- SHA-256: `985d41a44ee490fb172e6f470ec383dacdc45c0027c3181474ca24b757f4df79`
- Human decision: **Pass** — Founder, 2026-06-30
- Retention: standalone candidate deleted after the final dialogue passed; hash retained for traceability

## NARIN v2 candidate

`thai-narin-candidate-v2.mp3` replaces only the unintelligible first NARIN turn. It clones from the passed `thai-dns-tight-v3.mp3` voice, uses the matching UTF-8 prompt text, and enables reference denoising.

- Duration: 3.292 seconds
- Format: MP3, 192 kbps, mono, 48 kHz
- SHA-256: `cfe49fecde3a2c996ba4c23780fb181888f954a8a32f9049c49498827991f97e`
- Human decision: **Pass** — Founder, 2026-06-30
- Retention: standalone candidate deleted after the final dialogue passed; hash retained for traceability

## Dialogue v2

`thai-dns-dialogue-v2.mp3` uses the passed MAYA v3 and NARIN v2 references. The first two accepted turns are preserved; only turns 2–5 were newly rendered. Reference denoising was enabled for all new clones. MAYA receives the passed clarity EQ; all new turns receive silence control and loudness normalization.

- Turns: 6 of 6, in script order
- Duration: 31.312 seconds
- Format: MP3, 192 kbps, mono, 48 kHz
- SHA-256: `0d693dabeb1e10b6db70004a8cc1348470ffdf81f1998990e548e879ea4352e8`
- Long-silence check: no interval of at least 0.45 seconds detected at -40 dB
- Human decision: **Pass** — Founder, 2026-06-30

This pass confirms distinguishable Thai speakers, intelligible delivery, acceptable naturalness, and acceptable noise and pause handling for this short dialogue. It remains a smoke test rather than a complete Audio Rubric v1 episode pass.
