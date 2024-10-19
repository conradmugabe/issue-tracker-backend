import abc
from .issues import CreateIssue, Issue, UpdateIssue, IssueQuery


class Service(abc.ABC):
    """Issue service contract"""

    @abc.abstractmethod
    def create_issue(self, data: CreateIssue) -> Issue:
        """create issue"""

    @abc.abstractmethod
    def get_issues(self, query: IssueQuery) -> list[Issue]:
        """get issues"""

    @abc.abstractmethod
    def get_issue(self, issue_id: str) -> Issue | None:
        """get issue"""

    @abc.abstractmethod
    def update_issue(self, issue_id: str, data: UpdateIssue) -> Issue | None:
        """update issue"""

    @abc.abstractmethod
    def delete_issue(self, issue_id: str) -> Issue | None:
        """delete issue"""


class Validator(abc.ABC):
    """Issue validator service contract"""

    @abc.abstractmethod
    def validate_create_issue(self, data: CreateIssue) -> bool:
        """validate create issue"""

    @abc.abstractmethod
    def validate_issue_id(self, issue_id: str) -> bool:
        """validate issue id"""

    @abc.abstractmethod
    def validate_issue_query(self, query: IssueQuery) -> bool:
        """validate issue query"""

    @abc.abstractmethod
    def validate_update_issue(self, issue_id: str, data: UpdateIssue) -> bool:
        """validate update issue"""


class Storage(abc.ABC):
    """Issue storage service contract"""

    @abc.abstractmethod
    def save_issue(self, issue: Issue):
        """Save issue"""

    @abc.abstractmethod
    def get_issues(self, query: IssueQuery) -> list[Issue]:
        """Get issues"""

    @abc.abstractmethod
    def get_issue_by_id(self, issue_id: str) -> Issue | None:
        """Get issue by id"""

    @abc.abstractmethod
    def update_issue_by_id(self, issue_id: str, data: Issue):
        """Update issue by id"""

    @abc.abstractmethod
    def delete_issue_by_id(self, issue_id: str):
        """Delete issue by id"""
