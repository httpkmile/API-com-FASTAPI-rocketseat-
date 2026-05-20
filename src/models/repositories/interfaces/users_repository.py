from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):

    @abstractmethod
    async def insert_users(self, user_info: dict) -> None: pass

    @abstractmethod
    async def select_user_by_username(self, username: str) -> dict: pass
 