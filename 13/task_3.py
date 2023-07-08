# Создайте класс с базовым исключением и дочерние классы-
# исключения:
# ○ошибка уровня,
# ○ошибка доступа.


class UserExept(Exception):
    pass


class LevelError(UserExept):
    pass


class AccessError(UserExept):
    pass


def check_level(level):
    if level < 1 or level > 10:
        raise LevelError("Недопустимый уровень!")


def check_access(user):
    if user != "admin":
        raise AccessError("Нет доступа!")


if __name__ == '__main__':
    try:
        check_level(15)
    except LevelError as e:
        print("Ошибка уровня:", str(e))

    try:
        check_access("guest")
    except AccessError as e:
        print("Ошибка доступа:", str(e))
