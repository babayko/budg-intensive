from datetime import date


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            result = False
        else:
            result = True
    else:
        result = False
    return result


short_months = [4, 6, 9, 11]


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    year = some_date.year
    month = some_date.month
    day = some_date.day

    if month == 2 and is_leap_year(year) and day == 29:
        new_date = date(year, month+1, 1)
    elif month == 2 and day == 28 and not is_leap_year(year):
        new_date = date(year, month+1, 1)
    elif month == 12 and day == 31:
        new_date = date(year+1, 1, 1)
    elif month in short_months and day == 30:
        new_date = date(year, month + 1, 1)
    else:
        new_date = date(year, month, day+1)

    return new_date
