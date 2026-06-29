# Logging Standard

- Correlate events by episode, stage, artifact, and attempt identifiers.
- Record event name, timestamp, stage status, duration, configuration version, and error category where relevant.
- Log provenance references and quality-gate outcomes, not hidden model reasoning.
- Do not log secrets, raw listener data, or full copyrighted source content.
- Use structured fields and bounded payloads suitable for diagnosis.
- Make retries and partial results visible.

Logging implementation is deferred until runtime architecture is selected.
