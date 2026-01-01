'''
Запросить 3 раза строку из нескольких чисел через пробел
    - вывести все уникальные числа по возрастанию
    - вывести числа которые есть в каждой строке
    -* вывести числа которые есть только в одной из трех строк
    
    выполнить без циклов и условий
    
    пример:
    >>> 1 2 11 22
    >>> 1 2 22 33
    >>> 1 2 33 44


    1) 1 2 11 22 33 44
    2) 1 2
    3) 11 44
    
'''


phrase = 'Введите через пробел числа: '

str_1 = set(map(int, (input(phrase).split())))
str_2 = set(map(int, (input(phrase).split())))
str_3 = set(map(int, (input(phrase).split())))

# print(str_1)
# print(str_2)
# print(str_3)

# str_union = set.union(str_1, str_2, str_3)
# print(str_union)

# str_difference = set.difference(str_1, str_2, str_3)
# print(str_difference)

str_uno = (str_1 - str_2 -str_3 | str_2 - str_1 - str_3 | str_3 - str_1 -str_2)
print(str_uno)