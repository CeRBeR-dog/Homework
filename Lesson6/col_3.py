"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""
d = {'one':11, 'two':22, 'hello':'python', True:False}

num = input("Введите номер элемента")

spis_zn = list(d.values())

num = spis_zn.index(num)

print(d)
del d[num]

print(d)