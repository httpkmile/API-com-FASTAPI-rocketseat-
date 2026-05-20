#pylint: disable=C0114,C0115,C0116
from abc import ABC, abstractmethod

class UserDeleteInterface(ABC):
    """Interface para o controlador de deleção de usuários."""

    @abstractmethod
    async def delete_user(self, user_data: dict) -> dict:
        pass