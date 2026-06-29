# Repository Organization Standard

- Root documents define project-wide intent, governance, architecture, and operating policy.
- `docs/` holds decisions, proposals, research records, and design material.
- `blueprints/` describe planned capabilities; `contracts/` define module boundaries without implementation.
- `prompts/` contains versioned prompts by role only after evaluation requirements exist.
- `knowledge/`, `memory/`, and `evaluation/` keep source knowledge, retained context, and quality evidence separate.
- `apps/` contains deployable entry points; `packages/` contains reusable modules; `tests/` contains cross-module verification.
- New top-level directories require a distinct responsibility and an accepted architecture decision.
- Do not place business logic in documentation, prompts, generated artifacts, or catch-all utility folders.
