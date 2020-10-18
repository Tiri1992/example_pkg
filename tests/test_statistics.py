from example_pkg.statistics import mean

# Simple unit test


def test_mean():
    l = [2, 3, 4]
    assert mean(l) == 3.0
