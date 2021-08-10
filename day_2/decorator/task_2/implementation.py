from day_2.common import MyException


def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(value):
        if type(value) is int and value >= 0:
            result = func(value)
        else:
            raise MyException('Аргумент должен быть натуральным числом больше  нуля')
        return result

    return wrapper


def cache_result(func):
    """
    Декоратор обращается к словарю. Если находит там аргумент, то
    функция не производит вычисления а тут же отдает результат. Если же аргумента
    нет, то результат добавляется в словарь.
    """
    cache = {}

    def wrapper(value):
        if value in cache:
            result = cache[value]
        else:
            result = func(value)
            cache[value] = result
        return result

    return wrapper
