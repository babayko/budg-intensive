В рамках 9-го дня будет производиться работа с проектом https://github.com/sandanilenko/peerocks
Нужно будет развернуть проект на локальной машине и выполнить ряд заданий:

1. Вывести список всех рецептов. Список должен содержать информацию о самом рецепте, авторе;
2. Вывести детальную информацию рецепта. Нужно получить информацию о самом рецепте, о шагах приготовления, списке
    необходимых продоктов для приготовления;
3. Вывести список рецептов, аналогичный заданию 1, только дополнительно должно быть выведено количество лайков. Сам
    список должен быть отсортирован по количеству лайков по убыванию;
4. Вывести объединенный список TOP 3 авторов и TOP 3 голосующих с количеством рецептов для первых и количеством
    голосов для вторых. В выборке должен быть указан тип в отдельной колонкке - Автор или Пользователь;
5. Все продукты указаны для приготовления одной порции блюда. Необходимо вывести список необходимых продуктов для
    приготовления самостоятельно выбранного блюда в количестве 5-ти порций.

Все запросы должны быть реализованы в соотвествующих вьюхах в peerocks/peerocks/apps/common/views.py

Для удобства работы и проверки был подключен django-debug-toolbar.