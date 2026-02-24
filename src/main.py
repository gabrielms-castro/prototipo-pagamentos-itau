import random

from src.dataclasses.http_methods import HttpMethods
from src.services.transaction_service import TransactionService
from src.config import PV, TOKEN
from src.entities.environment import Environment
from src.entities.store import Store
from src.entities.erede import eRede


def main():
    store = Store(PV, TOKEN, Environment.sandbox())
    
    erede = eRede(store)
    
    access_token = erede.get_access_token()

    store.set_access_token(access_token)
    
    reference = "g" + str(random.randint(10**(16 - 1), (10**16)-1))
    
    json = {
        "capture": False,
        "kind": "credit",
        "reference": reference,
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


    transaction = erede.create(json)
    print(transaction)

    print()
    tid = transaction.get("tid")
    print(tid)

    print()
    print(erede.get_by_tid(tid))

    print()
    print(erede.get_by_reference(reference))
    

if __name__ == "__main__":
    main()