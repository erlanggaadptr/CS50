import re


def main():
    print(convert(input("Hours: ").strip()))


def validate(s):
    if matches := re.search(r"^(1[0-2]|[1-9])(?::([0-5][0-9]))?\s(AM|PM)\s(?:to)\s(1[0-2]|[1-9])(?::([0-5][0-9]))?\s(AM|PM)$", s):
        return True, matches

    return False, matches


def convert(s):
    is_validated, matches = validate(s)

    if is_validated and matches:
        hours = [
            {f"hour": matches.group(i), "minute": matches.group(i + 1), "indicator": matches.group(i + 2)}
            for i in range(1, 7, 3)
        ]

        for i in range(len(hours)):
            if hours[i]["hour"] == "12" and hours[i]["indicator"] != "PM":
                hours[i]["hour"] = f"0{str(int(hours[i]['hour']) - 12)}"

            else:
                if hours[i]["indicator"] == "AM":
                    hours[i]["hour"] = f"0{hours[i]['hour']}"
                elif hours[i]["indicator"] == "PM" and hours[i]["hour"] != "12":
                    hours[i]["hour"] = str(int(hours[i]["hour"]) + 12)

            if not hours[i]["minute"]:
                hours[i]["minute"] = "00"

        start_hour = ' '.join(list([value for key, value in hours[0].items() if key != "indicator"])).replace(" ", ":", 1)
        end_hour = ' '.join(list([value for key, value in hours[1].items() if key != "indicator"])).replace(" ", ":", 1)

        return f"{start_hour} to {end_hour}"

    raise ValueError


if __name__ == "__main__":
    main()
