'''
запросить у пользователя логин пароль и возраст
вывести доступ разрешен:
    логин:admin   пароль:123456    возраст: любой    
    логин:vasya   пароль: vas123   возраст: менее 60
    логин:guest   пароль: любой    возраст:более 18
    
в остальных случаях - "доступ запрещен".

'''

log = input("Введите логин: ")
pas = input("Введите пароль: ")
age = int(input("Введите возраст: "))

#Фразы для вывода
fr = "Доступ разреше"
fr_el = "Доступ запрещён"

#admin
log_a = log == 'admin'
pas_a = pas == '123456'

#vasya
log_v = log =='vasya'
pas_v = pas == 'vas123'
age_v = age < 60

#guest
log_g = log =='guest'
age_g = age > 18

if log_a and pas_a:
    print(fr)
elif log_v and pas_v and age_v:
    print(fr)
elif log_g and age_g:
    print(fr)
else:
    print(fr_el)