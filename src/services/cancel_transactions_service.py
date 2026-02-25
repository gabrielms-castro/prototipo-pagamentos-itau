from src.dataclasses.http_methods import HttpMethods
from src.entities.store import Store
from src.entities.transaction import Transaction
from src.services.transaction_service import TransactionService


class CancelTransactionService(TransactionService):
    def __init__(self, store: Store, transaction: Transaction):
        super().__init__(store)
        self.transaction = transaction

    def get_uri(self) -> str:
        return f"{super().get_uri()}/{self.transaction.tid}/refunds"
    
    def execute(self):
        return self.send_request(HttpMethods.POST, self.transaction.to_json())