from math import sqrt

def great_comprehension(list1, list2, list3):
    """
    Возвращает список с перемноженными элементами списков list1, list2 и list3 согласно условию
    """
    return [x % 10 * 2 * int(sqrt(y)) * z
            for x in list1
            for y in list2
            for z in list3
            if (str(x)[0] == str(x)[-1] and x > 2)
            and (99 < y < 1000 and y % 2 == 0)
            and (z == 4 or z % 2 == 1)]
