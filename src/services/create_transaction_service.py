from src.entities.store import Store
from src.dataclasses.http_methods import HttpMethods
from src.entities.transaction import Transaction
from src.services.transaction_service import TransactionService


class CreateTransactionService(TransactionService):
    def __init__(self, store: Store, transaction: Transaction):
        super().__init__(store)
        self.transaction = transaction

    def execute(self) -> Transaction:
        return self.send_request(HttpMethods.POST, self.transaction.to_json())