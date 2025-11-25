'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''
from pprint import pprint



def count_char(phr: str) -> dict:
    
    phr = list(phr)
    char_count ={}

    for char in phr:
        if  char not in char_count:
            char_count[char] = phr.count(char)
    
    pprint(char_count)


string = input("Введите строку: ")
count_char(string)