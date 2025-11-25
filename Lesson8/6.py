"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""


def yes_or_no(spis_num: str) -> list:
    
     # Проверка на целые числа
    try:
        for num in spis_num:
            num = int(num)
    
    
    except ValueError:
        print('False')


    # Если все числа целые
    else:
        spis_num = list(map(int, spis_num.split()))  
        
        #Создаем множестов для отслеживания встреченных чисел
        seen = set()
        res = []

        # Проверяем каждое число
        for num in spis_num:
            if  num  in seen:
                res.append('yes')
            else:
                res.append('no')
                seen.add(num)
        print(res)


string = input("Введите числа через пробел: ")
yes_or_no(string)