from src .models .repositories .users_repository import UsersRepository 
from src .controllers .users_finder import UsersFinder 
from src .views .user_finder_view import UsersFinderView 
def user_finder_composer ():
    model =UsersRepository ()
    controller =UsersFinder (model )
    view =UsersFinderView (controller )
    return view 
