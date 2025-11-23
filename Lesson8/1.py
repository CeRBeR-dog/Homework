"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""

def short_sfp(sfp: str, rev: bool = False) -> str:
    sfp = sfp.split()

    surname, first_name, patronymic = sfp

    first_name = list(first_name)
    short_fr_name = first_name[0] + "."    

    patronymic = list(patronymic)
    short_pat = patronymic[0] + "."

    if rev:
        print(short_fr_name + short_pat, surname)
        
    else:
        print(surname, short_fr_name + short_pat)

fio = input("Ведите ФИО: ")

short_sfp(fio)
