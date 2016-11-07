import pytest

from scripts.typing_descriptor import Integer

from scripts.typing_descriptor import Typed, type_assert

@pytest.fixture()
def point():
    class Point:
        x = Integer('x')
        y = Integer('y')
        def __init__(self, x, y):
            self.x = x
            self.y = y

    return Point(0, 0)


def test_integer(point):
    assert point.x == 0
    point.x = 42
    assert point.x == 42

    with pytest.raises(TypeError):
        point.x = 23.1


@pytest.fixture
def stock():
    @type_assert(name=str, shares=int, price=float)
    class Stock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    return Stock('NAME', shares=42, price=23.4)

def test_class_decorator(stock):
    assert stock.name == 'NAME'
    with pytest.raises(TypeError):
        stock.name = 23
    stock.name += 'qwe'
    assert stock.name == 'NAMEqwe'

    assert stock.shares == 42
    with pytest.raises(TypeError):
        stock.shares += 'NAME'

    stock.shares = 100500
