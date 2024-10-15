"""issues service"""

from typing import TypedDict
from uuid import uuid4 as uuid


class UpdateIssue(TypedDict):
    """update issue"""

    title: str | None = None


class CreateIssue(TypedDict):
    """create issue"""

    title: str


class Issue(CreateIssue):
    """issue"""

    id: str


class IssuesService:
    """issues service"""

    def __init__(self):
        self.__issues: list[Issue] = []

    def create_issue(self, data: CreateIssue) -> Issue:
        """create issue"""
        issue: Issue = {"id": str(uuid()), "title": data.get("title")}
        self.__issues.append(issue)

        return issue

    def get_issue(self, issue_id: str) -> Issue | None:
        """get issue"""
        for issue in self.__issues:
            if issue["id"] == issue_id:
                return issue

        return None

    def update_issue(self, issue_id: str, data: UpdateIssue) -> Issue | None:
        """update issue"""
        for index, issue in enumerate(self.__issues):
            if issue["id"] == issue_id:
                self.__issues[index] = {**issue, **data}
                return self.__issues[index]

        return None

    def delete_issue(self, issue_id: str) -> Issue | None:
        """delete issue"""
        for index, issue in enumerate(self.__issues):
            if issue["id"] == issue_id:
                del self.__issues[index]
                return issue

        return None
