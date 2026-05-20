    # FASTAPI - Projeto de Exemplo

    Este é um projeto de API web construído com FastAPI, organizado em camadas de modelo, controlador, visão e rotas. O objetivo é demonstrar um padrão de arquitetura claro, com validação de entrada, persistência em banco de dados SQLite assíncrono e rotas REST para cadastro e consulta de usuários.

    ## Visão geral do projeto

    - `src/main/server/server.py` - inicia a aplicação FastAPI e registra as rotas.
    - `src/main/routes/users_routes.py` - define os endpoints de criação e busca de usuários.
    - `src/main/composer/` - monta as dependências entre modelos, controladores e views.
    - `src/controllers/` - contém a lógica de negócios para registrar e buscar usuários.
    - `src/models/` - inclui entidades, repositórios e configuração do banco de dados.
    - `src/views/` - abstrai a conversão entre requisições HTTP internas e respostas.
    - `src/validators/` - valida os dados de entrada usando Pydantic.

    ## Como executar

    1. Instale as dependências listadas em `requirements.txt`.
    2. Execute o servidor com:

    ```bash
    python run.py
    ```

    ## Endpoints disponíveis

    - `POST /users` - cadastra um usuário.
    - `GET /users/{username}` - busca um usuário pelo nome de usuário.

    ## Visual da branch atual

    A branch ativa do repositório é:

    ```bash
    * main
    ```

    Estrutura de branches do projeto:

    ```text
    main    # branch principal com a implementação atual do projeto
    ```


