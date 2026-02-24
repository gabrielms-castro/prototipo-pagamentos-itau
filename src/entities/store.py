from typing import Optional

from src.entities.environment import Environment
from src.utils import encode_credentials


class Store:
    def __init__(self, pv: str, token: str, environment: Optional[Environment] = None):

        if environment is None:
            environment = environment.production()
        
        self.environment = environment
        self.pv = pv
        self.token = token
        self.b64_credential = encode_credentials(self.pv, self.token)
        self.access_token = None

    def get_access_token(self) -> str:
        return self.access_token
    
    def set_access_token(self, access_token) -> None:
        self.access_token = access_token

        
    