from src.models.repositories.users_repository import UsersRepository
from src.controllers.users_register import UsersRegister
from src.views.user_register_view import UserRegisterView
# compor o fluxo de registro de usuário com modelo, controlador e visão
def user_register_composer():
    model = UsersRepository() #erro de importação, corrigir o nome da classe do controlador
    controller = UsersRegister(model)
    view = UserRegisterView(controller)
    return view
