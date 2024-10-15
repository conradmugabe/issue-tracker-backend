"""http server"""

from fastapi import FastAPI

from src.issues.router import router as issues_router

app = FastAPI()

app.include_router(issues_router)
