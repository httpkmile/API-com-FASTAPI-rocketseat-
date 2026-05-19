from src.models.repositories.users_repository import UsersRepository
import pytest

@pytest.mark.skip(reason="testes de inserção e seleção de usuários")
@pytest.mark.asyncio
async def test_insert_user():
    
    new_user = {
        "username": "NomeDeTeste",
        "age": 99,
        "uf": "SP"
    }

    new_user2 = {
        "username": "NomeDeTeste2",
        "age": 100,
        "uf": "BA"
    }

    new_user3 = {
        "username": "NomeDeTeste",
        "age": 99,
        "uf": "SP"
    }

    repo = UsersRepository()

    await repo.insert_users(new_user)
    await repo.insert_users(new_user2)
    await repo.insert_users(new_user3)

@pytest.mark.asyncio
async def test_select_all_users():
    repo = UsersRepository()
    users = await repo.select_all_users("NomeDeTeste")
    print(users)