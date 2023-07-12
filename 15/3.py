# Доработаем задачу 2.
# 📌Сохраняйте в лог файл раздельно:
# ○уровень логирования,
# ○дату события,
# ○имя функции (не декоратора),
# ○аргументы вызова,
# ○результат.


import logging
import json


FORMAT = "{levelname} - {asctime}: {msg}"
logging.basicConfig(
    format = FORMAT,
    filename="log.log",
    encoding='utf-8',
    style='{',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def deco_logger(func):
    def wrapper(*args):
        result = func(*args)
        logging.info(f"Функция {func.__name__} Входные данные: {args}, Получен результат: {result}")
    return wrapper


@deco_logger
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
    solve_quadratic_equation(5, 6, 1)
