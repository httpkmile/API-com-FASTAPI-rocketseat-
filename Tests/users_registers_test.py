import pytest 

from src .controllers .users_register import UsersRegister 

class UserRepositoryMock :

    def __init__ (self ):
        self .insert_users_att ={}

    async def insert_users (self ,user_data :dict ):
        self .insert_users_att ["user_data"]=user_data 


@pytest .mark .asyncio 
async def test_register_user ():
    users_repository =UserRepositoryMock ()

    users_register =UsersRegister (users_repository )

    user_data ={
    "username":"test_user",
    "age":30 ,
    "uf":"SP"
    }

    response =await users_register .register_user (user_data )

    print (response )

    assert users_repository .insert_users_att ["user_data"]==user_data 

    assert response ["type"]=="USERS"
    assert response ["count"]==1 
    assert response ["attributes"]==user_data 

