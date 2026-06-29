# Evaluation Contract

## Purpose

Define consistent quality assessment across pipeline artifacts and completed episodes.

## Inputs

An identified artifact, its provenance and upstream references, a versioned rubric, and reviewer or evaluator context.

## Outputs

A report with criterion-level scores or judgments, supporting observations, critical failures, pass state, rubric version, and actionable remediation targets.

## Dependencies

Versioned quality rubrics, inspectable pipeline artifacts, provenance records, benchmark expectations, and qualified reviewer or evaluator context.

## Success criteria

The report is reproducible enough to audit, identifies every critical failure, gates accuracy and source quality independently, and routes actionable findings to the responsible stage.

## Invariants

- Accuracy and source quality are independent gates.
- Every judgment includes inspectable evidence or rationale.
- Aggregate scores cannot conceal constitutional violations.
- Evaluation output identifies the artifact and versions assessed.

## Failure behavior

Mark the evaluation invalid or incomplete when required artifacts, evidence, or rubric information is absent. Do not infer a passing result from missing data.

Scoring scales and automation choices are intentionally deferred to evaluated rubrics.
