"""issues router"""

from fastapi import APIRouter
from pydantic import BaseModel

from src.issues.service import IssuesService
from src.issues.controller import IssuesController
from src.issues.storage.in_memory_database_service import IssuesInMemoryDatabaseService


database_service = IssuesInMemoryDatabaseService()
issues_service = IssuesService(database_service)
issues_controller = IssuesController(service=issues_service)
router = APIRouter(prefix="/api/v1/issues", tags=["issues"])


class CreateIssueRequest(BaseModel):
    """create issue request"""

    title: str


class UpdateIssueRequest(BaseModel):
    """update issue request"""

    title: str | None = None


@router.post("/")
def create_issue(data: CreateIssueRequest):
    """create issue"""
    return issues_controller.create_issue({"title": data.title})


@router.get("/")
def get_issues(skip: int = None, limit: int = None, search: str = None):
    """get issues"""
    return issues_controller.get_issues(
        {"skip": skip, "limit": limit, "search": search}
    )


@router.get("/{issue_id}")
def get_issue(issue_id: str):
    """get issue"""
    return issues_controller.get_issue(issue_id)


@router.patch("/{issue_id}")
def update_issue(issue_id: str, data: UpdateIssueRequest | None):
    """update issue"""
    return issues_controller.update_issue(issue_id=issue_id, data={"title": data.title})


@router.delete("/{issue_id}")
def delete_issue(issue_id: str):
    """delete issue"""
    return issues_controller.delete_issue(issue_id)
