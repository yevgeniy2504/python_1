# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.


class Rectangle:
    """Класс "Прямоугольник" """

    __slots__ = ('_a', '_b')

    def __init__(self, a: int, b: int = None):
        """Конструктор класса, который принимает два аргумента:
         a и b (ширина и высота прямоугольника соответственно).
          Если аргумент b не передан, то он принимает значение a"""
        self._a = a
        self._b = b if b is not None else self._a

    @property
    def a(self):
        """Геттер для свойства a"""
        return self._a

    @a.setter
    def a(self, value):
        """Сеттер для свойства a"""
        self.validate(value)
        self._a = value

    @property
    def b(self):
        """Геттер для свойства b"""
        return self._b

    @b.setter
    def b(self, value):
        """Сеттер для свойства b"""
        self.validate(value)
        self._b = value

    def validate(self, value):
        """Метод для проверки допустимых значений"""
        if value < 0:
            raise ValueError("Значение должно быть неотрицательным")

    def area(self) -> int:
        """Возвращает площадь прямоугольника."""
        return self._a * self._b

    def perimeter(self) -> int:
        """Метод, который возвращает периметр прямоугольника."""
        return 2 * (self._a + self._b)

    def add(self, other):
        """Метод, который перегружает оператор сложения (+)."""
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self._a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __str__(self):
        """Метод, который возвращает строковое представление прямоугольника."""
        return f"Прямоугольник со сторонами {self._a} и {self._b}"

    def sub(self, other):
        """Метод, который перегружает оператор вычитания (-)"""
        new_perimeter = self.perimeter() - other.perimeter()
        new_a = min([self._a, self._b, other._a, other._b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)


if __name__ == '__main__':
    rect = Rectangle(5, 3)
    print(rect.a)
    print(rect.b)

    rect.a = 7
    rect.b = 4
    print(rect.a)
    print(rect.b)
    print(Rectangle.__dict__)


