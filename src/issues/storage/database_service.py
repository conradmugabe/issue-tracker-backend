"""issues database service"""

from typing import TypedDict
from abc import ABC, abstractmethod


class SaveIssue(TypedDict):
    """save issue"""

    title: str


class UpdateIssue(TypedDict):
    """update issue"""

    title: str | None = None


class Issue(TypedDict):
    """issue"""

    id: str
    title: str


class DatabaseService(ABC):
    """database service"""

    @abstractmethod
    def save_issue(self, data: SaveIssue) -> Issue:
        """save issue"""

    @abstractmethod
    def get_issue_by_id(self, issue_id: str) -> Issue | None:
        """get issue by id"""

    @abstractmethod
    def update_issue_by_id(self, issue_id: str, data: UpdateIssue) -> Issue | None:
        """update issue by id"""

    @abstractmethod
    def delete_issue_by_id(self, issue_id: str) -> Issue | None:
        """delete issue by id"""
