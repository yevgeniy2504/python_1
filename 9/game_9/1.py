
def solve_quadratic_equation(a: int, b: int, c: int) -> None | tuple[float, float]:
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None
    elif D == 0:
        x = -b / (2 * a)
        return x, x
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return x1, x2


if __name__ == '__main__':
    print(solve_quadratic_equation(2, 19, 1))
