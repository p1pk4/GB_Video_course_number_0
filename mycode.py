#import this
#строка
proposal = 'Для тех кто не в курсе, Пайтон самый легкий ЯП в освоении!!!11'

#Числа
one_digit = 100
second_digit = 0.2
third_digit = -1.3

print(str(one_digit) + ' раз можно повторить: ' + proposal)

#Список. Элемент списка начинается с 0
my_list = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 2.0, -14, True, 'word']
print(my_list[7])
#Индекс -1 выведет последний элемент из списка ('word')
print(my_list[-1])

'''
#Цикл
for word in proposal:
    print(word)
'''

count_my_list = len(my_list)
print(count_my_list)

#x = ''
#my_list.count(x)
#my_list.append(proposal)

print(my_list)


result = (one_digit ** (second_digit * third_digit))
print(result)