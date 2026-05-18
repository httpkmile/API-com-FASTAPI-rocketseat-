from fastapi import FastAPI #importação do FastAPI para criar a aplicação web e definir as rotas e endpoints da API
from src.main.routes.users_routes import users_routers #importação do roteador de usuários para incluir as rotas relacionadas a usuários na aplicação 

app = FastAPI() 
app.include_router(users_routers)