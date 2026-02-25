import random

from src.dataclasses.http_methods import HttpMethods
from src.entities.card import Card
from src.entities.transaction import Transaction
from src.enums.card import CardTypes
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

    transaction = Transaction(amount, reference)
    transaction.credit_card(
        card_number="5448280000000007",
        security_code="123",
        expiration_month=1,
        expiration_year=2028,
        card_holder_name="John Snow",
    ).capture_transaction(False)


    transaction_response = erede.create(transaction)
    print(transaction_response.serialize())
    if transaction_response.returnCode == "00":
        print("Transação criada com sucesso!")
        query_transaction = erede.get_by_tid(transaction_response.tid)
        print(f"\nTransação consultada: {query_transaction.serialize()}")
        
        erede.capture(transaction_response)
        query_transaction = erede.get_by_tid(transaction_response.tid)
        print(f"\nTransação consultada: {query_transaction.serialize()}")
        
        erede.cancel(transaction_response)
        query_transaction = erede.get_by_tid(transaction_response.tid)
        print(f"\nTransação consultada: {query_transaction.serialize()}")

if __name__ == "__main__":
    main()
