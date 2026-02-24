import requests
from src.authentication import get_access_token
from src.config import EREDE_BASE_URL


def refund(tid):
    access_token = get_access_token()
    response = requests.post(
        url=f"{EREDE_BASE_URL}/v2/transactions/{tid}/refunds",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        json={
            "amount": 2000,
            "urls": [
                {
                "kind": "callback",
                "url": "https://cliente.callback.com.br"
                }
            ]      
        }
    )

    return response.json()    