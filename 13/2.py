# Создайте функцию аналог get для словаря.
# 📌Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# 📌При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# 📌Реализуйте работу через обработку исключений.

def get_dict_value(dictionary, key, default_value=None):
    try:
        value_ = dictionary[key]
        return value_
    except KeyError:
        return default_value


if __name__ == '__main__':
    my_dict = {"apple": 1, "banana": 2, "orange": 3}
    value = get_dict_value(my_dict, "banana", "No value")
    print("Значение для ключа 'banana':", value)
    value = get_dict_value(my_dict, "grape", "No value")
    print("Значение для ключа 'grape':", value)


