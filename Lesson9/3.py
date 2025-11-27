
'''
Написать рекурсивную функцию, которая принимает 2 аргумента 
(целые числа - a и b) и высчитывает суммы всех чисел от a до b (включительно). 
Пример: a = 3, b = 5 -> 12 (3+4+5)
Пример: a = 5, b = 9 -> 35 (5+6+7+8+9)"

'''

def sum_2_arg(num1: int, num2: int) -> int:

    try:
        num1 = int(num1)
        num2 = int(num2)

    except ValueError:
        return ('Надо вести целое число!')
    

    # делаем чтобы num1 было меньше num2
    if num1 > num1:
       num1, num2 = num2, num1
    
    if num1 == num2:
        return num1
    
    return num1 + sum_2_arg(num1+1, num2)


num1 = input("Введите первый аргумент: ")
num2 = input("Введите второй аргумент: ")

print(sum_2_arg(num1, num2))