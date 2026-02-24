import requests

from src.authentication import get_access_token
from src.config import EREDE_BASE_URL

def capture(tid: str, amount: int):
    """Confirmar autorização da transação (captura) via PUT

    Args:
        tid (str): Número identificador único da transação.
        amount (int): Valor total da transação sem separador de milhar e decimal.

    Returns:
        _type_: json
    """
    access_token = get_access_token()

    response = requests.put(
        url=f"{EREDE_BASE_URL}/v2/transactions/{tid}",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        json={"amount": amount}  # pode capturar valor menor que o autorizado
    )

    return response.json()