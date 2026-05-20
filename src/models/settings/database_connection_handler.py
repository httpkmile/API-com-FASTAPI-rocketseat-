from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event

# Connection string for an SQLite database using the aiosqlite driver
CONNECTION_STRING = "sqlite+aiosqlite:///schema.db"

# Setting up the asynchronous engine and sessionmaker
engine = create_async_engine(
    CONNECTION_STRING,
    echo=False,
    # O SQLite usa StaticPool por padrão, aumentamos o timeout para evitar travas
    connect_args={"timeout": 30} 
)

# Variable to create asynchronous sessions
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)




@event.listens_for(engine.sync_engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA journal_mode=WAL;")  # Habilita o modo WAL para melhor concorrência
    cursor.execute("PRAGMA synchronous=NORMAL;")  # Reduz a sincronização para melhorar o desempenho
    cursor.close()

    
class DatabaseConnectionHandler:
    """
    Class to handle database connections using asynchronous
    context management.
    """

    def __init__(self) -> None:
        """
        Initialization of the DatabaseConnectionHandler class.
        """
        self.session: Optional[AsyncSession] = None

    async def __aenter__(self) -> AsyncSession:
        """
        Called when entering the asynchronous context.
        """
        self.session = async_session()
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Called when exiting the asynchronous context.
        """
        if self.session:
            await self.session.close()