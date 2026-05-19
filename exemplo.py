class ContextoSimples:

    def __enter__(self):  # Método chamado ao entrar no contexto
        print("Iniciando conexão com o banco de dados...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Método chamado ao sair do contexto,
        # independentemente de ocorrer uma exceção ou não
        print("Fechando conexão com o banco de dados com segurança...")


with ContextoSimples() as contexto:
    # Usando o contexto para realizar operações no banco de dados
    print("Executando operações no banco de dados!")