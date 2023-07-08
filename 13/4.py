# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# 📌Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# 📌Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.


import os
import json
import csv
import pickle

path_ = "/home/yevgeniy/Рабочий стол/"


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


class User:
    def __init__(self, name, id, access_level):
        self.name = name
        self.id = id
        self.access_level = access_level


def read_users_from_json(file_path):
    users = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for user_data in data:
            name = user_data['name']
            id = user_data['id']
            access_level = user_data['access_level']
            user = User(name, id, access_level)
            users.add(user)
    return users


if __name__ == '__main__':
    file_path = 'users.json'
    users = read_users_from_json(file_path)
    for user in users:
        print(f"Name: {user.name}, ID: {user.id}, Access Level: {user.access_level}")
