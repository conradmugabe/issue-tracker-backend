"""healthcheck router"""

from fastapi import APIRouter


router = APIRouter(prefix="/api/v1/issues", tags=["issues"])


@router.get("/healthcheck")
def healthcheck():
    """healthcheck"""
    return {"status": "ok"}
