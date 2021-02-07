""" Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка. """

my_f_2 = open("my_file_lesson5_task_1.txt", 'w', encoding="utf-8")
line = input('Введите текст \n')
while line:
    my_f_2.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f_2.close()


