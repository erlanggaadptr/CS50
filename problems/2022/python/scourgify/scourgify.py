import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        open(sys.argv[1])

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    students = scourge(sys.argv[1])

    with open(sys.argv[2], 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['first', 'last', 'house'])
        writer.writeheader()

        for student in students:
            writer.writerow({'first': student['first'], 'last': student['last'], 'house': student['house']})


def scourge(file_path):
    with open(file_path) as csvfile:
        rows = csv.DictReader(csvfile)
        list = []

        for row in rows:
            name = row["name"].split(", ")
            list.append({'first': name[1], 'last': name[0], 'house': row['house']})

        return list


if __name__ == '__main__':
    main()
