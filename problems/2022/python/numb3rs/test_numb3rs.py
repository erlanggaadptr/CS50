from numb3rs import validate


def main():
    test_validate_1()
    test_validate_2()
    test_validate_3()


def test_validate_1():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True


def test_validate_2():
    assert validate("75.456.76.65") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False


def test_validate_3():
    assert validate("cat") == False
    assert validate("dog") == False


if __name__ == "__main__":
    main()
