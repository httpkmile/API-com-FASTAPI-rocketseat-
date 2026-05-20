from fastapi import APIRouter #importação do APIRouter para criar rotas específicas para usuários
from fastapi.responses import JSONResponse #importação do JSONResponse para retornar respostas em formato JSON
from src.views.http_types.http_request import HttpRequest #importação do HttpRequest para lidar com requisições HTTP
from src.validators.users_register_validator import UserInput #importação do UserInput para validar os dados de entrada do usuário  

from src.main.composer.user_finder_composer import user_finder_composer
from src.main.composer.user_register_composer import user_register_composer

users_routers = APIRouter(tags=["USUARIOS"])

@users_routers.post("/users")

async def criar_usuario(body: UserInput):
    http_request = HttpRequest(body=dict (body))
    user_register = user_register_composer()

    http_response = await user_register.handle_register_user(http_request)

    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@users_routers.get("/users/{username}")
async def obter_usuario_por_username(username: str):

    http_request = HttpRequest(path_params={"username": username})
    user_finder = user_finder_composer()
    response = await user_finder.handle_find_user_by_username(http_request)

    return JSONResponse(content=response.body, status_code=response.status_code)