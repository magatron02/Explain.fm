import sys
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))

from packages.evaluation.listener_study import decide


def passing_report() -> dict:
    return {
        "control": {
            "assigned": 4,
            "completed_immediate": 4,
            "completed_delayed": 4,
            "withdrawn": 0,
            "median_gain": 1,
            "median_delayed": 3,
            "artifact_factual_errors": 0,
            "preference_responses": 4,
            "preference_followed": 2,
        },
        "personalized": {
            "assigned": 4,
            "completed_immediate": 4,
            "completed_delayed": 4,
            "withdrawn": 0,
            "median_gain": 2,
            "median_delayed": 3,
            "artifact_factual_errors": 0,
            "preference_responses": 4,
            "preference_followed": 3,
        },
    }


class ListenerStudyTests(unittest.TestCase):
    def test_passing_aggregate_meets_every_gate(self):
        self.assertEqual(decide(passing_report()).status, "pass")

    def test_learning_gain_regression_fails(self):
        report = deepcopy(passing_report())
        report["personalized"]["median_gain"] = 1.5
        decision = decide(report)
        self.assertEqual(decision.status, "fail")
        self.assertIn("personalized median learning gain is less than one point above control", decision.reasons)

    def test_small_completed_cohort_is_inconclusive(self):
        report = deepcopy(passing_report())
        report["personalized"]["completed_delayed"] = 3
        self.assertEqual(decide(report).status, "inconclusive")

    def test_invalid_counts_are_rejected(self):
        report = deepcopy(passing_report())
        report["control"]["completed_immediate"] = 5
        with self.assertRaisesRegex(ValueError, "completions cannot exceed assigned"):
            decide(report)

    def test_report_must_be_an_object(self):
        with self.assertRaisesRegex(ValueError, "report must be an object"):
            decide([])

    def test_boolean_count_is_rejected(self):
        report = deepcopy(passing_report())
        report["control"]["assigned"] = True
        with self.assertRaisesRegex(ValueError, "must be a non-negative integer"):
            decide(report)

    def test_impossible_score_is_rejected(self):
        report = deepcopy(passing_report())
        report["personalized"]["median_delayed"] = 5
        with self.assertRaisesRegex(ValueError, "must be between 0 and 4"):
            decide(report)

    def test_preference_responses_cannot_exceed_completions(self):
        report = deepcopy(passing_report())
        report["personalized"]["preference_responses"] = 5
        with self.assertRaisesRegex(ValueError, "cannot exceed completed_immediate"):
            decide(report)


if __name__ == "__main__":
    unittest.main()
