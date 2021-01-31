""" Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль. """

print("Программа деления целых числен, Вам нужно ввести 2 аргумента")

def result_func (user_number_one, user_number_two):
    try:
        sub = user_number_one / user_number_two
    except ZeroDivisionError:
        return "Ошибка- Делить на 0 нельзя"
    except ValueError:
        return "Ошибка: Вы ввели один из аргументов, который не является числом!"
    return sub

print(result_func(int(input("Введите первый аргумент:  ")), int(input("Введите второй аргумент:  "))))



