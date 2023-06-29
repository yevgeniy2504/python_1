# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# -Экземпляр должен запоминать последние k значений.
# -Параметр k передаётся при создании экземпляра.
# -Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.


class FactorialCalculator:
    def __init__(self, k):
        self.k = k
        self.history = {}

    def __call__(self, n):
        if n in self.history:
            return self.history[n]
        result = 1
        for i in range(1, n + 1):
            result *= i
        self.history[n] = result
        if len(self.history) > self.k:
            self.history.pop(list(self.history.keys())[0])
        return result

    def get_history(self):
        return self.history


if __name__ == '__main__':
    calculator = FactorialCalculator(3)
    print(calculator(5))
    print(calculator(3))
    print(calculator(4))
    print(calculator(5))
    print(calculator.get_history())
