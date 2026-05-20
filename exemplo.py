class ContextoSimples :

    def __enter__ (self ):
        print ("Iniciando conexão com o banco de dados...")
        return self 

    def __exit__ (self ,exc_type ,exc_val ,exc_tb ):
        print ("Fechando conexão com o banco de dados com segurança...")


with ContextoSimples ()as contexto :
    print ("Executando operações no banco de dados!")