from src.services import (
    AuthenticationService,
    CancelTransactionService,
    CaptureTransactionService,
    CreateTransactionService,
    GetTransactionService,
)
from src.dataclasses.http_methods import HttpMethods
from src.entities.store import Store


class eRede:
    def __init__(self, store: Store):
        self.store = store

    def get_access_token(self):
        auth_service = AuthenticationService(self.store)
        response = auth_service.send_request(HttpMethods.POST, self.store.b64_credential)
        return response.get("access_token")

    def create(self, transaction):
        """Create a Transaction
        """
        create_transaction = CreateTransactionService(self.store, transaction)
        return create_transaction.execute()

    def capture(self, transaction):
        """Capture a Transaction
        """
        capture_transaction = CaptureTransactionService(self.store, transaction)
        return capture_transaction.execute()
    
    def cancel(self, transaction):
        """Cancel a Transaction
        """
        cancel_transaction = CancelTransactionService(self.store, transaction)
        return cancel_transaction.execute()
    
    def get_by_tid(self, tid):
        """Get a Transaction by its TID
        """
        get_transaction = GetTransactionService(self.store)
        get_transaction.tid = tid
        return get_transaction.execute()
    
    def get_by_reference(self, reference):
        """Get a Transaction by its reference
        """
        get_transaction = GetTransactionService(self.store)
        get_transaction.reference = reference
        return get_transaction.execute()    
    
    def get_refunds(self, tid):
        """Get a Transaction refunds
        """
        get_transaction = GetTransactionService(self.store)
        get_transaction.tid = tid
        get_transaction.refunds = True
        return get_transaction.execute()