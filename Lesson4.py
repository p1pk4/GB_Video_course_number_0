'''
friends = 'Mike Donna'
print(friends)

#Поиск заданных символов в строке
print(friends.find('Donna'))

#Разделяет строки и делает из них список
print(friends.split())

#Проверяет состоит строчка из чисел или нет
print(friends.isdigit())

#Приводит все буквы к верхнему регистру
print(friends.upper())

#Приводит все буквы к нижнему регистру
print(friends.lower())
'''

top5 = 'Первые 5 мест на соревнованиях: 1. Иванов 2. Петров 3. Сидоров 4. Зиньгельрман 5. Тревор'
start = top5.find('1')
end = top5.find('4')
top3 = top5[start: end]
result = print('Поздравляем {}с успехом!'.format(top3.upper()))



hero = 'Superman'
if hero.find('man') != -1:
    print('Есть')

#Более красивый код

hero = input()
if 'man' in hero:
    print('Какой-то код')
else:
    print('Совпадений нет')