# Thai Voice Smoke Test

- Date: 2026-06-30
- Status: Passed Thai voice smoke test
- Scope: Thai capability check only, not a complete episode or Audio Rubric v1 pass
- Renderer: OpenBMB official `openbmb/VoxCPM-Demo` Hugging Face Space
- Space revision: `466abca91d371190950871c97d34ea7da6e2a0f1`
- API: `/generate`
- Model: VoxCPM2; the public Space does not expose its hidden backend model revision
- Configuration: CFG 2.0, normalization off, denoise off, voice design without reference audio
- Disclosure: the public Space logs submitted request text

## Render text

> เวลาคุณพิมพ์ชื่อเว็บไซต์ อุปกรณ์ไม่ได้รู้ทันทีว่าจะส่งคำขอไปที่ไหน ระบบดีเอ็นเอสจึงช่วยแปลงชื่อให้เป็นที่อยู่ รีโซลเวอร์อาจตอบจากข้อมูลในแคช หรือเดินตามลำดับชั้นไปยังเซิร์ฟเวอร์ต้นทาง ข้อมูลในแคชมีอายุจำกัดด้วยค่า ทีทีแอล จึงช่วยให้คำขอครั้งต่อไปเร็วขึ้น โดยไม่เก็บคำตอบเดิมไว้ตลอดไป

Pronunciation spellings are declared transformations: `DNS` → `ดีเอ็นเอส`, `resolver` → `รีโซลเวอร์`, `cache` → `แคช`, and `TTL` → `ทีทีแอล`.

## Variants

| Artifact | Voice direction | Duration | SHA-256 |
| --- | --- | ---: | --- |
| `thai-dns-calm-woman.mp3` | Calm adult Thai woman host; warm, clear, trustworthy, natural conversational pace, restrained expression | 12.984 s | `163999d743c487e39eb711df12386b88a6df99b8de2b97cd82a05465b209edc9` |
| `thai-dns-thoughtful-man.mp3` | Thoughtful adult Thai man co-host; clear, conversational, trustworthy, natural pace, slightly curious energy | 29.952 s | `3bd50f09bab8b01afe169f6da8a5508c88a952a8f266a4a8a1a5772eb68c2a41` |

Both artifacts are MP3, 192 kbps, mono, 48 kHz. The large duration difference makes pace and completeness explicit listening checks. The Space ASR returned only `.` for both Thai samples, so it provides no usable completeness evidence and is not an acceptance signal.

## Corrected UTF-8 variant

`thai-dns-utf8-v1.mp3` was rendered after reading `thai-dns-input.txt` explicitly as UTF-8. A preflight assertion confirmed 283 input characters, including 275 Thai Unicode characters and no question marks.

- Voice direction: thoughtful adult Thai man host; clear, conversational, trustworthy, natural pace, restrained expression
- Duration: 19.392 seconds
- Format: MP3, 192 kbps, mono, 48 kHz
- SHA-256: `425685d55779cd8977871ffad35815b7c06714e8b8107b4a3ccd2cd54a742e72`
- Human decision: **Revise** — Founder reported intrusive noise

## Clean-source revision

`thai-dns-clean-v2.mp3` keeps the verified UTF-8 input and changes only the voice direction by requiring a clean, dry professional studio recording with no background noise, music, sound effects, or room ambience. No post-processing noise filter was added, so this test isolates whether VoxCPM2 can avoid the artifact at generation time.

- Duration: 21.144 seconds
- Format: MP3, 192 kbps, mono, 48 kHz
- SHA-256: `3cae0f1dae4283b0c752f57752293fc178c4f49f1a597cd8cf75f96fada8b2d6`
- Human decision: **Revise** — dead air at 0:12–0:13 and excessive spacing at 0:15–0:16

Automated silence detection confirmed a 1.498-second silent interval from 12.473 to 13.971 seconds and a 0.302-second interval from 16.711 to 17.013 seconds.

## Timing revision

`thai-dns-tight-v3.mp3` preserves the v2 speech and uses FFmpeg `silenceremove` only to cap detected silence. Threshold: -40 dB; detection duration: 0.20 seconds; retained silence: 0.05 seconds. The long interval is reduced to 0.208 seconds, and the later interval is reduced to 0.259 seconds after the timeline shift.

- Duration: 19.724 seconds
- Format: MP3, 192 kbps, mono, 48 kHz
- SHA-256: `efc95656ad0cce1ad7f1945881c5e1bccc03d371e8a0804a1a0797575b640ea7`
- Human decision: **Pass** — Founder, 2026-06-30

This pass confirms intelligible Thai synthesis with acceptable noise and pause handling for this short sample. It does not satisfy `evaluation/rubrics/audio-v1.md`, which requires a complete rendered episode.

## Listening decision

Initial Founder review on 2026-06-30: **Revise both variants** because neither contained recognizable words.

Follow-up finding: both variants produced no recognizable words. The generation command piped its Python source through Windows PowerShell while `$OutputEncoding` was `us-ascii` and the active code page was 437. A direct byte check confirmed every Thai character became `?` (`0x3f`) before the request reached VoxCPM2. This invalidates both artifacts as Thai model evaluations; the rejected audio files were deleted.

The rejected configurations are:

- `thai-dns-calm-woman.mp3` — Invalid input encoding; deleted
- `thai-dns-thoughtful-man.mp3` — Invalid input encoding; deleted

Listening criteria:

- Every sentence is present and intelligible.
- `ดีเอ็นเอส`, `รีโซลเวอร์`, `แคช`, and `ทีทีแอล` sound correct.
- Pace and phrasing feel natural in Thai.
- Delivery preserves the explanation and sounds trustworthy.

The corrected test reads `thai-dns-input.txt` as UTF-8 instead of embedding Thai text in a PowerShell pipe. Only one variant is rerendered first; a second voice is unnecessary until intelligible Thai is confirmed.
