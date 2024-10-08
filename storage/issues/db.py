"""issues database service"""

from abc import ABC, abstractmethod

from entities.issue import Issue, CreateIssue


class IssueDatabaseService(ABC):
    """issue database service"""

    @abstractmethod
    def create(self, data: CreateIssue) -> Issue:
        """create issue"""

    @abstractmethod
    def get_one(self, issue_id: str) -> Issue:
        """get one issue"""
