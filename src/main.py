import random

from src.dataclasses.card import Card

from src.entities import Billing
from src.entities import Device
from src.entities import ThreeDSecure
from src.entities import Transaction
from src.entities import Url
from src.entities import Environment
from src.entities import eRede
from src.entities import Store

from src.config import Settings
from src.enums.transation_types import TransactionTypes
from src.enums.url_type import UrlType
from src.utils import convert


def main():
    settings = Settings()
    store = Store(settings.PV, settings.TOKEN, Environment.sandbox())
    erede = eRede(store)

    access_token = erede.get_access_token()
    store.set_access_token(access_token)

    reference = "g" + str(random.randint(10**(16 - 1), (10**16)-1))
    amount = convert(200)

    transaction = Transaction(amount, reference)

    ...

if __name__ == "__main__":
    main()
