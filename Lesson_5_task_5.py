""" Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран. """

from random import randint

with open("my_file_lesson5_task_5.txt", 'x', encoding="utf-8") as my_f_5:
    my_list = [randint(1, 100) for _ in range(100)]
    my_f_5.write (" ".join(map(str, my_list)))

print(f"Сумма всех чисел в моем листе - {sum(my_list)}")



