# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# * Для дочерних объектов указывайте родительскую директорию.
# * Для каждого объекта укажите файл это или директория.
# * Для файлов сохраните его размер в байтах, а для директорий размер файлов
# в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет
# для работы с файлами разных форматов.

import os
import json
import csv
import pickle


class DirSize:

    def __init__(self, file_name_json, file_name_csv, file_name_pickle):
        self.file_name_json = file_name_json
        self.file_name_csv = file_name_csv
        self.file_name_pickle = file_name_pickle

    def dir_to_dump(self, dir_):
        with open(self.file_name_json, 'a', encoding='utf-8') as f, \
                open(self.file_name_csv, 'a', encoding='utf-8') as f_2, \
                open(self.file_name_pickle, 'ab') as f_3:
            csv_write = csv.writer(f_2, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for item_name in os.listdir(dir_):
                item_path = os.path.join(dir_, item_name)
                if not os.path.exists(item_path):
                    continue
                size = os.path.getsize(item_path)
                if os.path.isdir(item_path):
                    dir_name = item_path.split('\\')[-1]
                    temp_dict = ['DIR', dir_name, size]
                    json.dump(temp_dict, f)
                    csv_write.writerow(temp_dict)
                    pickle.dump(temp_dict, f_3)
                    print(f"DIR: {dir_name}, size: {size}")
                    self.dir_to_dump(item_path)
                else:
                    file_name = item_path.split("\\")[-1]
                    temp_dict = ['FILE', file_name, size]
                    json.dump(temp_dict, f)
                    pickle.dump(temp_dict, f_3)
                    csv_write.writerow(temp_dict)

                    print('   FILE: ', file_name, "   size:", size)
        return None


p1 = DirSize('new_user.json', 'new_user.csv', 'new_user.pickle')
p1.dir_to_dump('/home/yevgeniy/Рабочий стол/git/python_1')
