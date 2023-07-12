# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# 📌Соберите информацию о содержимом в виде объектов namedtuple.
# 📌Каждый объект хранит:
# 📌
# ○имя файла без расширения или название каталога,
# ○расширение, если это файл,
# ○флаг каталога,
# ○название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.


import os
import logging
from collections import namedtuple

FORMAT = "{levelname} - {asctime}: {msg}"
logging.basicConfig(
    format=FORMAT,
    filename="log.log",
    encoding='utf-8',
    style='{',
    level=logging.ERROR
)

logger = logging.getLogger(__name__)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_file_info(path):
    try:
        file_info_list = []
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isfile(full_path):
                name, extension = os.path.splitext(item)
                file_info = FileInfo(name, extension, False, os.path.basename(path))
                file_info_list.append(file_info)
            elif os.path.isdir(full_path):
                file_info = FileInfo(item, '', True, os.path.basename(path))
                file_info_list.append(file_info)
        return file_info_list
    except Exception as e:
        logging.error(f"Не удалось получить информацию о файле для пути: {path}. Ошибка: {str(e)}")
        return None


if __name__ == '__main__':
    path = input("Введите путь к директории: ")
    file_info_list = get_file_info(path)
    if file_info_list:
        with open('file_info.txt', 'w') as file:
            for file_info in file_info_list:
                file.write(f"Имя: {file_info.name}, Расширение: {file_info.extension}, "
                           f"Это директория: {file_info.is_directory}, Родительская директория: {file_info.parent_directory}\n")
        logging.info(f"Информация о файлах сохранена в file_info.txt")
    else:
        print(f"Не удалось получить информацию о файле для пути: {path}")
