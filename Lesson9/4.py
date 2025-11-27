'''
Дан список [1,2,3,4,5,6,7,8,9]. Создать 3 копии этого списка 
и с каждой выполнить след действия:
    - возвести каждый элемент во 2ю степень
    - прибавить 3 к каждому элементу значение которого является четным 
    - элементы значения которого является 
            четными - умножить на 2 
            нечетным - умножить на 3

Использовать map и lambda.
'''


stand_list = [1,2,3,4,5,6,7,8,9]
print(stand_list)

sqr_list = list(map(lambda x: x**2, stand_list))
print(sqr_list)

add_3_even_list = list(map(lambda x: x+3 if x % 2 == 0 else x , stand_list))
print(add_3_even_list)

diff_list = list(map(lambda x: x*2 if x % 2 == 0 else x*3 , stand_list))
print(diff_list)