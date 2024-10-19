"""Main service"""

from .issues import IssueService
from models.issues import CreateIssue, Issue, UpdateIssue, IssueQuery


class Service:
    """Main service"""

    issue_service: IssueService

    def __init__(self, issue_service: IssueService):
        self.issue_service = issue_service

    def create_issue(self, data: CreateIssue) -> Issue:
        """create issue"""
        return self.issue_service.create_issue(data)

    def get_issues(self, query: IssueQuery) -> list[Issue]:
        return self.issue_service.get_issues(query)

    def get_issue(self, issue_id: str) -> Issue | None:
        """get issue"""
        return self.get_issue(issue_id)

    def update_issue(self, issue_id: str, data: UpdateIssue) -> Issue | None:
        """update issue"""
        return self.issue_service.update_issue(issue_id, data)

    def delete_issue(self, issue_id: str) -> Issue | None:
        """delete issue"""
        return self.issue_service.delete_issue(issue_id)
