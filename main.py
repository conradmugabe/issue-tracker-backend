"""entry point"""

from fastapi import FastAPI
from server.http.server import combine_routers
from server.http.handlers.issues.router import IssuesRouter
from server.http.handlers.users.router import UsersRouter
from service.issues import IssueService
from storage.in_memory import IssueStorage
from models.issues import IssueValidator
from models.common import UUIDGenerator
from models.users import Service as UsersService


app: FastAPI


def main() -> FastAPI:
    global app
    app = FastAPI()
    # Initialize uuid generator
    uuid_generator = UUIDGenerator()

    # Initialize issue storage
    issue_storage = IssueStorage()

    # Initialize issue validator
    issue_validator = IssueValidator()

    # Initialize the services
    issues_service = IssueService(
        storage=issue_storage,
        validator=issue_validator,
        id_generator=uuid_generator,
    )

    # Initialize the issue router
    issues_router = IssuesRouter(issue_service=issues_service)

    # do the same for users dependencies and the service
    # ...
    users_service = UsersService()

    # Initialize the user router
    users_router = UsersRouter(user_service=users_service)

    # Combine the routers
    app.include_router(combine_routers(issues_router, users_router))


# just an example of how to run the app
if __name__ == "__main__":
    import uvicorn

    # for flexibility to allow running as script or a wsgi
    main()

    uvicorn.run(app, host="127.0.0.1", port=8000)
