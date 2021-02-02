""" Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce(). """

from functools import reduce


my_list = [el + 2 for el in range(100, 1000) if el % 2 == 0]
result = reduce(lambda res, x: res*x, my_list, 1)

print("Разработчик и хотел проверить получившийся результат, да помер пока считал :)", "\n", result)
