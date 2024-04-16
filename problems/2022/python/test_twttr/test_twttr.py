from twttr import shorten


def test_lower():
    assert shorten("cat") == "ct"


def test_upper():
    assert shorten("CAT") == "CT"


def test_numbers():
    assert shorten("cat123") == "ct123"


def test_punctuation():
    assert shorten("cat.") == "ct."
