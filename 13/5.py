# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# 📌загрузка данных (функция из задания 4)
# 📌вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# 📌добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.Погружение в Python


from task_3 import UserExept, AccessError, LevelError
from task_4 import read_users_from_json


class Project:
    def __init__(self, users):
        self.users = users

    def load_data(self, file_name):
        self.users = read_users_from_json(file_name)

    def login(self, name, id):
        user = User(name, id, 0)
        if user in self.users:
            for u in self.users:
                if u == user:
                    return u.access_level
        else:
            raise AccessError("Доступ запрещен!")

    def add_user(self, user):
        for u in self.users:
            if user.access_level < u.access_level:
                raise LevelError("Недостаточный уровень доступа!")
        self.users.add(user)


if __name__ == '__main__':
    project = Project("User")
    project.load_data(file_name)
    project.login(name, id)
    project.add_user(user)

