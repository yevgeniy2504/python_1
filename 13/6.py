# Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
# 📌Передавайте необходимые данные из основного кода
# проекта.

class UserExept(Exception):
    pass


class LevelError(UserExept):
    pass


class AccessError(UserExept):
    def __init__(self, user_name, access_level):
        self.user_name = user_name
        self.access_level = access_level
        super().__init__(f"Доступ ограничен для пользователя '{user_name}' имеет следующий доступ {access_level}")


def check_level(level):
    if level < 1 or level > 10:
        raise LevelError("Недопустимый уровень!")


def check_access(user):
    if user != "admin":
        raise AccessError(user, "Нет доступа!")


if __name__ == '__main__':
    try:
        check_level(15)
    except LevelError as e:
        print("Ошибка уровня:", str(e))

    try:
        check_access("guest")
    except AccessError as e:
        print("Ошибка доступа:", str(e))
