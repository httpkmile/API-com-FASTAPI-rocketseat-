from src.models.repositories.interfaces.users_repository import UserRepositoryInterface
from src.controllers.interfaces.users_delete import UserDeleteInterface

class UsersDelete(UserDeleteInterface):
    """Classe de controle responsável por deletar usuários."""

    def __init__(self, users_repository: UserRepositoryInterface):
        self.__users_repository = users_repository

    async def delete_user(self, username: str) -> dict:
        # Deleta o usuário pelo username no repositório
        deleted = await self.__users_repository.delete_user_by_username(username)
        return {
            "type": "USER",
            "deleted": deleted
        }
    
    