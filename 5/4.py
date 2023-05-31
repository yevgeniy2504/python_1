# Создайте функцию генератор чисел Фибоначчи
import itertools


def fibonacci(len_fib):
    fib_1, fib_2 = 0, 1
    for _ in range(len_fib):
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2


print(list(fibonacci(10)))



