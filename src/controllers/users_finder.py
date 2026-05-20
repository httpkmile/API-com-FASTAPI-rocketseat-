from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface

class UsersFinder:
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repository = users_repository

    async def find_users_by_username(self, username: str) -> dict:
        users = await self.__users_repository.select_all_users(username)
        return {
            "type": "USERS",
                "count": len(users),
                "attributes": users
            }