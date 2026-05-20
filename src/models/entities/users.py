from src.models.settings.metadata import metadata
from sqlalchemy import Table, Column, Integer, String
# Importação do objeto metadata do módulo de configurações,
# usado para definir a estrutura de tabelas do banco de dados.

Users = Table(
    "users",  # Nome da tabela no banco de dados
    metadata,

    Column(
        "id",
        Integer,
        primary_key=True
    ),  # Coluna id do tipo inteiro e chave primária.

    Column(
        "username",
        String,
        nullable=False
    ),  # Coluna username obrigatória do tipo string.

    Column(
        "age",
        Integer,
        nullable=False,
        
    ),  # Coluna age obrigatória do tipo inteiro.

    Column(
        "uf",
        String,
        nullable=False
    )  # Coluna uf obrigatória do tipo string.
)