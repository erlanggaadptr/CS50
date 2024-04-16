# TODO
number = input("Number: ")

# Luhn's Algorithm
# Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
luhn = False
digits = list(number)
digits1 = [int(x) for x in digits]
digits2 = [int(x) for x in digits]
doubled_digits = []
sum_digits = 0
not_doubled = []

for i in range(len(digits1) - 2, -1, -2):
    digits1[i] *= 2
    doubled_digits.append(digits1[i])

for i in doubled_digits:
    while i > 0:
        ones = i % 10
        sum_digits += ones
        i //= 10

# Add the sum to the sum of the digits that weren’t multiplied by 2.
if len(digits) % 2 == 0:
    for i in range(1, len(digits2), 2):
        not_doubled.append(digits2[i])
elif len(digits) % 2 == 1:
    for i in range(0, len(digits2), 2):
        not_doubled.append(digits2[i])

total = sum_digits + sum(not_doubled)

# If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
if total % 10 == 0:
    luhn = True

# Card Identification
if luhn == True:
    # All American Express numbers start with 34 or 37
    if len(number) == 15 and number.startswith(("34", "37")):
        print("AMEX")

    # most MasterCard numbers start with 51, 52, 53, 54, or 55
    elif len(number) == 16 and number.startswith(("51", "52", "53", "54", "55")):
        print("MASTERCARD")

    # and all Visa numbers start with 4
    elif (len(number) == 13 or len(number) == 16) and number.startswith("4"):
        print("VISA")

    else:
        print("INVALID")
else:
    print("INVALID")
