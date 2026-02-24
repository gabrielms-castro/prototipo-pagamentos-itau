from dataclasses import dataclass

@dataclass
class ProductionUrls:
    AUTH_URL = "https://api.userede.com.br/redelabs/oauth2/token"
    TRANSACTION_URL = "https://api.userede.com.br/erede"