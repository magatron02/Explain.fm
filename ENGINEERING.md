# Engineering Principles

- Build the smallest end-to-end slice that can test a product assumption.
- Keep retrieval, reasoning, storytelling, voice, and evaluation separate.
- Preserve provenance across every transformation.
- Prefer explicit contracts and observable outputs over hidden agent behavior.
- Add dependencies only for a demonstrated need.
- Make failure visible; do not silently downgrade quality.
- Test at boundaries where information can be lost, altered, or fabricated.
- Record durable technical choices as ADRs.

No production stack is selected in Era 0. Architecture choices require evidence from the target slice, not speculative scale.
