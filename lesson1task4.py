# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

user_number = int(input("Введите целое число: "))
result_number = user_number % 10
user_number = user_number // 10
while user_number > 0:
    if user_number % 10 > result_number:
        result_number = user_number % 10
    user_number = user_number // 10
print("Самое большое число = ", result_number)