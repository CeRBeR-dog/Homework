'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''


def fact(n: int) -> int:

    try:
        n = int(n)

    except (ValueError, TypeError):
        print("Не число")
    
    if n < 0:
        print("Отрицательное число")

    else:
        fac = 1
        for i in range(1, n+1):
            fac = fac * i
        
        print(fac)


num = input("Введите число: ")

fact(num)