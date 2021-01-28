""" Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль. """

print("Программа деления целых числен, Вам нужно ввести 2 аргумента")

def result_func (*args):
    try:
        user_number_one = int(input("Введите первый аргумент:  "))
        user_number_two = int(input("Введите второй аргумент:  "))
        sub = user_number_one / user_number_two
    except ZeroDivisionError:
        return "Ошибка- Делить на 0 нельзя"
    except ValueError:
        return "Ошибка: Вы ввели один из аргументов, который не является числом!"
    return sub

print(result_func())



