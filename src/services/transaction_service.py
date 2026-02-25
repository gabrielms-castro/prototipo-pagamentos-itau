from typing import Any, Optional

import requests

from src.dataclasses.http_methods import HttpMethods
from src.entities.store import Store
from src.entities.transaction import Transaction


class TransactionService:

    def __init__(self, store: Store):
        self.store = store

    def execute(self):
        raise NotImplementedError("Not implemented")

    def get_uri(self) -> str:
        return self.store.environment.transactions_endpoint

    def send_request(self, method: HttpMethods, data: Optional[dict[str, Any]] = None) -> Transaction:
        
        url = self.get_uri()
        headers = {
            "Authorization": f"Bearer {self.store.access_token}",
            "Content-type": "application/json"
        }

        response = getattr(requests, method)(
            url=url,
            headers=headers,
            data=data
        )

        if response.status_code >= 400:
            raise Exception(response.json())
        

        return Transaction.unserialize(response.json())
