# Проверка двух ферзей по координатам, бьют друг друга или нет
def check_queens(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or (abs(x1-x2) == abs(y1 - y2)):
        return True
    return False

