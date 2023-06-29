# Доработаем задачу 1.
# -Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json


class FactorialCalculator:
    def __init__(self, k, filename):
        self.k = k
        self.history = {}
        self.filename = filename

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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        history = self.get_history()
        with open(self.filename, 'w') as f:
            json.dump(history, f)


if __name__ == '__main__':
    with FactorialCalculator(3, "my_json.json") as calculator:
        print(calculator(5))
        print(calculator(3))
        print(calculator(4))
        print(calculator(5))
        print(calculator.get_history())
