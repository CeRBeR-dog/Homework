'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Алфавит считаем от 0. a-0, b-1, c-3 и т.д.
Например: 13520 -> bdfca.
'''

num = input('Введите любое число: ')

alph = "abcdefghij"     # Эти нам не подходят, klmnopqrstuvwxyz, так как цифры от 0-9  
result = ""

# проверка на число
try:
    num = int(num)

except ValueError:
    print ("Вы вели не число")

else:
    num = str(num)
    for dig in num:
        ind = int(dig)
        result += alph[ind]

print(result)
    
