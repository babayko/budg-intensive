
def counter(func):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """

    count = 0

    def wrapper(*args):
        nonlocal count
        func(*args)
        count += 1
        return count

    return wrapper
