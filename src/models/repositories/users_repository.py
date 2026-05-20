# pylint: disable=W0212

from sqlalchemy import insert, select
from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DatabaseConnectionHandler
from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface

class UsersRepository(UsersRepositoryInterface):

    async def insert_users(self, user_info: dict) -> None:
        async with DatabaseConnectionHandler() as db:
            query = insert(Users).values(**user_info)

            await db.execute(query)
            await db.commit()

    async def select_all_users(self, username: str) -> list[dict]:
        async with DatabaseConnectionHandler() as db:
            query = select(Users).where(Users.c.username == username)

            result = await db.execute(query)
            rows = result.fetchall()

        users_list = [dict(row._mapping) for row in rows]
        return users_list