"""Decide a blinded listener study from aggregate-only results."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

CONDITIONS = ("control", "personalized")
COUNT_FIELDS = (
    "assigned",
    "completed_immediate",
    "completed_delayed",
    "withdrawn",
    "artifact_factual_errors",
    "preference_responses",
    "preference_followed",
)


@dataclass(frozen=True)
class StudyDecision:
    status: str
    reasons: tuple[str, ...]


def decide(report: dict) -> StudyDecision:
    if not isinstance(report, dict):
        raise ValueError("report must be an object")
    reasons: list[str] = []
    for condition in CONDITIONS:
        values = report.get(condition)
        if not isinstance(values, dict):
            raise ValueError(f"{condition} aggregate is required")
        for field in COUNT_FIELDS:
            value = values.get(field)
            if type(value) is not int or value < 0:
                raise ValueError(f"{condition}.{field} must be a non-negative integer")
        for field in ("median_gain", "median_delayed"):
            if not isinstance(values.get(field), (int, float)):
                raise ValueError(f"{condition}.{field} must be numeric")
        assigned = values["assigned"]
        if values["completed_immediate"] > assigned or values["completed_delayed"] > assigned:
            raise ValueError(f"{condition} completions cannot exceed assigned")
        if values["withdrawn"] > assigned:
            raise ValueError(f"{condition} withdrawals cannot exceed assigned")
        if values["preference_followed"] > values["preference_responses"]:
            raise ValueError(f"{condition} preference_followed cannot exceed preference_responses")
        if values["preference_responses"] > values["completed_immediate"]:
            raise ValueError(f"{condition} preference_responses cannot exceed completed_immediate")
        if not -6 <= values["median_gain"] <= 6:
            raise ValueError(f"{condition}.median_gain must be between -6 and 6")
        if not 0 <= values["median_delayed"] <= 4:
            raise ValueError(f"{condition}.median_delayed must be between 0 and 4")

    control = report["control"]
    personalized = report["personalized"]
    if min(
        control["completed_immediate"],
        control["completed_delayed"],
        personalized["completed_immediate"],
        personalized["completed_delayed"],
    ) < 4:
        return StudyDecision("inconclusive", ("fewer than four completed listeners per condition",))

    if control["artifact_factual_errors"] or personalized["artifact_factual_errors"]:
        reasons.append("an artifact has a factual error")
    if personalized["median_gain"] < control["median_gain"] + 1:
        reasons.append("personalized median learning gain is less than one point above control")
    if personalized["median_delayed"] < control["median_delayed"]:
        reasons.append("personalized delayed recall is lower than control")
    responses = personalized["preference_responses"]
    if not responses or personalized["preference_followed"] / responses < 0.75:
        reasons.append("fewer than 75% report that the explicit preference was followed")
    return StudyDecision("fail" if reasons else "pass", tuple(reasons))


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python packages/evaluation/listener_study.py <aggregate-results.json>", file=sys.stderr)
        return 2
    try:
        report = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
        decision = decide(report)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(exc, file=sys.stderr)
        return 2
    print(decision.status)
    for reason in decision.reasons:
        print(f"- {reason}")
    return 0 if decision.status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
