import pytest
from src.controllers.users_finder import UsersFinder

class UserRepositoryMock:
    def __init__(self):
        # Atributo que armazena o que foi passado no teste
        self.finder_users_att = {}

    # Corrigido: Nome igual ao que o Controller chama e apenas 1 argumento (username)
    async def select_user_by_username(self, username: str) -> dict:
        # Armazenamos o que foi buscado
        self.finder_users_att = {
            "username": username
        }
        
        # Retornamos um dicionário simulando o banco de dados
        return {
            "username": username,
            "age": 99,
            "uf": "SP"
        }

@pytest.mark.asyncio
async def test_finder_user():
    # 1. Preparação
    username_teste = "NomeDeTeste"
    
    mock_repo = UserRepositoryMock()
    controller = UsersFinder(mock_repo)
    
    # 2. Execução
    # Corrigido: Nome do método real do seu Controller
    response = await controller.find_user_by_username(username_teste)  
    
    # 3. Verificação
    print(f"Dados capturados pelo Mock: {mock_repo.finder_users_att}")
    
    # Asserts corrigidos para a estrutura "envelopada" do seu Controller
    # (type, count, attributes)
    assert response["type"] == "USER"
    assert response["count"] == 1
    assert response["attributes"][0]["username"] == username_teste
    assert response["attributes"][0]["age"] == 99
