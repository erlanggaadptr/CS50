while True:
    fraction = input("Fraction: ").strip()

    try:
        numerator, denominator = fraction.split('/')
        numerator = int(numerator)
        denominator = int(denominator)

        if denominator == 0:
            raise ZeroDivisionError
        elif numerator > denominator:
            continue

        percentage = round((numerator / denominator), 2) * 100

        if percentage >= 99:
            output ='F'
        elif percentage <= 1:
            output = 'E'
        else:
            output =f"{int(percentage)}%"

    except (ValueError, ZeroDivisionError):
        pass

    else:
        break

print(output)
