import random
import sys

level = 0

while level < 1:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass

number = random.randint(1, level)
guess = 0

while guess != number:
    try:
        guess = int(input("Guess: "))

        if guess > number:
            print("Too large!")

        elif guess < number:
            print("Too small!")

    except ValueError:
        pass

sys.exit("Just right!")
