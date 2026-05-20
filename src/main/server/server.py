from fastapi import FastAPI  # Importa o FastAPI para criar a aplicação web
from src.main.routes.users_routes import users_routers  # Importa o roteador de usuários para registrar as rotas

app = FastAPI()
app.include_router(users_routers)  # Registra o roteador de usuários na aplicação FastAPI
