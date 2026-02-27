from src.entities import Device
from src.entities import Billing
from src.models import BaseModel


class ThreeDSecure(BaseModel):
    
    CONTINUE = "continue"
    DECLINE = "decline"

    def __init__(self, userAgent, ipAddress, device: Device, billing: Billing, onFailure=CONTINUE, embedded=True):
        self.embedded = embedded
        self.onFailure = onFailure
        self.userAgent = userAgent
        self.ipAddress = ipAddress
        self.device = device
        self.billing = billing