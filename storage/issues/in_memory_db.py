"""in memory database service"""

from uuid import uuid4
from datetime import date as Date

from entities.issue import CreateIssue, Issue
from storage.issues.db import IssueDatabaseService


class TodoInMemoryDatabaseService(IssueDatabaseService):
    """In Memory Database Service"""

    def __init__(self, data: list[Issue] = None) -> None:
        if data is None:
            data = []
        self._data = data

    def create(self, data: CreateIssue) -> Issue:
        """saves issue to database"""
        print("data", data)
        issue: Issue = {
            "title": data.get("title"),
            "description": data["description"],
            "assignees": data["assignees"],
            "createdAt": Date.today(),
            "createdBy": "user_1",
            "id": str(uuid4()),
            "status": data["status"],
            "updatedAt": Date.today(),
        }
        self._data.append(issue)
        return issue

    def get_one(self, issue_id: str) -> Issue:
        """get an issue by id"""
        for issue in self._data:
            if issue["id"] == issue_id:
                return issue
        return None
