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

from src.config import PV, TOKEN
from src.enums.transation_types import TransactionTypes
from src.enums.url_type import UrlType
from src.utils import convert


def main():
    store = Store(PV, TOKEN, Environment.sandbox())
    erede = eRede(store)

    access_token = erede.get_access_token()
    store.set_access_token(access_token)

    reference = "g" + str(random.randint(10**(16 - 1), (10**16)-1))
    amount = convert(200)

    transaction = Transaction(amount, reference)

    billing = Billing(
        address="Rua Pedro Luiz",
        city="Guarulhos",
        postalcode="07151-385",
        state="SP",
        country="Brasil",
        emailAddress="email@user.com",
        phoneNumber="(11)91234-5678"        
    )

    device = Device(
        colorDepth=1,
        deviceType3ds="BROWSER",
        javaEnabled=False,
        language="BR",
        screenHeight=500,
        screenWidth=500,
        timeZoneOffset=3        
    )

    urls = [
        Url(kind=UrlType.SUCCESS, url="https://scommerce.userede.com.br/LojaTeste/Venda/sucesso"),
        Url(kind=UrlType.FAILURE, url="https://scommerce.userede.com.br/LojaTeste/Venda/falha"),
    ]

    three_d_secure_config = ThreeDSecure(
        embedded=True,
        onFailure="continue",
        userAgent="Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405",
        ipAddress="192.168.130.20",
        device=device,
        billing=billing
    )

    credit_card = Card(
        cardholderName="John Snow",
        cardNumber="2223000148400010",
        expirationMonth=1,
        expirationYear=2035,
        securityCode="123",  
        kind=TransactionTypes.DEBIT      
    )
    
    # transaction.card_transaction(credit_card)
    # transaction.three_d_secure_transaction(three_d_secure_config, urls)

    # print(transaction.to_json())
    # print()

    # three_d_secure_transaction = erede.create(transaction)
    # print(three_d_secure_transaction.to_json())

    print()
    query_transaction = erede.get_by_tid("10012602271646257551")
    print(query_transaction.to_json())



if __name__ == "__main__":
    main()
