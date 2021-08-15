'''
1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
'''

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 5, 12, 4]

my_list_1 = set(my_list_1)
my_list_2 = set(my_list_2)

print(my_list_1 - my_list_2)

#winners
print('СОРЕВНОВАНИЯ ПО PYTHON!!!')
count = int(input('Введите количество участников: '))
i = count
members = []

while i > 0:
    name = input('Кто занял {} место: '.format(i))
    members.append(name)
    i -= 1

print('В соревновании учавствовали: ', members)
members.reverse()
result = members[:3]
result = 'Победители: {}. Поздравляем!'.format(result)
print(result)
