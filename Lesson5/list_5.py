'''
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''

l_mar = ['samsung', 'lg', 'xerox', 'bosch']

l_mar.remove('xerox')
print(l_mar)

l_mar.insert(1, 'indesit')
print(l_mar)