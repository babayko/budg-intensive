def convert_temperature(value, to_scale):
    """Конвертирует температуру в нужную системы счисления

    Args:
        value: значение температуры
        to_scale: система счисления, в которую нужно конвертировать значение

    Returns: значение как результат конвертации
    """
    if to_scale == 'F':
        fah = (9 / 5 * value) + 32
        return fah
    elif to_scale == 'C':
        cel = 5 * (value - 32) / 9
        return cel
    else:
        return value
