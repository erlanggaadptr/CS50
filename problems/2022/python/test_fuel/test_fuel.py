from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("three/four")
        convert("1.5/3")
        convert("5/4")


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
