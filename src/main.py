import random

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


    #cartão de débito
    transaction = Transaction(amount, reference)
    debit_card = Card(
        cardNumber="5277696455399733",
        securityCode="123",
        expirationMonth=1,
        expirationYear=2035,
        cardholderName="John Snow",
        kind=TransactionTypes.DEBIT
    )
    
    transaction.card_transaction(debit_card)

    print()
    print(transaction.to_json())
    transaction_response = erede.create(transaction)
    print(transaction_response.to_json())
    print()
    print(erede.get_by_tid(transaction_response.tid).to_json())    

if __name__ == "__main__":
    main()
