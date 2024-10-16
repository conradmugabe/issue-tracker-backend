"""issues controller"""

from typing import TypedDict

from fastapi import HTTPException

from src.issues.service import IssuesService


class UpdateIssue(TypedDict):
    """update issue"""

    title: str | None = None


class CreateIssue(TypedDict):
    """create issue"""

    title: str


class Issue(CreateIssue):
    """issue"""

    id: str


class IssueQuery(TypedDict):
    """issue query"""

    skip: int = None
    limit: int = None
    search: str = None


class IssuesController:
    """issues controller"""

    def __init__(self, service: IssuesService):
        self.__service = service

    def create_issue(self, data: CreateIssue) -> Issue:
        """create issue"""
        issue = self.__service.create_issue({"title": data.get("title")})

        return issue

    def get_issues(self, query: IssueQuery) -> list[Issue]:
        """get issues"""
        issues = self.__service.get_issues(query)

        return issues

    def get_issue(self, issue_id: str) -> Issue:
        """get issue"""
        issue = self.__service.get_issue(issue_id)
        if issue is None:
            raise HTTPException(status_code=404, detail="Not found")

        return issue

    def update_issue(self, issue_id: str, data: UpdateIssue) -> Issue:
        """update issue"""
        issue = self.__service.update_issue(
            issue_id=issue_id, data={"title": data.get("title")}
        )
        if issue is None:
            raise HTTPException(status_code=404, detail="Not found")

        return issue

    def delete_issue(self, issue_id: str) -> Issue:
        """delete issue"""
        issue = self.__service.delete_issue(issue_id)
        if issue is None:
            raise HTTPException(status_code=404, detail="Not found")

        return issue
