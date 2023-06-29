# Изменяем класс прямоугольника.
# 📌Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.


class SizeValidator:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Значение должно быть положительным")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Rectangle:
    a = SizeValidator()
    b = SizeValidator()

    def __init__(self, a, b=None):
        self.a = a
        self.b = b if b is not None else self.a

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def add(self, other):
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __str__(self):
        return f"Прямоугольник со сторонами {self.a} и {self.b}"

    def sub(self, other):
        new_perimeter = self.perimeter() - other.perimeter()
        new_a = min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)


if __name__ == '__main__':
    rect = Rectangle(5, 10)
    print(rect.a)
    print(rect.b)

    rect.a = -7


