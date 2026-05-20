from src.models.repositories.users_repository import UsersRepository
# AQUI: Importe a classe real, não a interface
from src.controllers.users_finder import UsersFinder 
from src.views.user_finder_view import UsersFinderView

def user_finder_composer():
    model = UsersRepository()
    # AQUI: Use a classe real
    controller = UsersFinder(model) 
    view = UsersFinderView(controller)
    return view
