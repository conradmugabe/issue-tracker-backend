"""issues use cases"""

from entities.issue import CreateIssue, Issue
from storage.issues.db import IssueDatabaseService


class IssuesUseCases:
    """issues use cases"""

    def __init__(self, database_service: IssueDatabaseService) -> None:
        self._database_service = database_service

    def create(self, data: CreateIssue) -> Issue:
        """create issue"""
        # log user with id is creating issue
        issue = self._database_service.create(data)
        # log user has created an issue
        return issue

    def get_one(self, issue_id: str) -> Issue:
        """get one issue"""
        # log user with id is getting issue
        issue = self._database_service.get_one(issue_id)
        # log user has gotten an issue
        return issue
