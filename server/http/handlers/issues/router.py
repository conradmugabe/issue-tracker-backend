"""issues router"""

from fastapi import APIRouter
from .models import CreateIssueRequest, UpdateIssueRequest
from models.issues import Service


class IssuesRouter:
    def __init__(self, issue_service: Service):
        self.router = APIRouter(prefix="/api/v1/issues", tags=["issues"])
        self.issue_service = issue_service
        self._register_routes()

    def _register_routes(self):
        @self.router.post("/")
        def create_issue(data: CreateIssueRequest):
            """create issue"""
            return self.issue_service.create_issue({"title": data.title})

        @self.router.get("/")
        def get_issues(skip: int = None, limit: int = None, search: str = None):
            """get issues"""
            return self.issue_service.get_issues(
                {"skip": skip, "limit": limit, "search": search}
            )

        @self.router.get("/{issue_id}")
        def get_issue(issue_id: str):
            """get issue"""
            return self.issue_service.get_issue(issue_id)

        @self.router.patch("/{issue_id}")
        def update_issue(issue_id: str, data: UpdateIssueRequest | None):
            """update issue"""
            return self.issue_service.update_issue(
                issue_id=issue_id, data={"title": data.title}
            )

        @self.router.delete("/{issue_id}")
        def delete_issue(issue_id: str):
            """delete issue"""
            return self.issue_service.delete_issue(issue_id)

    def get_router(self):
        return self.router
