"""issues in memory database service"""

from uuid import uuid4 as uuid

from src.issues.storage.database_service import (
    DatabaseService,
    SaveIssue,
    Issue,
    UpdateIssue,
    IssueQuery,
)


class IssuesInMemoryDatabaseService(DatabaseService):
    """issues in memory database service"""

    def __init__(self, issues: list[Issue] = None) -> None:
        self.__issues = [] if issues is None else issues

    def save_issue(self, data: SaveIssue) -> Issue:
        """save issue"""
        issue: Issue = {"id": str(uuid()), "title": data.get("title")}
        self.__issues.append(issue)

        return issue

    def get_issues(self, query: IssueQuery) -> list[Issue]:
        """get issues"""
        return []

    def get_issue_by_id(self, issue_id: str) -> Issue | None:
        """get issue by id"""
        for issue in self.__issues:
            if issue["id"] == issue_id:
                return issue

        return None

    def update_issue_by_id(self, issue_id: str, data: UpdateIssue) -> Issue | None:
        """update issue by id"""
        for index, issue in enumerate(self.__issues):
            if issue["id"] == issue_id:
                self.__issues[index] = {**issue, **data}
                return self.__issues[index]

        return None

    def delete_issue_by_id(self, issue_id: str) -> Issue | None:
        """delete issue by id"""
        for index, issue in enumerate(self.__issues):
            if issue["id"] == issue_id:
                del self.__issues[index]
                return issue

        return None
