# Itaú Use Rede

Prototipação de uma SDK para a API e.Rede do Itaú.

Foi utilizado o repositório [original](https://github.com/DevelopersRede/erede-python/tree/master) como inspiração.

Este protótipo é basicamente uma refatoração/atualização com uma versão mais atual do Python e de novas funcionalidades do e.Rede (por exemplo, OAUTH2.0 para autenticação)

## Sandbox
 * [Cartões](https://developer.userede.com.br/e-rede#tutorial-sandbox-cartoes)


### [Autenticação](https://developer.userede.com.br/e-rede#autenticacao-autorizacao-rede-apis)

### [Captura](https://developer.userede.com.br/e-rede#documentacao-captura)
Ao realizar uma autorização, é necessária a confirmação desta transação (captura). Nesse momento é gerada a cobrança na fatura do portador do cartão.
```sh
PUT: /v2/transactions/{tid}
```


## Exemplos de Uso:
### Cartão de Crédito
```py
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

```


### Cartão de Débito
```py
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

```


### 3DS 2.0 MPI
```py
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
    
    transaction.card_transaction(credit_card)
    transaction.three_d_secure_transaction(three_d_secure_config, urls)
```

### Pix
```py
    expiration_datetime = datetime.now() + timedelta(hours=2)
    expiration_datetime_str = expiration_datetime.strftime("%Y-%m-%dT%H:%M:%S")
    transaction = Transaction(amount, reference)
    transaction.pix_transaction(expiration_datetime_str) 

    pix_transaction = erede.create(transaction)
    print("Resposta da transação Pix:", pix_transaction.to_json())

    query_pix_transaction = erede.get_by_tid(pix_transaction.tid)
    print()
    print("Consulta da transação Pix:", query_pix_transaction.to_json())
```
