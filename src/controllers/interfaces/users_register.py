from abc import ABC, abstractmethod

class UserRegisterInterface(ABC):
    """Interface para o controlador de cadastro de usuários."""

    @abstractmethod
    async def register_user(self, user_data: dict) -> dict:
        pass