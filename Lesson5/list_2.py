'''
Запросить по очереди у пользователя 5 имен. Добавить все в список. 
Отсортировать. 
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
'''

zap = "Ведите имя: "

n1 = input(zap)
n2 = input(zap)
n3 = input(zap)
n4 = input(zap)
n5 = input(zap)

spis_name = [n1, n2, n3, n4, n5]

#Преобразуем все именна с большой буквы
spis_up = list(map(str.capitalize,spis_name))

spis_up.sort()
print(spis_up)

print('Имя Вася:', 'Вася' in spis_up)
