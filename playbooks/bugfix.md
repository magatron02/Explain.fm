# Playbook: Bug Fix

1. Reproduce the failure and capture the smallest reliable evidence.
2. Identify the violated contract, invariant, or expected behavior.
3. Trace the earliest pipeline stage where the defect appears.
4. Fix the cause with the smallest bounded change.
5. Add a regression test or evaluation case.
6. Verify affected downstream artifacts and quality gates.
7. Record a failure pattern only if recurrence is established.

Do not hide a quality failure with retries, prompt wording, or downstream cleanup alone.
