class Card:
    """
    Representa os dados do cartão utilizado em uma transação.

    Attributes:
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
            Obrigatório. Aceita 2 ou 4 dígitos.
            Exemplo: `2028` ou `28`.

        securityCode (str, optional):
            Código de segurança do cartão (CVV/CVC), geralmente no verso.
            Tamanho máximo: 4. O envio aumenta a chance de aprovação.
            Exemplo: `"235"`.
    """
    def __init__(self, cardholderName, cardNumber, expirationMonth, expirationYear, securityCode):
        self.cardholderName = cardholderName
        self.cardNumber = cardNumber
        self.expirationMonth = expirationMonth
        self.expirationYear = expirationYear
        self.securityCode = securityCode
        self.kind = None