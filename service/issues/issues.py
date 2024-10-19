"""Issue service"""

from models.issues import (
    Service,
    Validator,
    Storage,
    Issue,
    IssueQuery,
    CreateIssue,
    UpdateIssue,
)
from models.common import IdGenerator


class IssueService(Service):
    """Issue service"""

    def __init__(
        self,
        storage: Storage,
        validator: Validator,
        id_generator: IdGenerator,
    ):
        self.storage = storage
        self.validator = validator
        self.id_generator = id_generator

    def create_issue(self, data: CreateIssue) -> Issue:
        """create issue"""
        valid = self.validator.validate_create_issue(data)
        if not valid:
            raise ValueError(
                "invalid issue data"
            )  # or handle in chosen error handling style

        issue = Issue()
        issue.id = self.id_generator.generate()
        issue.title = data.title

        self.storage.save_issue(issue)

        return issue

    def get_issues(self, query: IssueQuery) -> list[Issue]:
        """get issues"""
        valid = self.validator.validate_issue_query(query)
        if not valid:
            raise ValueError(
                "invalid issue query"
            )  # or handle in chosen error handling style

        return self.storage.get_issues(query)

    def get_issue(self, issue_id: str) -> Issue | None:
        """get issue"""
        valid = self.validator.validate_issue_id(issue_id)
        if not valid:
            raise ValueError(
                "invalid issue query"
            )  # or handle in chosen error handling style

        return self.storage.get_issue_by_id(issue_id)

    def update_issue(self, issue_id: str, data: UpdateIssue) -> Issue | None:
        """update issue"""
        valid = self.validator.validate_update_issue(issue_id, data)
        if not valid:
            raise ValueError("invalid update issue data")

        return self.storage.update_issue_by_id(issue_id, data)

    def delete_issue(self, issue_id: str) -> Issue | None:
        """delete issue"""
        valid = self.validator.validate_issue_id(issue_id)
        if not valid:
            raise ValueError(
                "invalid issue query"
            )  # or handle in chosen error handling style

        return self.storage.delete_issue_by_id(issue_id)
