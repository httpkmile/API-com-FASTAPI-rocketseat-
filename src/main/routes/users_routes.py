from fastapi import APIRouter 
from fastapi .responses import JSONResponse 
from src .views .http_types .http_request import HttpRequest 
from src .validators .users_register_validator import UserInput 

from src .main .composer .user_finder_composer import user_finder_composer 
from src .main .composer .user_register_composer import user_register_composer 
from src .main .composer .user_delete_composer import user_delete_composer 

users_routers =APIRouter (tags =["USUARIOS"])

@users_routers .post ("/users")
async def create_user (body :UserInput ):
    http_request =HttpRequest (body =dict (body ))
    user_register =user_register_composer ()

    http_response =await user_register .handle_register_user (http_request )

    return JSONResponse (content =http_response .body ,status_code =http_response .status_code )

@users_routers .get ("/users/{username}")
async def get_by_user_for_username (username :str ):
    http_request =HttpRequest (path_params ={"username":username })
    user_finder =user_finder_composer ()

    response =await user_finder .handle_find_user_by_username (http_request )

    return JSONResponse (content =response .body ,status_code =response .status_code )

@users_routers .delete ("/users/{username}")
async def delete_user (username :str ):

    http_request =HttpRequest (path_params ={"username":username })
    user_delete =user_delete_composer ()

    response =await user_delete .handle_delete_user (http_request )

    return JSONResponse (content =response .body ,status_code =response .status_code )
