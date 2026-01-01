"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""


a1 = 2
a2 = 3.3
a3 = 4
a4 = 5.5

type_float = type(a1) == float and type(a2) == float and type(a3) == float and type(a4) == float
one_is_str = type(a1) == str or type(a2) == str or type(a3) == str or type(a4) == str
one_is_pair_int = (type(a1) == int and type(a3) == int) or (type(a2) == int and type(a4) == int) or (type(a3) == int and type(a4) == int)

if type_float:
    print("все они дробные числа", type_float)

if one_is_str:
    print("одна из них строка", one_is_str)

if one_is_pair_int:
    print("одна пара переменных является целочисленным типом", one_is_pair_int)