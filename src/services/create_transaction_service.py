from src.entities.store import Store
from src.dataclasses.http_methods import HttpMethods
from src.services.transaction_service import TransactionService


class CreateTransactionService(TransactionService):
    def __init__(self, store: Store):
        super().__init__(store)
        self.body = None

    def execute(self):
        return self.send_request(HttpMethods.POST, self.body)