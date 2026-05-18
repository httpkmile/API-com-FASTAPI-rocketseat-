from fastapi import APIRouter #importação do APIRouter para criar rotas específicas para usuários
from fastapi.responses import JSONResponse #importação do JSONResponse para retornar respostas em formato JSON

users_routers = APIRouter(tags=["USUARIOS"])

@users_routers.post("/users")

async def criar_usuario():

    return JSONResponse(content={"message": "Usuário criado com sucesso!"}, status_code=201)
