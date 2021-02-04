""" Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке. """

with open("my_file_lesson5_task_2.txt", 'w+', encoding="utf-8") as my_f_2:
    my_f_2.writelines([f"{[1,2,3,4,5,6,7,8,9]}\n Привет\n как твои дела?\n", "Hi, world"])
with open("my_file_lesson5_task_2.txt", "r", encoding="utf-8") as my_f_2:
    lines = 0
    letters = 0
    for line in my_f_2:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} букв в строке")
    print(f"Количество строк {lines}")
