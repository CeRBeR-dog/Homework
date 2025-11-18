'''
Запросить число от 1 до 12. 
Если ввели другое число сообщить об ошибке. 
Если ввели не число сообщить об ошибке. 
Когда введут допустимое число - вывести на экран соответствующее 
название месяца, пору года и сколько дней в данном месяце.

'''

# Данные наших месяцев по порядку в году 
year = {
    1:{'mounth':'Juanuary', 'time_of_year':'Winter', 'days':"31"},
    2:{'mounth':'Febrary', 'time_of_year':'Winter', 'days':"28(9)"},
    3:{'mounth':'March', 'time_of_year':'Spring', 'days':"31"},
    4:{'mounth':'April', 'time_of_year':'Spring', 'days':"30"},
    5:{'mounth':'May', 'time_of_year':'Spring', 'days':"31"},
    6:{'mounth':'June', 'time_of_year':'Summer', 'days':"30"},
    7:{'mounth':'Jule', 'time_of_year':'Summer', 'days':"31"},
    8:{'mounth':'August', 'time_of_year':'Summer', 'days':"31"},
    9:{'mounth':'September', 'time_of_year':'Autumn', 'days':"30"},
    10:{'mounth':'October', 'time_of_year':'Autumn', 'days':"31"},
    11:{'mounth':'November', 'time_of_year':'Autumn', 'days':"30"},
    12:{'mounth':'December', 'time_of_year':'Winter', 'days':"31"}
}

num = input("Введите номер месяца: ")

# Пытаемся перевести строку в число
try:
    num = int(num)

# Если строку нельзя перевести - говорим об этом
except ValueError:
    print('Это строка')

# Если строка перевелась - продолжаем дальше
else:
    pod_num = 1 <= num <= 12
    
    # Выводим месяц и все его данные 
    if pod_num:
        if num == 1: 
            print(year[num])
        elif num == 2:
            print(year[num])
        elif num == 3:
            print(year[num])
        elif num == 4:
            print(year[num])
        elif num == 5:
            print(year[num])
        elif num == 6:
            print(year[num])
        elif num == 7:
            print(year[num])
        elif num == 8:
            print(year[num])
        elif num == 9:
            print(year[num])
        elif num == 10:
            print(year[num])
        elif num == 11:
            print(year[num])
        elif num == 12:
            print(year[num])
   
    # Гоморим, что даное число нам не подходит 
    else:
        print ('Неподходящее число')
