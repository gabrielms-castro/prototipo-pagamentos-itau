import requests

from src.dataclasses.http_methods import HttpMethods
from src.entities.store import Store


class AuthenticationService:

    def __init__(self, store: Store):
        self.store = store
    
    def send_request(self, method: HttpMethods, key: str) -> requests.Response:
        # key deve ser a concatenação de PV:Token em Base64
        headers = {
            "Authorization": f"Basic {key}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        data = {
            "grant_type": "client_credentials"
        }

        response = getattr(requests, method)(
            url=self.store.environment.auth_endpoint,
            headers=headers,
            data=data,
        )

        if response.status_code >= 400:
            error = response.json()
            raise Exception(error.get("returnMessage", "Requisição falhou"), error.get("returnCode", 0))

        return response.json()

