"""
Может ли кортеж, содержащий список, быть ключом словаря? Почему?
"""
some_list = [1, 2, 3]
some_tuple = ([123], [12], 123, 'list', some_list)
print(some_tuple)
some_list.append(4)
print(some_tuple)

"""
Кортеж, содержащий список, не может быть ключом словаря. Поскольку подобный кортеж не может иметь хэш.
Несмотря на то, что в подобном кортеже сохраняется запрет на изменение элементов, фактически изменения произвести можно.
Например, как в примере, указанном выше.
В данном случае несмотря на то, что с кортежем мы не производим никаких действий, а лишь добавляем элемент в список,
мы получаем два разных кортежа на выходе:
([123], [12], 123, 'list', [1, 2, 3])
([123], [12], 123, 'list', [1, 2, 3, 4])
"""