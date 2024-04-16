from plates import is_valid


def test_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False


def test_min_max_chars():
    assert is_valid("AA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False


def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False


def test_punctuation():
    assert is_valid("AAA.12") == False
    assert is_valid("AAA 12") == False
    assert is_valid("AAA,12") == False
    assert is_valid("AA:12") == False
    assert is_valid("AA/12") == False
