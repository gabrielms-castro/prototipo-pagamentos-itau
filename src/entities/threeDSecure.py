class ThreeDSecure:
    
    CONTINUE_ON_FAILURE = "continue"
    DECLINE_ON_FAILURE = "decline"

    def __init__(self):
        self.embedded = None
        self.onFailure = None
        self.userAgent = None
        self.ipAdress = None
        self.device = None
        self.cardholderName = None
        self.billing = None
        self.url = None
