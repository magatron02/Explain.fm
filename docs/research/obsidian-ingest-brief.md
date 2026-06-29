---
type: research-brief
status: reviewed
question: "How should Explain.fm use Obsidian for source ingestion without weakening portability or provenance?"
audience: "Explain.fm engineering and research"
created: "2026-06-29"
---

# Obsidian Ingest Brief

## Scope

This brief covers source-note metadata and links inside the local knowledge workspace. It does not select synchronization, publishing, or graph-memory technology.

## Findings

| Claim | Evidence | Source quality | Uncertainty |
| --- | --- | --- | --- |
| Flat YAML properties are an appropriate native format for compact ingest metadata. | `knowledge/obsidian/sources/Obsidian Properties Documentation.md:35`<br>`knowledge/obsidian/sources/Obsidian Properties Documentation.md:36` | Primary product documentation | Explain.fm still owns schema validation and migrations. |
| The native Templates feature can apply and merge the source-note property set. | `knowledge/obsidian/sources/Obsidian Properties Documentation.md:34` | Primary product documentation | Template insertion does not prove that required values were completed correctly. |
| Internal links can connect source notes to files, headings, and blocks for human navigation. | `knowledge/obsidian/sources/Obsidian Internal Links Documentation.md:35` | Primary product documentation | Link existence alone does not prove claim support. |
| Machine provenance should not depend on Obsidian block references because they are not portable Markdown. | `knowledge/obsidian/sources/Obsidian Internal Links Documentation.md:36` | Primary product documentation | Repository `file:line` citations can drift when a source note is edited. |
| Automatic link updates can reduce broken human-navigation links when files are renamed. | `knowledge/obsidian/sources/Obsidian Internal Links Documentation.md:34` | Primary product documentation | Machine citations still require repository validation. |

## Disagreements and uncertainty

No disagreement appears between the two official pages. Both are first-party documentation and neither specifies a documentation-content license.

## Open questions

- When should stable source anchors replace line-number citations?
- Which source-note edits should require re-review of dependent briefs?
- Should accepted source notes become immutable records with superseding versions?

## Recommendation

Keep ingest metadata in flat YAML frontmatter, use Obsidian links for human navigation, and keep machine-enforced `file:line` citations independent of Obsidian-specific link behavior. Continue validating required values and accepted-source status in repository tests.
