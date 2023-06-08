# 1 Решить задачи, которые не успели решить на семинаре.
# 2 Напишите функцию группового переименования файлов. Она должна:
# 3 принимать параметр желаемое конечное имя файлов.
#   При переименовании в конце имени добавляется порядковый номер.
# 4 принимать параметр количество цифр в порядковом номере.
# 5 принимать параметр расширение исходного файла.
#   Переименование должно работать только для этих файлов внутри каталога.
# 6 принимать параметр расширение конечного файла.
# 7 принимать диапазон сохраняемого оригинального имени.
#   Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение. 3. Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами.

__all__ = ['rename_func', 'help_func']

import os

path_ = "c:/Users/ykarabekov/Desktop/gb/python/7/test/"


def rename_func(dir, needed_name, ext_old, ext_new, num_len=1, take_from=0, take_to=0):
    os.chdir(dir)
    counter_ = 1
        
    for path, inside_dir, files in os.walk(dir):
        for file in files:
            if take_from !=0 or take_to != 0:
                new_name = file[take_from: take_to] + needed_name + "_" + \
                    str(counter_).rjust(num_len, "0")                
            else:
                new_name = needed_name + "_" + str(counter_).rjust(num_len, "0")
                
            new_name = os.path.join(path, new_name) + '.' + ext_new
            check_ext = file.split(".")
            if check_ext[1] == ext_old and not(os.path.exists("new_name")):
                os.rename(os.path.join(path, file), new_name)
                counter_ += 1
            if counter_ == 1:
                return "No files to rename"
    return "It was " + str(counter_) + " файлов"

    
def _test_func():
    print("Тестовая функция")
    return None


def help_func():
    return _test_func()


if __name__ == "__main__":
    print(rename_func(path_, "new name", "txt", "txt", 2, 2, 7))


