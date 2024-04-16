import pytest
from working import convert


def test_convert():
    io = [
        {"input": "9 AM to 5 PM", "output": "09:00 to 17:00"},
        {"input": "9:00 AM to 5:00 PM", "output": "09:00 to 17:00"},
        {"input": "10:00 PM to 8:00 AM", "output": "22:00 to 08:00"},
        {"input": "10:30 PM to 8:50 AM", "output": "22:30 to 08:50"},
    ]

    for i in range(len(io)):
        assert convert(io[i]["input"]) == io[i]["output"]


def test_convert_ValueError():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM5 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("9:60 to 5:60")
