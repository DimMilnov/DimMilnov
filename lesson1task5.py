# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

corp_profit = int(input("Введите выручку фирмы за год: "))
corp_cost = int(input("Введите расходы фирмы за год: "))
corp_result = corp_profit - corp_cost
if corp_result > 0:
    print("Фирма в этом году получила прибыль",corp_result,"Эльфийских пряников")
    corp_staff = int(input( "Введите кол-во сотрудников: "))
    corp_staff_result = float(corp_result / corp_staff)
    print("Прибыль фирмы на одного сотрудника сотавила: ", "%0.2f" % (corp_staff_result), "Эльфийских пряников")
elif corp_result == 0:
    print("Фирма вышла в 0")
else:
    print("Фирма ушла в минус", corp_result, "Эльфийских пряников")

