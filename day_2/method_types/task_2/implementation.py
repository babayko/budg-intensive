from day_2.common import MyException


class ClassFather:

    registered_list = set()

    def __init__(self):
        self._name = None

    @classmethod
    def register(cls):
        if cls != ClassFather:
            cls.registered_list.add(cls)
        else:
            raise MyException('Объект не принадлежит родительскому классу')

    def get_name(self):
        if type(self) in self.registered_list:
            return self._name
        else:
            raise MyException('Объект не зарегистрирован или отсутствует')


class User1(ClassFather):

    def __init__(self):
        super().__init__()
        self._name = 'User1'


class User2(ClassFather):

    def __init__(self):
        super().__init__()
        self._name = 'User2'
