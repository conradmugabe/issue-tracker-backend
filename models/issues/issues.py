from dataclasses import dataclass
from models.common import Pagination, Search


@dataclass
class CreateIssue:
    """Create issue data"""

    title: str


class UpdateIssue:
    """Update issue data"""

    title: str


class Issue:
    """Issue"""

    id: str
    title: str


class IssueQuery:
    """Issue query"""

    pagination: Pagination
    search: Search
