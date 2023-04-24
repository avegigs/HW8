from datetime import datetime, timedelta


def get_birthdays_per_week(users):

    birthdays = {}
    today = datetime.now().date()
    monday = today - timedelta(days=today.weekday())

    for user in users:
        birthday = user['birthday'].date().replace(year=today.year)
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        weekday = birthday.weekday()

        if weekday >= 5:
            weekday = 0
        else:
            weekday += 1
        birthday_day = monday + timedelta(days=weekday)
        if birthday_day not in birthdays:
            birthdays[birthday_day] = []
        birthdays[birthday_day].append(user['name'])
    ordered_birthdays = sorted(birthdays.items(), key=lambda x: x[0])
    for day, names in ordered_birthdays:
        day_name = day.strftime('%A')
        print(f'{day_name}: {", ".join(names)}')


users = [
    {'name': 'Alice', 'birthday': datetime(2000, 4, 22)},
    {'name': 'Bob', 'birthday': datetime(1985, 9, 1)},
    {'name': 'Charlie', 'birthday': datetime(1995, 12, 31)},
    {'name': 'David', 'birthday': datetime(1970, 2, 14)},
    {'name': 'Eve', 'birthday': datetime(1998, 7, 4)},
    {'name': 'Frank', 'birthday': datetime(1982, 11, 23)},
    {'name': 'Grace', 'birthday': datetime(2005, 1, 30)},
    {'name': 'Harry', 'birthday': datetime(1978, 6, 15)},
    {'name': 'Ivy', 'birthday': datetime(1992, 10, 10)},
    {'name': 'John', 'birthday': datetime(1965, 3, 8)},
    {'name': 'Karen', 'birthday': datetime(1987, 5, 19)},
    {'name': 'Larry', 'birthday': datetime(1990, 8, 12)},
    {'name': 'Mia', 'birthday': datetime(2002, 6, 7)},
    {'name': 'Nick', 'birthday': datetime(1975, 9, 27)},
    {'name': 'Olivia', 'birthday': datetime(1989, 12, 17)},
    {'name': 'Paul', 'birthday': datetime(1960, 7, 20)},
    {'name': 'Quinn', 'birthday': datetime(1997, 11, 11)},
    {'name': 'Rose', 'birthday': datetime(1994, 2, 2)},
    {'name': 'Sam', 'birthday': datetime(2001, 4, 10)},
    {'name': 'Tina', 'birthday': datetime(1973, 10, 5)}
]

get_birthdays_per_week(users)
