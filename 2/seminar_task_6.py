# -Начальная сумма равна нулю
# -Допустимые действия: пополнить, снять, выйти
# -Сумма пополнения и снятия кратны 50 у.е.
# -Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# -После каждой третей операции пополнения или снятия начисляются проценты - 3%
# -Нельзя снять больше, чем на счёте
# -При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
#     операцией, даже ошибочной
# -Любое действие выводит сумму денег

START_SUMM = 0
MIN_GIVEN_SUMM = 50
TRANSACTION_COST = 0.015
MIN_COST = 30
MAX_COST = 600
BONUS_QTY_TRANSACTIONS = 4
BONUS = 0.03
MAX_WEALTH = 5_000_000
MAX_WEALTH_PERCENT = 0.1

counter = 0
total = START_SUMM

def print_bonuses(summ, counter):
    if counter % BONUS_QTY_TRANSACTIONS == 0:
        summ *= BONUS
    else:
        summ = 0
    print(f"Вам начисленно {summ} у.е бонусов")
    return summ


def wealth_pay(summ):
    if summ > MAX_WEALTH:
        summ = summ - summ * MAX_WEALTH_PERCENT
    return summ


def add_money(summ):
    value = int(input("Введите сумму пополнения:  "))
    if value % MIN_GIVEN_SUMM == 0:
        summ += value
        return summ
    else:
        print(f"Сумма должна быть кратна {MIN_GIVEN_SUMM} у.е.")
        return summ


def withdraw(summ):
    comm_cost = summ * TRANSACTION_COST
    if comm_cost < MIN_COST:
        comm_cost = MIN_COST
    elif comm_cost > MIN_COST:
        comm_cost = MIN_COST
    value = int(input("Введите сумму списания:  "))
    if value % MIN_GIVEN_SUMM == 0:
        summ -= value
        return summ - comm_cost
    elif summ < 0:
        return 0
    else:
        print(f"Сумма должна быть кратна {MIN_GIVEN_SUMM} у.е.")
        return summ


def print_results(summ):
    print(f"На вашем счету {summ} у.е")
    return summ


while True:
    user_action = int(input("""Введите желаемую операцию
    0 - Выход
    1 - Пополнить
    2 - Снять
    ----------------------
    > """))
    if user_action == 0:
        counter += 1
        print("До скорых встреч")
        total = wealth_pay(total)
        print_results(total)
        print_bonuses(total, counter)
        break
    elif user_action == 1:
        counter += 1
        total = wealth_pay(total)
        total = add_money(total) + print_bonuses(total, counter)
        print_results(total)
    elif user_action == 2:
        counter += 1
        total = wealth_pay(total)
        total = withdraw(total) + print_bonuses(total, counter)
        print_results(total)
    else:
        print("Такой операции не существует")
        total = wealth_pay(total)
        print_results(total)
        print_bonuses(total, counter)


