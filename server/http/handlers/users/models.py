from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    """create issue request"""

    title: str


class UpdateUserRequest(BaseModel):
    """update issue request"""

    id: str
    title: str | None = None
