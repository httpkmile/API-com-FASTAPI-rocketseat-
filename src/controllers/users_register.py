from src.models.repositories.interfaces.users_repository import (
    UserRepositoryInterface,
)
from src.controllers.interfaces.users_register import UserRegisterInterface

class UsersRegister(UserRegisterInterface):

    def __init__(
        self,
        users_repository: UserRepositoryInterface
    ) -> None:
        self.__users_repository = users_repository

    async def register_user(self, user_data: dict) -> dict:
        self.__validate_user_data(user_data)

        await self.__register_user(user_data)

        response = self.__format_response(user_data)

        return response

    def __validate_user_data(self, user_data: dict) -> None:
        age = user_data["age"]
        uf = user_data["uf"].upper()

        if uf not in ["SP", "RJ", "MG"]:
            raise Exception(
                "UF must be one of the following: SP, RJ, MG."
            )

        if age < 0 or age > 120:
            raise Exception(
                "Age must be between 0 and 120."
            )

    async def __register_user(self, user_data: dict) -> None:
        await self.__users_repository.insert_users(user_data)

    def __format_response(self, user_data: dict) -> dict:
        return {
            "type": "USERS",
            "count": 1,
            "attributes": user_data
        }