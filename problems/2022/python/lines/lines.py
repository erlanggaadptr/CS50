import sys


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif not sys.argv[1].rstrip().endswith(".py"):
        sys.exit("Not a Python file")

    try:
        open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count_lines(sys.argv[1]))


def count_lines(file_path):
    with open(file_path) as file:
        count = 0

        for line in file:
            if line.strip() != "" and not line.lstrip().startswith("#"):
                count += 1

    return count


if __name__ == '__main__':
    main()
