---
type: story-plan
status: reviewed
research_brief: "docs/research/ai-agents-brief.md"
audience: "Thai general listeners learning while working"
duration: "4-5 minutes"
created: "2026-07-02"
---

# AI Agent Story Plan

## Listener change

เปลี่ยนภาพจำจาก “AI Agent คือแชตบอตที่ฉลาดขึ้น” เป็นวงจรทำงานที่รับเป้าหมาย เลือกขั้นตอน ใช้เครื่องมือ ดูผล และตัดสินใจว่าจะทำต่อ หยุด หรือคืนงานให้มนุษย์

## Hook

เปิดด้วยความต่างระหว่างการถามร้านอาหารจากแชตบอต กับการสั่งให้ระบบหาร้านที่ตรงเงื่อนไข ตรวจเวลาว่าง และเตรียมการจอง โดยยังไม่ทำรายการสำคัญหากไม่ได้รับอนุญาต Evidence: `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:32`, `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:36`.

## Motivation

อธิบายว่าความต่างสำคัญเพราะ agent สามารถกระทบระบบจริงได้ ความสามารถจึงต้องมาพร้อมขอบเขตและจุดส่งงานคืนมนุษย์ Evidence: `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:36`.

## Problem

แก้คำเรียกรวมที่เอา chatbot, automation, workflow และ agent มาปนกัน เน้นว่าป้ายชื่อไม่สำคัญเท่ากับว่าใครเป็นผู้เลือกขั้นตอน Evidence: `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:33`, `knowledge/obsidian/sources/Anthropic Building Effective Agents.md:32`.

## Explanation

สอนวงจรห้าจังหวะ: เป้าหมาย สังเกต ตัดสินใจ ลงมือผ่านเครื่องมือ ตรวจผล แล้ววนซ้ำหรือหยุด วาง model, instructions และ tools เป็นส่วนประกอบ ไม่สร้างภาพว่า agent มีสติ Evidence: `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:34`, `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:36`.

## Examples

ใช้ตัวอย่างจัดทริป: อ่านปฏิทิน ค้นข้อมูล เปรียบเทียบตัวเลือก ร่างแผน และขออนุมัติก่อนจ่ายเงิน แยกสิ่งที่ agent เลือกเองกับสิ่งที่มนุษย์ต้องยืนยัน Evidence: `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:32`, `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:36`.

## Comparison

เปรียบเทียบสามแบบด้วยเส้นทาง: chatbot ตอบคำถาม, fixed workflow เดินตามทางที่โค้ดกำหนด, agent เลือกบางช่วงของเส้นทางจากสถานการณ์ Evidence: `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:33`, `knowledge/obsidian/sources/Anthropic Building Effective Agents.md:32`.

## Common mistakes

แก้สามความเข้าใจผิด: มีเครื่องมือแล้วเป็น agent เสมอ, ต้องมีหลาย agent, และ agent เหมาะกับทุกงาน ชี้ว่าความซับซ้อนเพิ่มเวลา ค่าใช้จ่าย และความเสี่ยง Evidence: `knowledge/obsidian/sources/Anthropic Building Effective Agents.md:33`, `knowledge/obsidian/sources/Anthropic Building Effective Agents.md:34`, `knowledge/obsidian/sources/Anthropic Building Effective Agents.md:36`.

## Recap

ย้ำคำห้าคำ: เป้าหมาย ดู เลือก ทำ ตรวจ พร้อมขอบเขต “หยุดหรือถามคน” Evidence: `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:32`, `knowledge/obsidian/sources/OpenAI Practical Guide to Building AI Agents.md:36`.

## Takeaway

Agent ไม่ได้เก่งเพราะพูดเหมือนคน แต่เพราะรับผิดชอบเส้นทางบางส่วนเพื่อทำเป้าหมายให้สำเร็จ และ agent ที่ดีต้องรู้ขอบเขตของตัวเอง Evidence: `knowledge/obsidian/sources/Anthropic Building Effective Agents.md:32`, `knowledge/obsidian/sources/Anthropic Building Effective Agents.md:36`.

## Caveats

ไม่กล่าวว่า agent รับประกันความถูกต้อง เรียนรู้ถาวร มีสติ หรือตัดสินใจแทนมนุษย์ได้ทุกเรื่อง ไม่ผูกนิยามกับ framework หรือผู้ให้บริการรายเดียว
