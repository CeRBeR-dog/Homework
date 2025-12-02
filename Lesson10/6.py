"""
Написать генератор triangular_numbers, который возвращает подряд 
треугольные числа

Формула:
Tn = 1 / 2 * n * (n + 1)

Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""


def triangular_numbers() :
    
    tn = 1
    n = 1
    while True:
        yield tn
        tn = 1/2*n*(n+1)
        n += 1
       

if __name__ == '__main__':
    
    triangular_gen = triangular_numbers()

    num = int(input("Введите количество чисел которое хотетие вывести: "))

    for i in range(num):
        print(next(triangular_gen))