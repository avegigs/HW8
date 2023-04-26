from datetime import datetime, timedelta


def get_birthdays_per_week(users: dict):
    days_name = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    birthday_dict = {"Monday": [], "Tuesday": [],
                     "Wednesday": [],  "Thursday": [],  "Friday": []}

    today = datetime.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = today + timedelta(days=4-today.weekday())
    # week_end = week_start + timedelta(days=6)
    print(week_start, week_end)

    for user in users:
        birthday = user["birthday"]
        birthday = birthday.replace(year=today.year)
        # print(type(birthday))
        name = user["name"]
        if birthday.month == today.month:
            if birthday.day in range(week_start.day-2, week_end.day+1):
                # print(name)
                if birthday.weekday() < 5:
                    day_a = days_name.get(birthday.weekday())
                    birthday_dict[day_a].append(name)
                    # print(type(day_a))

                elif birthday.weekday() >= 5:
                    birthday_dict["Monday"].append(name)

    for key, values in birthday_dict.items():
        if values:
            print(f'{key}: ', end='')

            for value in values:

                print(f'{value}, ', end=' ')
            print()


users = [
    {'name': 'Alice', 'birthday': datetime(2023, 4, 24)},
    {'name': 'TOk', 'birthday': datetime(1974, 4, 24)},
    {'name': 'Bob', 'birthday': datetime(1985, 9, 1)},
    {'name': 'Charlie', 'birthday': datetime(1995, 4, 28)},
    {'name': 'David', 'birthday': datetime(1970, 2, 14)},
    {'name': 'Eve', 'birthday': datetime(1998, 7, 4)},
    {'name': 'Frank', 'birthday': datetime(1982, 4, 23)},
    {'name': 'Grace', 'birthday': datetime(2005, 4, 30)},
    {'name': 'Harry', 'birthday': datetime(1978, 6, 15)},
    {'name': 'Ivy', 'birthday': datetime(1992, 10, 10)},
    {'name': 'John', 'birthday': datetime(1965, 3, 8)},
    {'name': 'Karen', 'birthday': datetime(1987, 4, 29)},
    {'name': 'Larry', 'birthday': datetime(1990, 4, 28)},
    {'name': 'Mia', 'birthday': datetime(2002, 6, 7)},
    {'name': 'Nick', 'birthday': datetime(1975, 9, 27)},
    {'name': 'Olivia', 'birthday': datetime(1989, 12, 17)},
    {'name': 'Paul', 'birthday': datetime(1960, 7, 20)},
    {'name': 'Quinn', 'birthday': datetime(1997, 4, 26)},
    {'name': 'Rose', 'birthday': datetime(1994, 2, 2)},
    {'name': 'Sam', 'birthday': datetime(2001, 4, 22)},
    {'name': 'Tina', 'birthday': datetime(1973, 10, 5)}
]

get_birthdays_per_week(users)
