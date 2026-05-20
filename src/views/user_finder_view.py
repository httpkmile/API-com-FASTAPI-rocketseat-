from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.users_finder import UserFinderInterface

class UsersFinderView:
    """Visão responsável por orquestrar a resposta de busca de usuário."""

    def __init__(self, controller: UserFinderInterface) -> None:
        self.controller = controller

    async def handle_find_user_by_username(self, http_request: HttpRequest) -> HttpResponse:
        # Extrai o parâmetro de rota username da requisição HTTP
        user_data = http_request.path_params["username"]
        response = await self.controller.find_user_by_username(user_data)
        return HttpResponse(body=response, status_code=200)
    