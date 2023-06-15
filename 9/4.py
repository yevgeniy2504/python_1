# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:07:24 2023

@author: ykarabekov
"""

import json


def save_to_json(func):
    def wrapper(*args):
        with open('new_json.json', 'a') as jsonf:
            json.dump(func(*args), jsonf)

    return wrapper


@save_to_json
def solve_quadratic_equation(a: int, b: int, c: int):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None, None
    elif D == 0:
        x = -b / (2 * a)
        return x, None
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return x1, x2


if __name__ == '__main__':
    solve_quadratic_equation(5, 6, 1)
