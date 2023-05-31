# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

employee = ["Антон", "Сергей", "Анна"]
salary = [100, 200, 400]
bonus = ["5%", "9%", "3%"]


def bonus_calculate(employee_list: list, salary_list: list, bonus_list: list) -> dict[str, float]:
    return {name: cost * float(percent.replace("%", ""))/100 for name, cost, percent in
            zip(employee_list, salary_list, bonus_list)}


print(bonus_calculate(employee, salary, bonus))
