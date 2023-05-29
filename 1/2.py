print("Введите стороны треугольника:")
a = input('a = :  ')
b = input('b = :  ')
c = input('c = :  ')

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("треугольник равносторонний")
    elif a == b or b == c or c == a:
        print("треугольник равнобедренный")
else:
    print("треугольник не существует")
