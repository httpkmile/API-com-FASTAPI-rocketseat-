from src.models.repositories.users_repository import UsersRepository
from src.controllers.users_register import UsersRegister
from src.views.user_register_view import UserRegisterView

# Compor o fluxo de cadastro de usuário com modelo, controlador e visão
def user_register_composer():
    model = UsersRepository()
    controller = UsersRegister(model)
    view = UserRegisterView(controller)
    return view
