from src.models import BaseModel


class Billing(BaseModel):
    def __init__(self, address, city, postalcode, state, country, emailAddress, phoneNumber):
        self.address = address
        self.city = city
        self.postalcode = postalcode
        self.state = state
        self.country = country
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber