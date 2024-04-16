from datetime import date
from seasons import get_date
import pytest


def test_get_date():
    inputs = [
        {"input": "2023-03-18", "output": date(2023, 3, 18)},
        {"input": "2022-03-18", "output": date(2022, 3, 18)},
        {"input": "2000-01-01", "output": date(2000, 1, 1)},
        {"input": "1995-12-31", "output": date(1995, 12, 31)},
        {"input": "2010-02-28", "output": date(2010, 2, 28)},
    ]

    for i in range(len(inputs)):
        assert get_date(inputs[i]["input"]) == inputs[i]["output"]


def test_get_date_invalid():
    inputs = [
        "abcdef",
        "January, 10th, 2022",
        "2022/10/01",
        "2023-02-30",
        "2023-05-XX",
    ]

    with pytest.raises(SystemExit) as e:
        for i in range(len(inputs)):
            get_date(inputs[i])

        assert str(e.value) == "Invalid date"

