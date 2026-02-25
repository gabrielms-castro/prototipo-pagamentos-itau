from dataclasses import dataclass

from src.models.base_model import BaseModel


@dataclass
class TransactionResponse(BaseModel):
    def __init__(self):
        self.tid = None
        self.nsu = None
        self.authorizationCode = None
        self.brandTid = None
        self.transactionLinkId = None
        self.dateTime = None
        self.amount = None
        self.cardBin = None
        self.last4 = None
        self.returnCode = None
        self.returnMessage = None
        self.links = []
        self.status = None
        