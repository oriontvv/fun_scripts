import json
from scripts.json import read_ordered_json

_content = '{"name": "ACME", "shares": 50, "price": 490.1}'

def test_read_ordered_json():
    data = read_ordered_json(_content)
    assert list(data.keys()) == ['name', 'shares', 'price']


from scripts.json import read_object, JSONObject
def test_read_object():
    obj = read_object(_content)
    assert obj.name == 'ACME'
    assert obj.shares == 50
    assert obj.price == 490.1


from scripts.json import Point, serialize_instance, unserialize_object
def test_custom_type_serialization():
    point = Point(23, 42)
    s = json.dumps(point, default=serialize_instance)
    #assert s == {'__classname__': 'Point', 'x': 23, 'y': 42}
    assert '__classname__' in s

    p = json.loads(s, object_hook=unserialize_object)
    assert p.x == point.x and p.y == point.y
