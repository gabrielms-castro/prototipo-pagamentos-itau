from ast import Store
from datetime import timedelta
import datetime
from random import random

from src.config import PV, TOKEN
from src.dataclasses.card import Card
from src.entities.environment import Environment
from src.entities.erede import eRede
from src.entities.transaction import Transaction
from src.enums import TransactionTypes
from src.utils import convert


class PaymentService:
    store = Store(PV, TOKEN, Environment.sandbox())
    
    erede = eRede(store)
    
    access_token = erede.get_access_token()
    store.set_access_token(access_token)

    
    reference = "g" + str(random.randint(10**(16 - 1), (10**16)-1))
    amount = convert(2000.00)

    transaction = Transaction(amount, reference)
    credit_card = Card(
        cardNumber="5448280000000007",
        securityCode="123",
        expirationMonth=1,
        expirationYear=2028,
        cardholderName="John Snow",
        kind=TransactionTypes.CREDIT
    )
    
    transaction.card_transaction(credit_card)
    transaction.capture_transaction(False)
    
    print(transaction.to_json())
    input()

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

    erede.get_refunds(transaction_response.tid)
    query_transaction = erede.get_by_tid(transaction_response.tid)
    print(f"\nTransação consultada: {query_transaction.serialize()}")


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


    # Pix
    expiration_datetime = datetime.now() + timedelta(hours=2)
    expiration_datetime_str = expiration_datetime.strftime("%Y-%m-%dT%H:%M:%S")
    transaction = Transaction(amount, reference)
    transaction.pix_transaction(expiration_datetime_str) 

    pix_transaction = erede.create(transaction)
    print("Resposta da transação Pix:", pix_transaction.to_json())

    query_pix_transaction = erede.get_by_tid(pix_transaction.tid)
    print()
    print("Consulta da transação Pix:", query_pix_transaction.to_json())
