""" Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами. """

from sys import argv


path, prod_hours, rate_hours, user_prize = argv
prod_hours = int(prod_hours)
rate_hours = int(rate_hours)
user_prize = int(user_prize)

print("Путь ", argv)
print("Выработка в часах: ", prod_hours)
print("Ставка в час: ", rate_hours, "Эльфийских пряников")
print("Премия: ", user_prize, "Эльфийских пряников")


def my_accounting():
    global prod_hours
    global rate_hours
    global user_prize
    user_salary = (prod_hours * rate_hours) + user_prize

    return f"Зарплата нашего единственого сотрудника, Джона. Составила: {user_salary} - Эльфийских пряников"


print(my_accounting())
