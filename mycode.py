#import this
#строка
proposal = 'Для тех кто не в курсе, Пайтон самый легкий ЯП в освоении!!!11'

#Числа
one_digit = 100
second_digit = 0.2
third_digit = -1.3

print(str(one_digit) + ' раз можно повторить: ' + proposal)

#Список. Элемент списка начинается с 0
my_list = ['a', 'b', 'c', 1,1,1,1,1,1,1,1,'d', 'e', 1, 2, 3, 2.0, -14, True, 'word']
print(my_list[7])

#Индекс -1 выведет последний элемент из списка ('word')
print(my_list[-1])

#Длина списка
print(len(my_list))

#Срезы/слайсы списка
print(my_list[:5]) #c первого элемента списка до 5-1. [:5] или [0:5] = список с первого элемента до 5 минус 1. Всегда минус 1!
print(my_list[8:11]) #выведет 2.0, -14, True
print(my_list[1:]) #с b и до конца

#Изменение элементов в списке
my_list[-1] = 'Hello'
print(my_list)

#Index вернет положение индекса, например
print(my_list.index(-14)) #вернулось 9. Это 9й элемент в списке со значением -14
#Указать откуда начинаем поиск
print(my_list.index(-14, 13)) #Начнет искать элемент "-14" с индекса 13. После 13 индекса элемента -14 нет, вернет: -14 is not in list

#Метод count
print(my_list.count(1))#Выведет кол-во 1 в списке(-14) тоже посчитает!

#Метод sort
my_list1 = [2, 5, 2, 1, -0.3, 3, 4]
my_list1.sort()
print(my_list1)
    #sort наоборот
my_list2 = [1, 2, 3, 4, 5]    
my_list2.sort(reverse = True) #5,4,3,2,1
print(my_list2[:2])
    #Можно сортировать строки
my_list_names = ['Adam', 'Treho', 'Alex', 'Serega', 'Johny']
my_list_names.sort()
print(my_list_names)

#append добавляет элемент в список
my_list_names.append('Chavk')
print(my_list_names)

my_list1.append(123)
print(my_list1)
'''
#Цикл
for word in proposal:
    print(word)
'''

#count_my_list = len(my_list)
#print(count_my_list)

#x = ''
#my_list.count(x)
#my_list.append(proposal)

print(my_list)


result = (one_digit ** (second_digit * third_digit))
print(result)