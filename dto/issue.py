"""issue dto"""

from typing import Optional
from datetime import date as Date

from pydantic import BaseModel

from entities.issue import IssueStatus


class CreateIssue(BaseModel):
    """create issue model"""

    title: str
    description: str
    assignees: Optional[list[str]] = None


class Issue(BaseModel):
    """issue model"""

    id: str
    title: str
    description: str
    status: IssueStatus
    assignees: Optional[list[str]]
    createdAt: Date
    updatedAt: Date
    createdBy: str
