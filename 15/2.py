# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# 📌Напишите аналогичный декоратор, но внутри используйте
# модуль logging.


import logging
import json


def save_to_json(func):
    def wrapper(*args):
        result = func(*args)
        logging.info(f"Функция {func.__name__} Входные данные: {args}, Получен результат: {result}")
        with open('new_json.json', 'a') as jsonf:
            json.dump(result, jsonf)

    return wrapper


@save_to_json
def solve_quadratic_equation(a: int, b: int, c: int):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None, None
    elif D == 0:
        x = -b / (2 * a)
        return x, None
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return x1, x2


if __name__ == '__main__':
    logging.basicConfig(filename='log.txt', level=logging.INFO)
    FORMAT = "{asctime} - {message}"
    solve_quadratic_equation(5, 6, 1)
