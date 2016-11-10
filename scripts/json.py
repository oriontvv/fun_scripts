import json
from collections import OrderedDict


def read_ordered_json(s):
    return json.loads(s, object_pairs_hook=OrderedDict)



class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


def read_object(s):
    return json.loads(s, object_hook=JSONObject)


#################################
# serialize/deserialize custom type
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d

# Dictionary mapping names to known classes
classes = {
    'Point' : Point
}
def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d