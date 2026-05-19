from src.models.settings.metadata import metadata
from sqlalchemy import Table, Column, Integer, String
# Importação do objeto metadata do módulo de configurações,
# que é usado para definir a estrutura do banco de dados e as tabelas

Users = Table(
    "users",  # Table name
    metadata,

    Column(
        "id",
        Integer,
        primary_key=True
    ),  # Column id of type integer, primary key

    Column(
        "username",
        String,
        nullable=False
    ),  # Column username of type string, cannot be null

    Column(
        "age",
        Integer,
        nullable=False,
        unique=True
    ),  # Column age of type integer, cannot be null and must be unique

    Column(
        "uf",
        String,
        nullable=False
    )  # Column uf of type string, cannot be null
)