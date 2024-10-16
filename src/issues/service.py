"""issues service"""

from typing import TypedDict

from src.issues.storage.database_service import DatabaseService


class UpdateIssue(TypedDict):
    """update issue"""

    title: str | None = None


class CreateIssue(TypedDict):
    """create issue"""

    title: str


class Issue(CreateIssue):
    """issue"""

    id: str


class IssueQuery(TypedDict):
    """issue query"""

    skip: int = None
    limit: int = None
    search: str = None

    @classmethod
    def create(cls, skip: int = None, limit: int = None, search: str = None):
        """create issue query"""
        skip = 0 if skip is None else skip
        limit = 10 if limit is None else limit
        search = "" if search is None else search

        return IssueQuery(skip=skip, limit=limit, search=search)


class IssuesService:
    """issues service"""

    def __init__(self, database_service: DatabaseService):
        self.__database_service = database_service

    def create_issue(self, data: CreateIssue) -> Issue:
        """create issue"""
        issue = self.__database_service.save_issue({"title": data.get("title")})

        return issue

    def get_issues(self, query: IssueQuery) -> list[Issue]:
        """get issues"""
        query = IssueQuery.create(
            skip=query.get("skip"), limit=query.get("limit"), search=query.get("search")
        )

        issues = self.__database_service.get_issues(query)

        return issues

    def get_issue(self, issue_id: str) -> Issue | None:
        """get issue"""
        issue = self.__database_service.get_issue_by_id(issue_id)

        return issue

    def update_issue(self, issue_id: str, data: UpdateIssue) -> Issue | None:
        """update issue"""
        issue = self.__database_service.update_issue_by_id(
            issue_id, {"title": data.get("title")}
        )

        return issue

    def delete_issue(self, issue_id: str) -> Issue | None:
        """delete issue"""
        issue = self.__database_service.delete_issue_by_id(issue_id)

        return issue
