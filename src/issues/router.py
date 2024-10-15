"""issues router"""

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/api/v1/issues", tags=["issues"])


class CreateIssueRequest(BaseModel):
    """create issue request"""

    title: str


class UpdateIssueRequest(BaseModel):
    """update issue request"""

    title: str | None = None


@router.post("/issues")
def create_issue(data: CreateIssueRequest):
    """create issue"""
    return {"title": data.title, "id": 1}


@router.get("/issues")
def get_issues():
    """get issues"""
    return []


@router.get("/issues/{issue_id}")
def get_issue(issue_id: int):
    """get issue"""
    return {"id": issue_id}


@router.patch("/issues/{issue_id}")
def update_issue(issue_id: int, data: UpdateIssueRequest | None):
    """update issue"""
    if data.title is None:
        return {"id": issue_id}
    return {"id": issue_id, "title": data.title}


@router.delete("/issues/{issue_id}")
def delete_issue(issue_id: int):
    """delete issue"""
    return {"id": issue_id}
