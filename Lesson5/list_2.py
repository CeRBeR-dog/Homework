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

spis_name.sort()
print(spis_name)

spis_low = list(map(str.lower,spis_name))
print('Имя Вася:', 'вася' in spis_low)
