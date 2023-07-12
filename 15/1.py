import logging


def divide_numbers(x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError as e:
        logging.error(str(e))


logging.basicConfig(
    filename="log.log",
    encoding='utf-8',
    format='{asctime} {levelname} {funcName}->{lineno}: {msg}',
    style='{',
    level=logging.WARNING
)

# Пример использования функции
result = divide_numbers(10, 0)
print("Результат:", result)
