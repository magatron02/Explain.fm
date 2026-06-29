# Obsidian Knowledge

The repository root is the Explain.fm Obsidian vault. This directory is the human-readable ingest workspace.

## Structure

- `inbox/` — candidate sources awaiting review.
- `sources/` — accepted source notes with complete provenance.
- `templates/source.md` — native Obsidian template for one source.
- `../raw/` — original permitted files or captures; never cleaned in place.
- `../topics/`, `../examples/`, `../analogies/`, `../mental-models/` — curated knowledge derived from accepted sources.

## Ingest workflow

1. Create a note in `inbox/` from `templates/source.md`.
2. Fill in provenance, authority, usage rights, scope, and limitations.
3. Put any permitted original artifact in `knowledge/raw/` and link it from the note.
4. Apply `playbooks/new-source.md`; reject unsupported or unusable material.
5. Move an accepted note to `sources/`, then create linked derived notes in the appropriate knowledge folders.

Do not store raw HTML, ads, cookie banners, navigation, duplicate content, or extraction noise. Local `.obsidian/` settings remain excluded from Git.
