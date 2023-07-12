# Создайте класс прямоугольник.
# -Класс должен принимать длину и ширину при создании
# экземпляра.
# -У класса должно быть два метода, возвращающие периметр
# и площадь.
# -Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:
    """Класс "Прямоугольник" """

    def __init__(self, a: int, b: int = None):
        """Конструктор класса, который принимает два аргумента:
         a и b (ширина и высота прямоугольника соответственно).
          Если аргумент b не передан, то он принимает значение a"""
        self.a = a
        self.b = b if b is not None else self.a

    def area(self) -> int:
        """Возвращает площадь прямоугольника."""
        return self.a * self.b

    def perimeter(self) -> int:
        """Метод, который возвращает периметр прямоугольника."""
        return 2 * (self.a + self.b)

    def __add__(self, other):
        """Метод, который перегружает оператор сложения (+)."""
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __str__(self):


    def __sub__(self, other):
        """Метод, который перегружает оператор вычитания (-)"""
        new_perimeter = self.perimeter() - other.perimeter()
        new_a = min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __eq__(self, other):
        return self.area() == other.area()

    # def __ne__(self, other):
    #     return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    # def __le__(self, other):
    #     return self.area() <= other.area()

    # def __gt__(self, other):
    #     return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()


if __name__ == '__main__':
    rect1 = Rectangle(4, 6)
    rect2 = Rectangle(11)
    print(f"{rect1.perimeter() = }, {rect1.area() = }")
    print(f"{rect2.perimeter() = }, {rect2.area() = }")
    res_sum = rect1 + rect2
    print(f"{res_sum.a = }, {res_sum.b =}")
    res_sub = rect1 - rect2
    print(f"{res_sub.a = }, {res_sub.b =}")
    print(rect1 == rect2)
    print(rect1 != rect2)
    print(rect1 < rect2)
    print(rect1 <= rect2)
    print(rect1 > rect2)
    print(rect1 >= rect2)
