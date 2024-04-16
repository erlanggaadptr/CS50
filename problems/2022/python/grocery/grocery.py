groceries = dict()

while True:
    try:
        item = str(input())
        if item not in groceries:
            groceries[item] = 1
        else:
            groceries[item] += 1
    except EOFError:
        sorted_groceries = sorted(groceries.keys())
        for item in sorted_groceries:
            count = groceries[item]
            print(f"{count} {item.upper()}")
        exit()
