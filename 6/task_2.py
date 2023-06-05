# Вам дана расстановка 8 ферзей на доске, определите, 
# есть ли среди них пара бьющих друг друга.
# Програма получает на вход 8 пар чисел, если ферзи не бьют друг друга верните 
# истину, а если бьют - ложь.

from check_queens import check_queens
from itertools import permutations

coordinates = [(1, 2), (4, 6), (8, 2), (8, 1), (7, 8), (1, 7), (3, 7), (3, 8), (4, 7), (8, 3), (4, 5), (6, 5), (3, 6), (4, 1), (7, 8), (4, 5)]


def check_8_combinations(coord):
    for f1, f2 in permutations(coord, 2):
        x1, y1 = f1
        x2, y2 = f2
        if not check_queens(x1, y1, x2, y2):
            return False

    return True


print(check_8_combinations(coordinates))
        
        
    




