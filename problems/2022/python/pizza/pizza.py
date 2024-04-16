import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 1:
        sys.exit("Too few command-line arguments")

    elif not sys.argv[1].rstrip().endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(convert(sys.argv[1]), headers="keys", tablefmt="grid"))


def convert(file_path):
    list = []

    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames

        for row in reader:
            temp = {}

            for header in headers:
                temp[header] = row[header]

            list.append(temp)

    return list


if __name__ == '__main__':
    main()
