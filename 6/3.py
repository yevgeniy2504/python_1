import random
from task_2 import check_8_combinations
from itertools import permutations


def find_4_good_positions():
    possible_positions = []

    for i in permutations(range(1, 8), 2):
        possible_positions.append(i)

    k = 0
    while k <= 3:
        l = 0
        while l < 7:
            comb = []
            for coord in random.sample(possible_positions, 8):
                comb.append(coord)
                l += 1
            if check_8_combinations(comb):
                print(comb)
                k += 1


find_4_good_positions()
