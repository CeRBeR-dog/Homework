'''

**

Есть список чисел: 
some_list = [111, 222, 333, 444, 555, 666, 777, 888, 999]. 

* Нужно преобразовать его в одну строку, где элементы списка 
    разделены '---'
    Результат:  
    111---222---333---444---555---666---777---888---999

** дополнительно каждый элемент списка разделить дефисом 
    образец: 111 -> 1-1-1 

    Результат:  
    1-1-1---2-2-2---3-3-3---4-4-4---5-5-5---6-6-6---7-7-7---8-8-8---9-9-9


не использовать for и lambda

'''

some_list = [111, 222, 333, 444, 555, 666, 777, 888, 999]

print(*some_list, sep='---')

a, b, c, d, e, f, g, w, h = some_list

a = str(a)
a = list(map(str, a))
a = '-'.join(a)

b = str(b)
b = list(map(str, b))
b = '-'.join(b)

c = str(c)
c = list(map(str, c))
c = '-'.join(c)

d = str(d)
d = list(map(str, d))
d = '-'.join(d)

e = str(e)
e = list(map(str, e))
e = '-'.join(e)

f = str(f)
f = list(map(str, f))
f = '-'.join(f)

g = str(g)
g = list(map(str, g))
g = '-'.join(g)

w = str(w)
w = list(map(str, w))
w = '-'.join(w)

h = str(h)
h = list(map(str, h))
h = '-'.join(h)

some_list_1 = [a, b, c, d, e, f, g, w, h]
print(*some_list_1, sep='---')