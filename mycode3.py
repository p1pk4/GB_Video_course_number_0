#ввести с клавы цифры или буквы, добавить ввод в список. Если введены буквы, сравнить с дефольным списком цифр
#и наоборот и сравнить их в цикле

#Пользовательский ввод списков 
digitals = [int(i) for i in input('Введите цифры через пробел(не по порядку): ').split()]
words = [str(f) for f in input('Введите буквы через пробел(не по порядку): ').split()]

#Сортировка списков
digitals.sort()
words.sort()

#Прибавляет или отнимает еденицу от значения в индексах в списке цифр
if len(digitals) < 10:
    for digital in digitals:
        #Пользователь вводит элементы списка пока список не станет равен 15, потом break
        digitals.append(input()) #+= input(digitals.append) #+= 1
        print(digitals)
        if digitals == 15:
            break
#count запихнуть
elif len(digitals) > 15:
    for digital in digitals:
        digital -= 1
        print(digitals)

#Ветвление списков
if len(digitals) == len(words):
    print('Список цифр {} и список букв {} равны'.format(digitals, words))
elif len(digitals) > len(words):
    print('Вы ввели цифры: {} и этот список длиннее списка букв'.format(digitals))
elif len(digitals) < len(words):
    print('Список букв {} длиннее чем список с цифрами'.format(words))

