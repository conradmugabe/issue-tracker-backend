"""entry point"""

from fastapi import FastAPI

from routers.issues.read_one import router as read_one_router
from routers.issues.create import router as create_issue_router
from routers.healthcheck.router import router as healthcheck_router

app = FastAPI()

app.include_router(healthcheck_router)
app.include_router(create_issue_router)
app.include_router(read_one_router)


@app.get("/healthcheck")
def healthcheck():
    """healthcheck"""
    return {"status": "ok"}
