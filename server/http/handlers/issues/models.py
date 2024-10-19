from pydantic import BaseModel


class CreateIssueRequest(BaseModel):
    """create issue request"""

    title: str


class UpdateIssueRequest(BaseModel):
    """update issue request"""

    id: str
    title: str | None = None
