# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:02:03 2023

@author: ykarabekov
"""

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


path_ = "c:/Users/ykarabekov/Desktop/gb/python/"


def dir_to_dump(dir_: str):
    with (
            open('new_user.json', 'a', encoding='utf-8') as f,
            open('new_user_2.csv', 'a', encoding='utf-8') as f_2,
            open('my_dict.pickle', 'ab') as f_3
    ):
        csv_write = csv.writer(f_2, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for item_name in os.listdir(dir_):
            item_path = os.path.join(dir_, item_name)
            size = os.path.getsize(item_path)
            if os.path.isdir(item_path):
                dir_name = item_path.split('/')[-1]
                temp_dict = ['DIR', dir_name, size]
                json.dump(temp_dict, f)
                csv_write.writerow(temp_dict)
                pickle.dump(temp_dict, f_3)
                print(f"DIR: {dir_name}, size: {size}")                
                dir_to_dump(item_path)
            else:
                file_name = item_path.split("\\")[-1]
                temp_dict = ['FILE', file_name, size]
                json.dump(temp_dict, f)
                pickle.dump(temp_dict, f_3)
                csv_write.writerow(temp_dict)
                
                print('   FILE: ', file_name, "   size:", size)
            
            
            
              
            
            
            
            
        
        
         
if __name__ == "__main__":
    print(dir_to_dump(path_))
