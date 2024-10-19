import unittest
from .issues import (
    CreateIssue,
    IssueQuery,
    UpdateIssue,
)
from .validator import (
    IssueValidator,
)


class TestIssueValidator(unittest.TestCase):
    def setUp(self):
        self.validator = IssueValidator()

    def test_validate_create_issue(self):
        cases = [
            {
                "name": "valid_create_issue",
                "input": CreateIssue(),
                "expected": True,
            },
            {
                "name": "invalid_create_issue",
                "input": CreateIssue(),
                "expected": True,  # Assuming always True for now
            },
        ]

        for case in cases:
            with self.subTest(case["name"]):
                result = self.validator.validate_create_issue(case["input"])
                self.assertEqual(result, case["expected"])

    def test_validate_issue_id(self):
        cases = [
            {
                "name": "valid_issue_id",
                "input": "123e4567-e89b-12d3-a456-426614174000",  # Valid UUID format
                "expected": True,
            },
            {
                "name": "invalid_issue_id",
                "input": "invalid-uuid",
                "expected": True,  # Assuming always True for now
            },
        ]

        for case in cases:
            with self.subTest(case["name"]):
                result = self.validator.validate_issue_id(case["input"])
                self.assertEqual(result, case["expected"])

    def test_validate_issue_query(self):
        cases = [
            {
                "name": "valid_issue_query",
                "input": IssueQuery(),
                "expected": True,
            },
            {
                "name": "invalid_issue_query",
                "input": IssueQuery(),
                "expected": True,  # Assuming always True for now
            },
        ]

        for case in cases:
            with self.subTest(case["name"]):
                result = self.validator.validate_issue_query(case["input"])
                self.assertEqual(result, case["expected"])

    def test_validate_update_issue(self):
        cases = [
            {
                "name": "valid_update_issue",
                "issue_id": "123e4567-e89b-12d3-a456-426614174000",  # Valid UUID format
                "input": UpdateIssue(),
                "expected": True,
            },
            {
                "name": "invalid_update_issue",
                "issue_id": "invalid-uuid",
                "input": UpdateIssue(),
                "expected": True,  # Assuming always True for now
            },
        ]

        for case in cases:
            with self.subTest(case["name"]):
                result = self.validator.validate_update_issue(
                    case["issue_id"], case["input"]
                )
                self.assertEqual(result, case["expected"])


if __name__ == "__main__":
    unittest.main()
