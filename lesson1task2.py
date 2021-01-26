# Урок №1 - Задание №2 (Lesson №1 - Task №2)
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк..
# (The user enters the time in seconds. Convert the time into hours, minutes and seconds and output in the format
# hh: mm: ss. Use string formatting.)

# Запрашиваем у пользователя ввести число секунд (We ask the user to enter the number of seconds)

print("Привет, Это программа перевода секунд в часовой формат")
user_seconds = int(input("Введите время в секундах: "))

hh = int(user_seconds / 3600)
mm = int(user_seconds % 3600 / 60)
ss = int(user_seconds % 3600 % 60)
print(f"Ваши секунды, переведены в часвой формат = {hh:02}:{mm:02}:{ss:02}") # Вариант решения 1
print("Ваши секунды, переведены в часвой формат = ", "%02d:%02d:%02d" % (hh,mm,ss)) # Вариант решения 2