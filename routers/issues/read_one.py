"""read issue by id router"""

from dto.issue import Issue
from use_cases import issues_use_cases
from routers.issues.router import router


@router.get("/{issue_id}")
def create_issue(issue_id: str) -> Issue:
    """read issue by id"""

    issue = issues_use_cases.get_one(issue_id=issue_id)
    return issue
