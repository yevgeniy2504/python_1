import csv


def solve_quadratic_equation_for_csv(func):
    def wrapper():
        with open('new_csv.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                a, b, c = row
                result = func(int(a), int(b), int(c))
                print(f"Equation {a}x^2 + {b}x + {c} = 0 has roots: {result}")

    return wrapper


@solve_quadratic_equation_for_csv
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
    print(solve_quadratic_equation())
