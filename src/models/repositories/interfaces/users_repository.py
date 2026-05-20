from abc import ABC, abstractmethod

class UsersRepositoryInterface(ABC):

    @abstractmethod
    async def insert_users(self, user_info: dict) -> None: pass

    @abstractmethod
    async def select_all_users(self, username: str) -> list[dict]: pass
 