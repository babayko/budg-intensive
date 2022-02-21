def get_numbers():
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    list_num = []

    for num in range(1000, 2001):
        if (num % 7) == 0 and (num % 5) != 0:
            list_num.append(num)
    return list_num
