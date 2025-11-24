'''

Написать функцию, которая возвращает любое число в виде денежной величины 
с разделителями групп разрядов в качестве пробела и валютой в конце. 
Денежная величина всегда должна содержать количество копеек в виде дух 
знаков после точки, даже если исходное число целое. 
*Нельзя использовать форматную строку.
Например: 1234567 -> "1 234 567.00 руб."

с помощью try перехватить возможные ошибки.
'''


def money (num: float) -> str:

    try:
       num = float(num)
    
    except ValueError:
        print("Не число")
    
    # Приводим к целому числу
    full_num = int(round(abs(num)*100))
    
    # Определяем знак
    minus = "-" if num < 0 else ""

    # Отделение рублей и копеек
    rub = full_num // 100
    kop = full_num % 100

    # Раззделение рублей
    rub_st = str(rub)
    rub_parts = []
    i = len(rub_st)
    while i > 0:
        start = max(0 , i - 3)
        rub_parts.append(rub_st[start:i])
        i -= 3
    rub_st_new = " ".join(reversed(rub_parts))

    # Копейки 
    kop = round(kop)
    kop_st = str(kop)

    print (minus + rub_st_new + "." + kop_st + " руб.")




num = input("Введите число: ")

money(num)