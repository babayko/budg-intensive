def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    dict_month = {
        'январь': 31,
        'февраль': 28,
        'март': 31,
        'апрель': 30,
        'май': 31,
        'июнь': 30,
        'июль': 31,
        'август': 31,
        'сентябрь': 30,
        'октябрь': 31,
        'ноябрь': 30,
        'декабрь': 31
    }
    days = 0
    if month in dict_month:
        days = dict_month[month]
    return days
