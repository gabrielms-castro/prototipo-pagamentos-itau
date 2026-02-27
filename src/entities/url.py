from src.enums import UrlType
from src.models import BaseModel

class Url(BaseModel):
    def __init__(self, kind: UrlType, url: str):
        self.kind = kind
        self.url = url

