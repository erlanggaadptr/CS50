MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date_input = input("Date: ").strip()
        date_split = date_input.split()

        if len(date_split) == 1:
            date_split = date_input.split('/')
            month, day, year = date_split

        elif len(date_split) == 3:
            month, day, year = date_split

            if ',' in day:
                day = day[:-1]

            else:
                raise ValueError

            month = MONTHS.index(month) + 1

        else:
            raise ValueError

        if int(month) > 12 or int(day) > 31:
            raise ValueError

        break

    except ValueError:
        pass

day = str(day).zfill(2)
month = str(month).zfill(2)

print(f"{year}-{month}-{day}")
