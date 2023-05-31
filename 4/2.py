# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов

init_list = [1, 1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9, ]


def remove_repeated_numbers(elem):
    """
    Проверяет есть ли повторения числа в глобальном списке, возвращает число если нет повторений
    """
    global init_list
    if init_list.count(elem) == 1:
        return elem


print(*(filter(remove_repeated_numbers, init_list)))
