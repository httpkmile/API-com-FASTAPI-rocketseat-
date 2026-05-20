#pylint: disable=C0116
from fastapi import APIRouter  # APIRouter para criar rotas agrupadas de usuários
from fastapi.responses import JSONResponse  # Retorna respostas formatadas em JSON
from src.views.http_types.http_request import HttpRequest  # Objeto de requisição HTTP para o fluxo da aplicação
from src.validators.users_register_validator import UserInput  # Validador dos dados de cadastro de usuário

from src.main.composer.user_finder_composer import user_finder_composer
from src.main.composer.user_register_composer import user_register_composer
from src.main.composer.user_delete_composer import user_delete_composer

users_routers = APIRouter(tags=["USUARIOS"])  # Roteador de endpoints relacionados a usuários

@users_routers.post("/users")
async def create_user(body: UserInput):
    # Cria o objeto HttpRequest a partir dos dados validados pelo Pydantic
    http_request = HttpRequest(body=dict(body))
    user_register = user_register_composer()

    # Executa o fluxo de cadastro e retorna o HttpResponse resultante
    http_response = await user_register.handle_register_user(http_request)

    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@users_routers.get("/users/{username}")
async def get_by_user_for_username(username: str):
    # Cria o objeto HttpRequest para consulta usando parâmetros de rota
    http_request = HttpRequest(path_params={"username": username})
    user_finder = user_finder_composer()

    # Executa o fluxo de busca de usuário e retorna o HttpResponse
    response = await user_finder.handle_find_user_by_username(http_request)

    return JSONResponse(content=response.body, status_code=response.status_code)

@users_routers.delete("/users/{username}")
async def delete_user(username: str):
    
    http_request = HttpRequest(path_params={"username": username})
    user_delete = user_delete_composer()

    # Executa o fluxo de deleção de usuário e retorna o HttpResponse
    response = await user_delete.handle_delete_user(http_request)

    return JSONResponse(content=response.body, status_code=response.status_code)