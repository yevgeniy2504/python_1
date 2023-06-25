# -Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# -При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# -list-архивы также являются свойствами экземпляра


class Archive:
    """Принимает два значения число и строку
    Все данные экземпляров сохраняются в архив"""

    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        """Принимает значения value, и number """
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        self.number = number
        self.value = value

    def __str__(self):
        return f'Номер = {self.number}, значение - "{self.value}"'

    def __repr__(self):
        return f'Archive({self.number}, "{self.value}")'


if __name__ == '__main__':
    a_1 = Archive(1, 'One')
    print(f"{a_1.numbers = }, {a_1.values = }")
    a_2 = Archive(2, "two")
    print(f"{a_2.numbers = }, {a_2.values = }")
    a_3 = Archive(3, "three")
    print(f"{a_3.numbers = }, {a_3.values = }")
    print(a_3.__repr__())
    print(f'{a_1 = }')
    print(f'{a_1}')
