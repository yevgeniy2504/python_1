# Создайте класс-генератор.
# -Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# -Если переданы два параметра, считаем step=1.
# -Если передан один параметр, также считаем start=1.

class GeneratorFactorial:
    def __init__(self, stop, start=1, step=1):
        if start > stop:
            self.start = stop
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        result = 1
        for i in range(1, self.current + 1):
            result *= i
        self.current += self.step
        return result


if __name__ == '__main__':
    f_1 = GeneratorFactorial(4, 9, 2)
    for i in f_1:
        print(i)



