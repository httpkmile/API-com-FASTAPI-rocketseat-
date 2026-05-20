from src.models.repositories.interfaces.users_repository import UserRepositoryInterface
from src.controllers.interfaces.users_finder import UserFinderInterface


class UsersFinder(UserFinderInterface):
    def __init__(self, users_repository: UserRepositoryInterface):
        self.__users_repository = users_repository

    async def find_user_by_username(self, username: str) -> dict:
        user = await self.__users_repository.select_user_by_username(username)
        return {
            "type": "USER",
                "count": 1 if user else 0,
                "attributes": [user] if user else []
            }
        