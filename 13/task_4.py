# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# 📌Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# 📌Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.


import json


class User:
    def __init__(self, name, id, access_level):
        self.name = name
        self.id = id
        self.access_level = access_level


def read_users_from_json(file_name):
    users = set()
    with open(file_name, 'r') as file:
        data = json.load(file)
        for user_data in data:
            name = user_data['name']
            id = user_data['id']
            access_level = user_data['access_level']
            user = User(name, id, access_level)
            users.add(user)
    return users


if __name__ == '__main__':
    users = read_users_from_json('users.json')
    for user in users:
        print(user.name, user.id, user.access_level)
