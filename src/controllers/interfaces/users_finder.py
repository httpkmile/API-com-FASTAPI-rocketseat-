from abc import ABC, abstractmethod

class UserFinderInterface(ABC):

    @abstractmethod
    async def find_user_by_username(self, username: str) -> dict:
        pass