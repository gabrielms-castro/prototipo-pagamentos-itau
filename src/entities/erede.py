from src.dataclasses.http_methods import HttpMethods
from src.entities.store import Store
from src.services.authentication_service import AuthenticationService


class eRede:
    def __init__(self, store: Store):
        self.store = store

    def get_access_token(self):
        auth_service = AuthenticationService(self.store)
        return auth_service.send_request(HttpMethods.POST, self.store.b64_credential)