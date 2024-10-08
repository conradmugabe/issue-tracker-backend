"""issue entity"""

from enum import Enum
from datetime import date as Date
from typing import Optional, TypedDict

__all__ = ["CreateIssue", "Issue"]


class IssueStatus(str, Enum):
    """issue status enum"""

    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    CLOSED = "CLOSED"


class CreateIssue(TypedDict):
    """create issue model"""

    title: str
    description: str
    assignees: Optional[list[str]] = None
    status: IssueStatus.OPEN


class Issue(TypedDict):
    """issue model"""

    id: str
    title: str
    description: str
    status: IssueStatus
    assignees: Optional[list[str]]
    createdAt: Date
    updatedAt: Date
    createdBy: str
