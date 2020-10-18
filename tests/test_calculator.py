from example_pkg.calculator import add
from example_pkg.calculator import subtract

# Simple unit tests


def test_add():
    x = 2
    y = 3
    assert add(x, y) == 5


def test_subtract():
    x = 8
    y = 7
    assert subtract(x, y) == 1
