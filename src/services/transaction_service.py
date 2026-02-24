from typing import Any, Optional

import requests

from src.dataclasses.http_methods import HttpMethods
from src.entities.store import Store
from src.enums.card import Card


class TransactionService:

    def __init__(self, store: Store):
        self.store = store

    def execute(self):
        raise NotImplementedError("Not implemented")

    def get_uri(self) -> str:
        return self.store.environment.transactions_endpoint

    def send_request(self, method: HttpMethods, data: Optional[dict[str, Any]] = None) -> requests.Response:
        
        url = self.get_uri()
        headers = {
            "Authorization": f"Bearer {self.store.access_token}",
            "Content-type": "application/json"
        }

        response = getattr(requests, method)(
            url=url,
            headers=headers,
            json=data
        )

        if response.status_code >= 400:
            error = response
            # raise Exception(error.get("returnMessage", "Requisição falhou"), error.get("returnCode", 0))
            raise Exception(error)

        return response.json()
