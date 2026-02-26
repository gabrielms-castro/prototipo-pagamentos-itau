import random
from datetime import datetime, timedelta

from src.dataclasses.http_methods import HttpMethods
from src.dataclasses.card import Card
from src.entities.transaction import Transaction
from src.enums import TransactionTypes
from src.config import PV, TOKEN
from src.entities.environment import Environment
from src.entities.store import Store
from src.entities.erede import eRede
from src.utils import convert


def main():
    store = Store(PV, TOKEN, Environment.sandbox())
    erede = eRede(store)

    access_token = erede.get_access_token()
    store.set_access_token(access_token)

    reference = "g" + str(random.randint(10**(16 - 1), (10**16)-1))
    amount = convert(2000.00)

    # Pix
    expiration_datetime = datetime.now() + timedelta(hours=2)
    expiration_datetime_str = expiration_datetime.strftime("%Y-%m-%dT%H:%M:%S")
    transaction = Transaction(amount, reference)
    transaction.pix_transaction(expiration_datetime_str) 

    response = erede.create(transaction)
    print("Resposta da transação Pix:", response.to_json())

if __name__ == "__main__":
    main()
