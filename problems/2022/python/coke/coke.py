ACCEPTED_DENOMINATIONS = [25, 10, 5]
amount_due = 50

def request_input():
    print(f"Amount Due: {amount_due}")
    return int(input("Insert Coin: "))

while not amount_due <= 0:
    inserted_coin = request_input()

    while inserted_coin not in ACCEPTED_DENOMINATIONS:
        inserted_coin = request_input()

    amount_due -= inserted_coin

if amount_due < 0:
    amount_due *= -1

print(f"Change Owed: {amount_due}")
