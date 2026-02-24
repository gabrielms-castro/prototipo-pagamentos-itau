from typing import Optional

from src.entities.environment_production import ProductionUrls
from src.entities.environment_sandbox import SandboxUrls


class Environment:
    PRODUCTION = ProductionUrls
    SANDBOX = SandboxUrls
    VERSION = "v2"

    def __init__(self, base_url: str, version: Optional[str] = None):
        if version is None:
            version = Environment.VERSION

        self.transactions_endpoint = f"{base_url.TRANSACTION_URL}/{version}/transactions"
        self.auth_endpoint = base_url.AUTH_URL

    @staticmethod
    def production():
        return Environment(Environment.PRODUCTION)

    @staticmethod
    def sandbox():
        return Environment(Environment.SANDBOX)