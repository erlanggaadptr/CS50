from datetime import date
import inflect
import re
import sys


def main():
    p = inflect.engine()

    duration = date.today() - get_date(input("Date of Birth: "))

    duration_total_minutes = int(duration.total_seconds() / 60)
    string = ", ".join(p.number_to_words(duration_total_minutes, wantlist=True)).capitalize()

    print(re.sub(r"\band\s*", "", string), "minutes")


def get_date(birthdate):
    try:
        return date.fromisoformat(birthdate)

    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
