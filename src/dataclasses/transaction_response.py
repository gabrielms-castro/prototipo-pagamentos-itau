from dataclasses import dataclass, fields


@dataclass
class TransactionResponse:
    reference: str
    tid: str
    nsu: str
    authorizationCode: str
    brandTid: str
    transactionLinkId: str
    dateTime: str
    amount: int
    cardBin: str
    last4: str
    returnCode: str
    returnMessage: str
    links: list[dict[str, str]]

    @classmethod
    def unserialize(cls, response: dict):
        if response is None:
            return {}
        
        known_fields = {f.name for f in fields(cls)}
        filtered = {}
        for key, value in response.items():
            if key in known_fields:
                filtered[key] = value
        
        return cls(**filtered)
                