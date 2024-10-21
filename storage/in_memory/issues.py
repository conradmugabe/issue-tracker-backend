"""issues in memory database service"""

from models.issues import (
    Storage,
    Issue,
    IssueQuery,
    UpdateIssue,
)


class IssueStorage(Storage):
    """Issues in memory database service"""

    def __init__(self) -> "IssueStorage":
        self.__issues = []

    def save_issue(self, issue: Issue):
        """save issue"""
        self.__issues.append(issue)

    def get_issues(self, query: IssueQuery) -> list[Issue]:
        """get issues"""
        skip = query.get("skip")
        limit = query.get("limit")
        search = query.get("search")
        queried_issues = self.__issues

        if search:
            queried_issues = [
                issue for issue in queried_issues if search in issue.get("title")
            ]

        s = skip
        e = skip + limit

        return queried_issues[s:e]

    def get_issue_by_id(self, issue_id: str) -> Issue | None:
        """get issue by id"""
        for issue in self.__issues:
            if issue["id"] == issue_id:
                return issue

        raise FileNotFoundError(
            f"issue with id {issue_id} not found"
        )  # or handle in chosen error handling style

    def update_issue_by_id(self, issue_id: str, data: UpdateIssue):
        """update issue by id"""
        for index, issue in enumerate(self.__issues):
            if issue["id"] == issue_id:
                self.__issues[index] = {**issue, **data}
                return None

        raise FileNotFoundError(
            f"issue with id {issue_id} not found"
        )  # or handle in chosen error handling style

    def delete_issue_by_id(self, issue_id: str):
        """delete issue by id"""
        for index, issue in enumerate(self.__issues):
            if issue["id"] == issue_id:
                del self.__issues[index]
                return None

        raise FileNotFoundError(
            f"issue with id {issue_id} not found"
        )  # or handle in chosen error handling style
