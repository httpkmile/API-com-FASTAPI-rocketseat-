from src.models.repositories.interfaces.users_repository import (
    UserRepositoryInterface,
)
from src.controllers.interfaces.users_register import UserRegisterInterface

class UsersRegister(UserRegisterInterface):
    """Classe de controle responsável pelo cadastro de usuários."""

    def __init__(
        self,
        users_repository: UserRepositoryInterface
    ) -> None:
        self.__users_repository = users_repository

    async def register_user(self, user_data: dict) -> dict:
        # Valida os dados do usuário antes de persistir no banco
        self.__validate_user_data(user_data)

        # Insere o usuário no repositório de dados
        await self.__register_user(user_data)

        # Prepara a resposta que será devolvida à camada de apresentação
        response = self.__format_response(user_data)

        return response

    def __validate_user_data(self, user_data: dict) -> None:
        age = user_data["age"]
        uf = user_data["uf"].upper()

        if uf not in ["SP", "RJ", "MG"]:
            raise Exception(
                "UF deve ser uma das seguintes: SP, RJ, MG."
            )

        if age < 0 or age > 120:
            raise Exception(
                "A idade deve estar entre 0 e 120."
            )

    async def __register_user(self, user_data: dict) -> None:
        await self.__users_repository.insert_users(user_data)

    def __format_response(self, user_data: dict) -> dict:
        return {
            "type": "USERS",
            "count": 1,
            "attributes": user_data
        }