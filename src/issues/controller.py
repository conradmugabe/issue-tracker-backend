"""issues controller"""

from typing import TypedDict
from uuid import uuid4 as uuid

from fastapi import HTTPException


class CreateIssue(TypedDict):
    """create issue"""

    title: str


class Issue(CreateIssue):
    """issue"""

    id: str


class IssuesController:
    """issues controller"""

    def __init__(self):
        self.__issues: list[Issue] = []

    def create_issue(self, data: CreateIssue) -> Issue:
        """create issue"""
        issue: Issue = {"id": str(uuid()), "title": data.get("title")}
        self.__issues.append(issue)

        return issue

    def get_issue(self, issue_id: str) -> Issue:
        """get issue"""
        for issue in self.__issues:
            if issue["id"] == issue_id:
                return issue

        raise HTTPException(status_code=404, detail="Not found")
