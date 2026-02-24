import random
import requests

def authorize(access_token):
    """Realizar transação do tipo 'Autorização'

    Returns:
        _type_: JSON
    """
    

    response = requests.post(
        url = "https://sandbox-erede.useredecloud.com.br/v2/transactions",

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


