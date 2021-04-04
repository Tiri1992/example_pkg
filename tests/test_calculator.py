from example_pkg.calculator import add
from example_pkg.calculator import subtract

# Simple unit tests


def test_add():
    assert add(3, 2) == 5


def test_subtract():
    assert subtract(5, 4) == 1
