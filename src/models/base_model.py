import json

class BaseModel:

    def to_json(self):
        return json.dumps(self.serialize())

    def serialize(self):
        return { key: value for key, value in self.__dict__.items() if value is not None }

