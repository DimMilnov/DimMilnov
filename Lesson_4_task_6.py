"""  Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения """

""" Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. 
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено. """

from itertools import count
from itertools import cycle

# Решение а)
for el in count(3):
    if el > 10:
       break
    else:
        print(el)


# Решение б)
"""c = 0
for el1 in cycle(int(1)):
    if el1 > 10:
        break
    print(el1)
    с += 1"""