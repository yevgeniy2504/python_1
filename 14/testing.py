# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# 📌
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○
# doctest,
# unittest,
# pytest.


import doctest
from rectangle import Rectangle
import unittest
import pytest


# 1. doctest:

def test_rectangle():
    """
    >>> rect = Rectangle(4, 6)
    >>> rect.area()
    24
    >>> rect.perimeter()
    20
    >>> rect2 = Rectangle(11)
    >>> rect2.area()
    121
    >>> rect2.perimeter()
    44
    """
    pass


# 2. unittest:

class TestRectangle(unittest.TestCase):
    def test_area(self):
        rect = Rectangle(4, 6)
        self.assertEqual(rect.area(), 24)

    def test_perimeter(self):
        rect = Rectangle(4, 6)
        self.assertEqual(rect.perimeter(), 20)

    def test_add(self):
        rect1 = Rectangle(4, 6)
        rect2 = Rectangle(11)
        res = rect1 + rect2
        self.assertEqual(res.a, 4)
        self.assertEqual(res.b, 9)

    def test_sub(self):
        rect1 = Rectangle(4, 6)
        rect2 = Rectangle(11)
        res = rect1 - rect2
        self.assertEqual(res.a, 4)
        self.assertEqual(res.b, -3)

    def test_eq(self):
        rect1 = Rectangle(4, 6)
        rect2 = Rectangle(11)
        self.assertFalse(rect1 == rect2)

    def test_lt(self):
        rect1 = Rectangle(4, 6)
        rect2 = Rectangle(11)
        self.assertTrue(rect1 < rect2)

    def test_ge(self):
        rect1 = Rectangle(4, 6)
        rect2 = Rectangle(11)
        self.assertTrue(rect1 >= rect2)


# 3. pytest:


def test_area():
    rect = Rectangle(4, 6)
    assert rect.area() == 24


def test_perimeter():
    rect = Rectangle(4, 6)
    assert rect.perimeter() == 20


def test_add():
    rect1 = Rectangle(4, 6)
    rect2 = Rectangle(11)
    res = rect1 + rect2
    assert res.a == 4
    assert res.b == 9


def test_sub():
    rect1 = Rectangle(4, 6)
    rect2 = Rectangle(11)
    res = rect1 - rect2
    assert res.a == 4
    assert res.b == -3


def test_eq():
    rect1 = Rectangle(4, 6)
    rect2 = Rectangle(11)
    assert not (rect1 == rect2)


def test_lt():
    rect1 = Rectangle(4, 6)
    rect2 = Rectangle(11)
    assert rect1 < rect2


def test_ge():
    rect1 = Rectangle(4, 6)
    rect2 = Rectangle(11)
    assert rect1 >= rect2


if __name__ == '__main__':
    unittest.main()
    doctest.testmod()
