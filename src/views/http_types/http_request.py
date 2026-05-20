class HttpRequest :
    """Representa uma requisição HTTP interna usada nas camadas da aplicação."""

    def __init__ (self ,
    headers :dict =None ,
    body :dict =None ,
    path_params :dict =None ,
    ):
        self .headers =headers 
        self .body =body 
        self .path_params =path_params 