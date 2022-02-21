"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))

# Тут будет выведено Test message и None. Внутри функции transmit_to_space определяется и вызывается функция
# data_transmitter. Поскольку data_transmitter не принимает никаких аргументов, то при вызове принта она начинает
# поиск в следующей области видимости - функции transmit_to_space. Там находит нужню переменную и передает ее в принт.
# Но поскольку сама функция transmit_to_space ничего не возвращает, то и при выводе ее в консоль выходит None.
