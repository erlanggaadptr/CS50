def main():
    while True:
        fraction = input("Fraction: ")

        try:
            percentage = convert(fraction)

        except (ValueError, ZeroDivisionError) as e:
            pass

        else:
            print(gauge(percentage))

def convert(fraction):
    numerator, denominator = fraction.split("/")
    numerator, denominator = int(numerator), int(denominator)

    if denominator == 0:
        raise ZeroDivisionError

    elif numerator > denominator:
        raise ValueError

    return round((numerator / denominator), 2) * 100


def gauge(percentage):
    if percentage >= 99:
        return 'F'

    elif percentage <= 1:
        return 'E'

    else:
        return f"{int(percentage)}%"


if __name__ == "__main__":
    main()
