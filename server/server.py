from fastapi import APIRouter
from server.http.handlers.issues.router import IssuesRouter
from server.http.handlers.users.router import UsersRouter


def combine_routers(
    issues_router: IssuesRouter,
    users_router: UsersRouter,
) -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(issues_router.get_router())
    api_router.include_router(users_router.get_router())
    return api_router
