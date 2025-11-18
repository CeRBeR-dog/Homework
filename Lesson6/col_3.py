"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""
d = {'one':11, 'two':22, 'hello':'python', True:False}
print(d)

d_elm = list(d.keys())
elm = input("Введите элемента: ")

num_el = d_elm.index(elm)
print(num_el)

del d[elm]

print(d)