from src.dataclasses.http_methods import HttpMethods
from src.entities.store import Store

from .transaction_service import TransactionService


class GetTransactionService(TransactionService):
    def __init__(self, store: Store):
        super().__init__(store)
        self.tid = None
        self.reference = None
        self.refunds = False

    def get_uri(self) -> str:
        if self.reference is not None:
            return f"{super().get_uri()}?reference={self.reference}"

        if self.tid is None:
            raise ValueError("You need to specify one: the tid or the reference")

        if self.refunds:
            return f"{super().get_uri()}/{self.tid}/refunds"

        return f"{super().get_uri()}/{self.tid}"
    
    def execute(self):
        return self.send_request(HttpMethods.GET)