from datetime import date


def leap_year():
    leap_year_list = []
    for year in range(0, 2100, 4):
        if year % 100 == 0 and year % 400 != 0:
            continue
        leap_year_list.append(year)
    return leap_year_list


list_leap_year = leap_year()


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    short_month = [4, 6, 9, 11]

    year = some_date.year
    month = some_date.month
    day = some_date.day

    if month == 2 and year in list_leap_year and day == 29:
        new_date = date(year, month+1, 1)
    elif month == 2 and day == 28 and year not in list_leap_year:
        new_date = date(year, month+1, 1)
    elif month == 12 and day == 31:
        new_date = date(year+1, 1, 1)
    elif month in short_month and day == 30:
        new_date = date(year, month + 1, 1)
    else:
        new_date = date(year, month, day+1)

    return new_date
