from .interfaces import Validator
from .issues import CreateIssue, IssueQuery, UpdateIssue


class IssueValidator(Validator):
    """Issue validator service"""

    def validate_create_issue(self, data: CreateIssue) -> bool:
        """validate create issue"""
        return True

    def validate_issue_id(self, issue_id: str) -> bool:
        """validate issue id"""
        return True

    def validate_issue_query(self, query: IssueQuery) -> bool:
        """validate issue query"""
        return True

    def validate_update_issue(self, issue_id: str, data: UpdateIssue) -> bool:
        """validate update issue"""
        return True
