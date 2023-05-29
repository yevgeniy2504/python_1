# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction


def gcd_calc(v1, v2):
    while v1 != v2:
        if v1 > v2:
            v1 = v1 - v2
        else:
            v2 = v2 - v1
    return v1


# без проверки ввода - добропорядочный пользователь
first_digit = input("Введите первую дробь вид а/b :   ")
second_digit = input("Введите вторую дробь вид а/b :   ")

a, b = first_digit.split("/")
c, d = second_digit.split("/")

a = int(a)
b = int(b)
c = int(c)
d = int(d)
if b and d:
    if b == d:
        result_a = a + c
        result_b = b
        print("2")
    else:
        result_a = a * d + b * c
        result_b = b * d
        gcd_digit = gcd_calc(result_a, result_b)
        result_a /= gcd_digit
        result_b /= gcd_digit
else:
    print("некорректная дробь - деление на ноль ")
    print("6")


print(f"результат = {int(result_a)}/{int(result_b)}")

f1 = Fraction(a, b)
f2 = Fraction(c, d)
print(f"Проверка - {f1 + f2}")







