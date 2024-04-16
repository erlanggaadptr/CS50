from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hello world") == 0


def test_h():
    assert value("h") == 20
    assert value("H") == 20
    assert value("howdy") == 20


def test_else():
    assert value("morning") == 100
    assert value("Morning") == 100
