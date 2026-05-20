from src .models .repositories .users_repository import UsersRepository 
from src .controllers .users_delete import UsersDelete 
from src .views .user_delete_view import UsersDeleteView 
def user_delete_composer ():
    model =UsersRepository ()
    controller =UsersDelete (model )
    view =UsersDeleteView (controller )
    return view 
