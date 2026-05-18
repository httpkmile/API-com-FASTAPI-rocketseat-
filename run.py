import uvicorn #importação do Uvicorn, um servidor ASGI para rodar a aplicação FastAPI

if __name__ == "__main__": #funcao main para rodar a aplicação, verificando se o script está sendo executado diretamente
    uvicorn.run("src.main.server.server:app", host="127.0.0.1", port=8000,reload=True) 