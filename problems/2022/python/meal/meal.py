def main():
    time = input("What time is it? ").strip()
    converted_time = convert(time)

    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")


def convert(time):
    time = time.split(":")
    hour = float(time[0])
    minute = float(time[1]) / 60
    return float(hour + minute)


if __name__ == "__main__":
    main()
