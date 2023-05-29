from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
nb_of_attempts = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)
try_nb = 0
user_nb = None
print(f"Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT}")
while try_nb < nb_of_attempts:
    try_nb += 1
    user_nb = int(input("Введите число:  "))
    if user_nb == num:
        print(f"Вы угадали число - {user_nb} c {try_nb} попыток ")
        break
    elif user_nb > num:
        print("меньше")
    elif user_nb < num:
        print("больше")

if user_nb != num:
    print("Лузер")
