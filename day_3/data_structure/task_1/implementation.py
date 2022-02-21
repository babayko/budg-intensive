class Tuple:
    """
    Создает неизменяемый объект, с упорядоченной структурой, методами count и index.
    При создание принимается последовательность объектов
    """
    def __init__(self, *args):
        self.obj = tuple(args)

    def __getitem__(self, key):
        return self.obj[key]

    def count(self, value):
        """
        Возвращает число раз появления value в объекте
        Args:
            value: Элемент число вхождения которого ищется в объекте
        """
        count = 0
        for item in self.obj:
            if item == value:
                count += 1
        return count

    def index(self, value):
        """
        Возвращает индекс первого вхождения элемента в объекте
        Args:
            value: Элемент индекс которого ищется в объекте
        """
        index = 0
        for item in self.obj:
            if item == value:
                result = index
                break
            else:
                index += 1
        else:
            raise ValueError
        return result
