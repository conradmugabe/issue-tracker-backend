"""Main service"""

from .issue_methods import IssueMethods
from .issue_create import IssueCreate
from models.issues import (
    Service,
    CreateIssue,
    Validator,
    Storage,
    Issue,
    IssueQuery,
    UpdateIssue,
)
from models.common import IdGenerator


class IssueService(Service):
    """Issue service"""

    issue_methods: IssueMethods
    issue_create: IssueCreate

    def __init__(
        self,
        issue_storage: Storage,
        issue_validator: Validator,
        uuid_generator: IdGenerator,
    ):
        self.issue_methods = IssueMethods(
            issue_storage, issue_validator, uuid_generator
        )
        self.issue_create = IssueCreate(issue_storage, issue_validator, uuid_generator)

    def create_issue(self, data: CreateIssue) -> Issue:
        """create issue"""
        return self.issue_create.create_issue(data)

    def get_issues(self, query: IssueQuery) -> list[Issue]:
        return self.issue_methods.get_issues(query)

    def get_issue(self, issue_id: str) -> Issue | None:
        """get issue"""
        return self.get_issue(issue_id)

    def update_issue(self, issue_id: str, data: UpdateIssue) -> Issue | None:
        """update issue"""
        return self.issue_methods.update_issue(issue_id, data)

    def delete_issue(self, issue_id: str) -> Issue | None:
        """delete issue"""
        return self.issue_methods.delete_issue(issue_id)
