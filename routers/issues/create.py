"""create issue router"""

from use_cases import issues_use_cases
from entities.issue import IssueStatus
from dto.issue import CreateIssue, Issue
from routers.issues.router import router


@router.post("/")
def create_issue(data: CreateIssue) -> Issue:
    """create issue"""

    issue = issues_use_cases.create(
        data={
            "title": data.title,
            "description": data.description,
            "assignees": data.assignees,
            "status": IssueStatus.OPEN,
        }
    )
    return issue
