"""
*
Написать программу калькулятор которая предлагает 
ввести пример для решения пока пользователь не введет команду "стоп"
Программа должна решить пример и запросить следующий.
При вводе команды "стоп" программа завершается.
Поддерживаемые операции: + - * ** /
Пример:
    Введите пример или 'стоп' для завершения: 2 + 2
    Ответ: 4
    Введите пример или 'стоп' для завершения: 16 / 8
    Ответ: 2
    Введите пример или 'стоп' для завершения: 1651+
    Неправильный формат. Пример: '2 + 4'


eval() exec() нельзя
"""

import operator

example = " "
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow
}

print("Поддерживаемые операции: + - * ** /")

while example != "stop":
    
    example = input('Введите пример или "стоп" для завершения: ')

    if example.lower() == "stop":
        break

    try:
        first_var, sign, second_var = example.split(" ")
        first_var = int(first_var)
        second_var = int(second_var)

    except ValueError:
        print("Неправильный формат. Пример: '2 + 4'")
        continue
    
    if sign in operations:
        
        try:
            print(operations[sign](first_var, second_var))
        
        except ZeroDivisionError:
            print("Ошибка: деление на ноль")
        
    else:
        print("Такая операция пока не подерживается")