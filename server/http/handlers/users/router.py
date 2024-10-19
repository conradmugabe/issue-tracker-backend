"""Users router"""

from fastapi import APIRouter
from models.users import Service  # Assuming you have a similar Service for users
from .models import CreateUserRequest, UpdateUserRequest


class UsersRouter:
    def __init__(self, user_service: Service):
        self.router = APIRouter(prefix="/api/v1/users", tags=["users"])
        self.user_service = user_service
        self._register_routes()

    def _register_routes(self):
        @self.router.post("/")
        def create_user(data: CreateUserRequest):
            """create user"""
            return self.user_service.create_user({"name": data.name})

        @self.router.get("/")
        def get_users(skip: int = None, limit: int = None, search: str = None):
            """get users"""
            return self.user_service.get_users(
                {"skip": skip, "limit": limit, "search": search}
            )

        @self.router.get("/{user_id}")
        def get_user(user_id: str):
            """get user"""
            return self.user_service.get_user(user_id)

        @self.router.patch("/{user_id}")
        def update_user(user_id: str, data: UpdateUserRequest | None):
            """update user"""
            return self.user_service.update_user(
                user_id=user_id, data={"name": data.name}
            )

        @self.router.delete("/{user_id}")
        def delete_user(user_id: str):
            """delete user"""
            return self.user_service.delete_user(user_id)

    def get_router(self):
        return self.router
