'''
Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать
строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной
строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''
def int_func (*args):
    word = input("Введите слово с маленькой буквы ")
    print(word.title())
    return
int_func()

# 2 Вариант
def my_func(a):
    my_word = a.split(' ')
    total = []
    for i in my_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total
print(my_func(a = input("Введите предложение, используя только маленькие буквы: ")))
