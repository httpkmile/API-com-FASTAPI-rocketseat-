# pylint: disable=W0212
from sqlalchemy import insert, select
from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DatabaseConnectionHandler
from src.models.repositories.interfaces.users_repository import UserRepositoryInterface

class UsersRepository(UserRepositoryInterface):
    """Implementação do repositório de usuários usando SQLAlchemy."""

    async def insert_users(self, user_info: dict) -> None:
        async with DatabaseConnectionHandler() as db:
            query = insert(Users).values(**user_info)
            await db.execute(query)
            await db.commit()

    async def select_user_by_username(self, username: str) -> dict:
        async with DatabaseConnectionHandler() as db:
            # Consulta o usuário por username na tabela users
            query = select(Users).where(Users.c.username == username)

            result = await db.execute(query)
            rows = result.fetchall()

        users_list = [dict(row._mapping) for row in rows]
        
        # Retorna o primeiro usuário encontrado ou None se não existir
        return users_list[0] if users_list else None
