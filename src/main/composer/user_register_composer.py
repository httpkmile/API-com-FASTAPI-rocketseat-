from src.models.repositories.users_repository import UsersRepository
from src.controllers.users_register import UsersRegister
from src.views.user_register_view import UserRegisterView

def user_register_composer(): #mvc formulando e completo
    model = UsersRepository()
    controller = UsersRegister(model)
    view = UserRegisterView(controller)
    return view 