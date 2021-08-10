from day_2.common import MyException


TYPE_DATA = (int, float)
ZERO = 0


class Value:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if type(other) in TYPE_DATA:
            return self.value + other
        else:
            raise MyException('Ошибка сложения разных типов данных')

    def __sub__(self, other):
        if type(other) in TYPE_DATA:
            return self.value - other
        else:
            raise MyException('Ошибка вычетания разных типов данных')

    def __truediv__(self, other):
        if other == ZERO:
            raise MyException('Ошибка деления на ноль')
        elif type(other) in TYPE_DATA:
            return self.value / other
        else:
            raise MyException('Ошибка деления разных типов данных')

    def __mul__(self, other):
        if type(other) in TYPE_DATA:
            return self.value * other
        else:
            raise MyException('Ошибка умножения разных типов данных')
