import uvicorn 

if __name__ =="__main__":
    uvicorn .run ("src.main.server.server:app",host ="localhost",port =0000 ,reload =True )
    #inicia o servidor FastAPI usando Uvicorn, especificando o módulo e a aplicação a ser executada, além de configurar o host, porta e habilitar o modo de recarga automática para desenvolvimento.
