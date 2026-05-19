import pytest
from ..src.models.settings.database_connection_handler import DatabaseConnectionHandler

@pytest.mark.asyncio
async def test_connection():

    async with DatabaseConnectionHandler() as session:
        print(session)

        assert session is not None  