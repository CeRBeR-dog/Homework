"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):

    if not all(isinstance(arg, int) for arg in args):
        raise TypeError("Все позиционные аргументы должны быть целыми")
    
    if not all(isinstance(kwarg, str) for kwarg in kwargs.values()):
        raise TypeError("Все позиционные аргументы должны быть строками")
    
    args_sum = sum(args)

    kwargs_max_len = max((len(val) for val in kwargs.values()), default=0)

    return {
        "args_sum": args_sum,
        "kwargs_max_len": kwargs_max_len
        }


test_dict = dict_from_args(1 ,2 , 3, 4, name = 'Vasya', second_name = "Ivanov")
print(test_dict)
