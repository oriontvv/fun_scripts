import pytest

from scripts.typing_descriptor import Integer

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
