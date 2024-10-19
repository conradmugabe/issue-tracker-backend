import unittest
from unittest.mock import MagicMock
from models.issues import IssueValidator
from models.issues import CreateIssue, Issue
from .service import (
    IssueService,
)


class TestIssueService(unittest.TestCase):

    def test_create_issue_success(self):
        storage_mock = MagicMock()
        id_generator_mock = MagicMock()

        cases = [
            {
                "name": "success",
                "args": {
                    "data": CreateIssue(title="Test issue"),
                },
                "prepare": lambda: self.prepare_provider(
                    id_generator_mock,
                    {
                        "get_pipeline_state": "123e4567-e89b-12d3-a456-426614174000",
                    },
                ),
                "after": lambda: self.post_assertions(
                    storage_mock,
                    {
                        "save_issue": [
                            Issue(
                                id="123e4567-e89b-12d3-a456-426614174000",
                                title="Test issue",
                            )
                        ],
                    },
                ),
                "expected": Issue(
                    id="123e4567-e89b-12d3-a456-426614174000", title="Test issue"
                ),
            },
            {
                "name": "invalid_create_issue",
                "input": CreateIssue(),
                "expected": True,  # Assuming always True for now
            },
        ]

        for case in cases:
            with self.subTest(case["name"]):
                case["prepare"]()

                service = IssueService(
                    storage_mock,
                    IssueValidator(),
                    id_generator_mock,
                )

                result = service.create_issue(case["input"])

                self.assertEqual(result, case["expected"])

                case["after"]()

    def prepare_provider(self, mock_provider, pairs):
        for method, return_value in pairs.items():
            mock_provider.configure_mock(
                **{method: MagicMock(return_value=return_value)}
            )

    def post_assertions(self, mock_service_provider, pairs):
        for method, args in pairs.items():
            getattr(mock_service_provider, method).assert_called_with(*args)


if __name__ == "__main__":
    unittest.main()
