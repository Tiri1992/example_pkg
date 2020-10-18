from example_pkg.foo import say_hello


def test_say_hello():
    assert say_hello() == "Hello World! Requests has been imported."
