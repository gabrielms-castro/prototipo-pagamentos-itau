import random
import requests

from src.authentication import get_access_token
from src.config import EREDE_BASE_URL


def authorize():
    """Realizar transação do tipo 'Autorização'

    Returns:
        _type_: JSON
    """
    access_token = get_access_token()

    response = requests.post(
        url = f"{EREDE_BASE_URL}/v2/transactions",

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-type": "application/json"
        },

        json = {
            "capture": False,
            "kind": "credit",
            "reference": "g" + str(random.randint(10**(16 - 1), (10**16)-1)),
            "amount": 2000,
            "installments": 2,
            "cardholderName": "John Snow",
            "cardNumber": "5448280000000007",
            "expirationMonth": 1,
            "expirationYear": 2028,
            "securityCode": "123",
            "softDescriptor": "string",
            "subscription": False,
            "origin": 1,
            "distributorAffiliation": 0,
            "brandTid": "string",
            "storageCard": "0",
            "transactionCredentials": {
                "credentialId": "01"
            }
        }
    )

    return response.json()


