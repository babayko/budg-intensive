from day_2.common import MyException
import time


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """

    def fist_wrapper(func):
        def wrapper():
            for i in range(times):
                try:
                    result = func()
                    break
                except AssertionError:
                    time.sleep(delay)
                    continue
            else:
                raise MyException('Превышено число попыток вызова функции')
            return result
        return wrapper
    return fist_wrapper
