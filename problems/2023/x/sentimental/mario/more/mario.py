# TODO
while True:
    try:
        height = int(input("Height: "))
    except ValueError:
        print("Invalid input: not an integer!")
        continue
    if height < 1:
        print("Invalid input: not a natural number!")
        continue
    if height > 8:
        print("Invalid input: maximum is 8!")
        continue
    else:
        break

for i in range(1, height + 1):
    j = height - i
    print(" " * j, end="")
    print("#" * i, end="")
    print("  ", end="")
    print("#" * i)
