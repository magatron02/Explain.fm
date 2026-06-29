# Research Briefs

A research brief converts accepted sources into bounded findings without adding unsupported claims.

## Required shape

- Frontmatter: `type: research-brief`, `status`, `question`, and `audience`.
- `## Findings`: one Markdown table row per claim.
- Evidence cells: one or more backtick citations in `repository/path.md:line` form.
- `## Disagreements and uncertainty` and `## Open questions` remain explicit, even when empty.

Validate a brief from the repository root:

```bash
python packages/research/brief.py docs/research/example.md
```

Only accepted source notes under `knowledge/obsidian/sources/` are valid evidence.
