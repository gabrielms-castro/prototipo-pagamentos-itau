from src.services.get_transaction_service import GetTransactionService
from src.dataclasses.http_methods import HttpMethods
from src.entities.store import Store
from src.services.authentication_service import AuthenticationService


class eRede:
    def __init__(self, store: Store):
        self.store = store

    def get_access_token(self):
        auth_service = AuthenticationService(self.store)
        response = auth_service.send_request(HttpMethods.POST, self.store.b64_credential)
        return response.get("access_token")

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