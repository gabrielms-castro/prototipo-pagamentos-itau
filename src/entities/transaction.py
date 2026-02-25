from src.dataclasses.transaction_response import TransactionResponse
from src.entities.card import Card
from src.enums.card import CardTypes
from src.models import BaseModel


class Transaction(BaseModel):
    """
    Representa uma transação (crédito/débito) e seus dados de autorização/captura.

    Attributes:
        capture (bool, optional):
            Define se a transação terá captura automática (`True`) ou posterior (`False`).
            Se não enviado, será considerado captura automática (`True`).
            Exemplo: `False`.

        kind (str, optional):
            Tipo de transação a ser realizada.
            - Para transações de crédito, utilizar `"credit"`.
            - Para transações de débito, utilizar `"debit"`.
            Se não enviado, será considerado `"credit"`.
            Exemplo: `"credit"`.

        reference (str):
            Código da transação gerado pelo estabelecimento.
            Obrigatório. Tamanho máximo: 50.
            Exemplo: `"pedido123"`.

        amount (int | float):
            Valor total da transação **sem separador de milhar e sem casa decimal** (em centavos).
            Obrigatório. Quantidade máxima de dígitos: 10.
            Exemplos:
                - R$ 10,00 = `1000`
                - R$ 0,50  = `50`

        installments (int, optional):
            Número de parcelas em que uma transação será autorizada.
            Mínimo: 2. Máximo: 12.
            Se não enviado, será considerado à vista.
            Exemplo: `2`.

        cardholderName (str, optional):
            Nome do portador impresso no cartão.
            Tamanho máximo: 30.
            Exemplo: `"John Snow"`.

        cardNumber (str):
            Número do cartão.
            Obrigatório. Tamanho máximo: 19.
            Exemplo: `"5448280000000007"`.

        expirationMonth (int):
            Mês de vencimento do cartão.
            Obrigatório. Mínimo: 1. Máximo: 12.
            Exemplo: `12`.

        expirationYear (int | str):
            Ano de vencimento do cartão.
            Obrigatório. Pode ser enviado com 2 ou 4 dígitos (ex.: `28` ou `2028`).
            Exemplo: `2028`.

        securityCode (str, optional):
            Código de segurança do cartão (geralmente no verso).
            Tamanho máximo: 4.
            O envio deste parâmetro aumenta a possibilidade de aprovação da transação.
            Exemplo: `"235"`.

        softDescriptor (str, optional):
            Frase personalizada que será impressa na fatura do portador.
            Tamanho máximo: 18.

        subscription (bool, optional):
            Informa ao emissor se a transação é proveniente de uma recorrência.
            - Se for recorrência, enviar `True`.
            - Caso contrário, enviar `False`.
            Se não enviado, será considerado `False`.

            Observação: a Rede não gerencia agendamentos de recorrência; apenas permite indicar
            que a transação originou de um plano recorrente.

        origin (int, optional):
            Identifica a origem da transação.
            Valores:
                - e.Rede = 1
                - MasterPass = 4
                - Click to Pay = 6
            Quantidade máxima de dígitos: 2.
            Se não enviado, será considerado e.Rede (`1`).
            Exemplo: `1`.

        distributorAffiliation (int, optional):
            Número de filiação do distribuidor (PV).
            Quantidade máxima de dígitos: 9.

        brandTid (str, optional):
            Identifica a primeira e as demais transações de recorrência através do envio deste campo.
            Usado somente quando `subscription` for `True`.
            Campo dinâmico.
            OBS: utilizado somente para as bandeiras Visa, Master e ELO.
            Tamanho máximo: 16.

        storageCard (str | int, optional):
            Indica operações que possam ou não estar utilizando COF (Card on File):
                - `0`: Transação com credencial não armazenada.
                - `1`: Transação com credencial armazenada pela primeira vez.
                - `2`: Transação com credencial já armazenada.
            Atenção: se não enviado, será considerado `0`.
            Tamanho máximo: 1.
            Exemplo: `1`.

        transactionCredentials (TransactionCredentials, optional):
            Objeto com informações de credenciais armazenadas (COF).

            Campos esperados em `TransactionCredentials`:
                - credentialId (str):
                    Indica a categoria da transação com credencial armazenada.
                    Tamanho máximo: 2.
                    Exemplo: `"05"`.
                    (Consulte a seção “Categorização de transações card-on-file” para detalhes.)
    """

    def __init__(self, amount, reference):
        self.amount = amount
        self.reference = reference

        self.capture = None
        self.installments = None

        self.cardNumber = None
        self.securityCode = None
        self.expirationMonth = None
        self.expirationYear = None
        self.cardHolderName = None
        self.kind = None

        self.softDescriptor = None
        self.subscription = None
        self.origin = None
        self.distributorAffiliation = None
        self.brandTid = None
        self.storageCard = None
        self.transactionCredentials = None
        self.credentialId = None

    def capture_transaction(self, capture: bool) -> None:
        if self.kind == CardTypes.CREDIT:
            self.capture = True

        self.capture = capture

    def credit_card(self, card_number, security_code, expiration_month, expiration_year, card_holder_name):
        return self.card(
            card_number, 
            security_code, 
            expiration_month, 
            expiration_year, 
            card_holder_name,
            CardTypes.CREDIT
        )

    def debit_card(self, card_number, security_code, expiration_month, expiration_year, card_holder_name):
        return self.card(
            card_number, 
            security_code, 
            expiration_month, 
            expiration_year, 
            card_holder_name,
            CardTypes.DEBIT
        )

    def card(self, card_number, security_code, expiration_month, expitarion_year, card_holder_name, kind):
        self.cardNumber = card_number
        self.securityCode = security_code
        self.expirationMonth = expiration_month
        self.expirationYear = expitarion_year
        self.cardHolderName = card_holder_name
        self.kind = kind

        return self

    @staticmethod
    def unserialize(data: dict):

        if data is None:
            return {}
        
        instance = TransactionResponse()

        for key, value in data.items():
            setattr(instance, key, value)
        
        return instance