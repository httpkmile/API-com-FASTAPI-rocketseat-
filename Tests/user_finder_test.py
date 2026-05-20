import pytest 
from src .controllers .users_finder import UsersFinder 

class UserRepositoryMock :
    def __init__ (self ):
        self .finder_users_att ={}

    async def select_user_by_username (self ,username :str )->dict :
        self .finder_users_att ={
        "username":username 
        }

        return {
        "username":username ,
        "age":99 ,
        "uf":"SP"
        }

@pytest .mark .asyncio 
async def test_finder_user ():
    username_teste ="NomeDeTeste"

    mock_repo =UserRepositoryMock ()
    controller =UsersFinder (mock_repo )

    response =await controller .find_user_by_username (username_teste )

    print (f"Dados capturados pelo Mock: {mock_repo .finder_users_att }")

    assert response ["type"]=="USER"
    assert response ["count"]==1 
    assert response ["attributes"][0 ]["username"]==username_teste 
    assert response ["attributes"][0 ]["age"]==99 
