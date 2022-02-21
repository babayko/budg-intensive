from datetime import datetime


def time_execution(function):
    """
    Обертка, печатающая время выполнения функции.
    """

    def wrapper(*args):
        start_time = datetime.now()
        result = function(*args)
        print(datetime.now() - start_time)
        return result

    return wrapper
