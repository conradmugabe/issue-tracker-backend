"""issues controller"""

from typing import TypedDict
from uuid import uuid4 as uuid


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
        issue: Issue = {"id": uuid(), "title": data.get("title")}
        self.__issues.append(issue)

        return issue
