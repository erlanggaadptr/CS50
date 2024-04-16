import sys

names = []

while True:
    try:
        names.append(input("Name: "))

    except EOFError:
        print("Adieu, adieu, to ", end='')

        if len(names) == 1:
            print(''.join(names))

        elif len(names) == 2:
            print(' and '.join(names[0:]))

        elif len(names) > 2:
            print(', '.join(names[0:-1]) + ', and ' + ''.join(names[-1]))

        sys.exit()
