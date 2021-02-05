""" Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл. """


trans_rus = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
out_file = []
with open("my_file_lesson5_task_4.txt", 'r', encoding="utf-8") as my_f_4:
    print("Вывод содержания файла до изменений")
    cont = my_f_4.read().split("\n")
    print(cont)
    my_f_4.seek(0)
    for i in my_f_4:
        i = i.split(" ", 1)
        out_file.append(trans_rus[i[0]] + " " + i[1])

with open("out_file_task4.txt", "w") as file_out:
    file_out.writelines(out_file)

with open("out_file_task4.txt", "r") as my_f_4:
    print("Вывод содержания файла после изменений")
    cont = my_f_4.read().split("\n")
    print(cont)