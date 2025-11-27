'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''


def factor(num: int) -> int:

    try:
        num = int(num)

    except ValueError:
        return ('Не число')
    
    if num < 0:
        return ('Отрицательное число или равно 0')
    
    # Остановка рекусрсии 
    elif num == 0:
        return 1
    
    return num*factor(num-1)

num = input("Введите число: ")

print(factor(num))

