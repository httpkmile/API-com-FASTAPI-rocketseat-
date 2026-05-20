from abc import ABC ,abstractmethod 

class UserFinderInterface (ABC ):
    """Interface para o controlador de busca de usuários."""

    @abstractmethod 
    async def find_user_by_username (self ,username :str )->dict :
        pass 