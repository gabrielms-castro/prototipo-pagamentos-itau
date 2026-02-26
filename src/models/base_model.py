import json

class BaseModel:

    def to_json(self):
        return json.dumps(self.serialize(), cls=RecursiveEncoder)

    def serialize(self):
        collection = { key: value for key, value in self.__dict__.items() if value is not None }

        for key, value in collection.items():
            if hasattr(value, "serialize"):
                collection[key] = value.serialize()
                
        return collection


class RecursiveEncoder(json.JSONEncoder):

    def default(self, obj):

        if hasattr(obj, "serialize"):
            return obj.serialize()
        
        return super().default(obj)