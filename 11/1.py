# -Создайте класс Моя Строка, где:
# -будут доступны все возможности str
# -дополнительно хранятся имя автора строки и время создания
# -(time.time)


import time


class MyString(str):
    """ Расширение класса str. """

    def __new__(cls, value: str, name: str):
        """ Добавление в метод параметры value и number. """
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time.time()
        return instance

    def __init__(self, value: str, name: str):
        self.value = value
        self.name = name

    def __str__(self):
        return f'Значение = "{self.value}", Имя = "{self.name}"'

    def __repr__(self):
        return f'MyString({self.value}, "{self.name}")'


if __name__ == '__main__':
    mystr = MyString('Сама строка', 'Жан-Клод Ван дам')
    print(mystr.name)
    print(mystr.created_at)
    print(mystr)
    print(mystr.upper())
    print(mystr.isalpha())
    help(MyString)
