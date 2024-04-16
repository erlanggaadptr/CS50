import random


def main():
    level = get_level()
    problems = [f"{generate_integer(level)} + {generate_integer(level)} = " for _ in range(10)]
    score = 0

    for problem in problems:
        tries = 0
        answer = eval(problem.replace(' = ', ''))

        while tries != 3:
            try:
                if int(input(problem)) != answer:
                    raise ValueError

                else:
                    score += 1
                    break

            except ValueError:
                print("EEE")
                tries += 1

            if tries == 3:
                print(f"{problem}{str(answer)}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level not in range(1, 4):
                raise ValueError
            else:
                return level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    else:
        return random.randint(10 ** (level - 1), (10 ** level) - 1)


if __name__ == "__main__":
    main()
