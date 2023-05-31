# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
from typing import Tuple, Any

path_ = "/home/Desktop/python/firs_project/6/2.py"


def string_plit(text_: str) -> tuple:
    if "." in text_ and "/" in text_:
        *path, file_extension = text_.split("/")
        file, extension = file_extension.split(".")
        return "/".join(path), file, extension


print(string_plit(path_))
