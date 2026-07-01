---
type: personalization-experiment
status: complete-option-b-rejected
preference_scope: request-only
preference: "Detailed Thai explanation with an explicit three-state sequence"
retention: "Evaluation artifact only; no listener profile created"
created: "2026-07-01"
---

# Thai Detailed DNS Personalization v1

## Reason for this variant

The concise option passed audio preference review but failed two comprehension checks. This variant changes the teaching sequence rather than polishing the voice again.

## Script

**MAYA:** ลองแบ่งการค้นหาชื่อเว็บไซต์เป็นสามช่วงนะคะ ช่วงแรก ก่อนหมดอายุ และหลังหมดอายุ

**NARIN:** ช่วงแรกยังไม่มีคำตอบในแคช ระบบจึงต้องไปขอคำตอบจากแหล่งข้อมูล

**MAYA:** เมื่อได้คำตอบแล้ว ระบบเก็บไว้พร้อมเวลา ทีทีแอล ซึ่งกำหนดว่าคำตอบนี้นำกลับมาใช้ได้นานแค่ไหน

**NARIN:** ถ้าถามซ้ำก่อน ทีทีแอล หมด ระบบอาจใช้คำตอบในแคชได้ จึงไม่ต้องออกไปถามใหม่ทุกครั้ง

**MAYA:** แต่เมื่อ ทีทีแอล หมด คำตอบเดิมจะไม่ถูกนำกลับมาใช้ต่อ ระบบต้องปรึกษาแหล่งข้อมูลอีกครั้ง

**NARIN:** สรุปคือ ก่อนหมดอายุใช้คำตอบเดิมได้ หลังหมดอายุต้องตรวจใหม่ และ ทีทีแอล บอกอายุการใช้ซ้ำ ไม่ได้รับรองว่าคำตอบถูกเสมอ

## Evidence

- Cached data may answer before a new authoritative lookup: `knowledge/obsidian/sources/RFC 1034 Domain Names Concepts and Facilities.md:37`
- TTL limits reuse before the information source is consulted again: `knowledge/obsidian/sources/RFC 9499 DNS Terminology.md:36`

## Text comprehension gate

1. Before TTL expires, may the system reuse the cached answer? **Fail** — the user selected “must ask again every time”; the expected answer was “may reuse the cached answer.”
2. After TTL expires, should the system reuse the old answer or consult the information source again? **Fail** — the user selected “reuse the old answer”; the expected answer was “consult the information source again.”

## Decision

Option B is rejected after failing both text comprehension checks. No audio was rendered. More detail alone did not produce a demonstrated learning benefit.
