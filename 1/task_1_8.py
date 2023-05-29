repeat = int(input('Введите число повторений:  '))
_ = 0
ADD_STRING = "**"
string = "*"

while _ < repeat:
    print(string.center(repeat*2))
    string = string + ADD_STRING
    _ += 1
