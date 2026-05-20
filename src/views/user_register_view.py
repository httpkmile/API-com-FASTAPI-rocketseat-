from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.users_register import UserRegisterInterface

class UserRegisterView:
    """Visão responsável por orquestrar o fluxo de cadastro de usuário."""

    def __init__(self, controller: UserRegisterInterface) -> None:
        self.controller = controller

    async def handle_register_user(self, http_request: HttpRequest) -> HttpResponse:
        # Extrai os dados do corpo da requisição HTTP
        user_data = http_request.body

        # Chama o controlador para processar o cadastro
        response = await self.controller.register_user(user_data)

        return HttpResponse(body=response, status_code=201) 