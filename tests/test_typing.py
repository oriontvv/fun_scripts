import pytest

from scripts.typing import Integer

@pytest.fixture()
def point():
	class Point:
		x = Integer('x')
		y = Integer('y')

	return Point()


# def test_simple(point):
	# assert point.x == 0
	