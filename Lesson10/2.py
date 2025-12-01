
"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial ():
    
    f, n = 1, 1
    
    while True:
         f *= n
         yield f
         n += 1


if __name__ == '__main__':
    
    factorial_gen = factorial()

    num = int(input("Введите количество факториалов которое хотетие вывести: "))

    for i in range(num):
        print(next(factorial_gen))
