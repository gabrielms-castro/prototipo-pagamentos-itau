import requests

from src.authentication import get_access_token
from src.config import EREDE_BASE_URL

def query_transaction(tid: str):
    """Consultar transação por reference

    Args:
        tid (str): Número identificador único da transação.

    Returns:
        _type_: JSON
    """

    access_token = get_access_token()

    response = requests.get(
        url=f"{EREDE_BASE_URL}/v2/transactions/{tid}",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
    )
    print(response)
    return response.json()