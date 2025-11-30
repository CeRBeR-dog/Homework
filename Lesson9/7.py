"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""

from pprint import pprint
from string import ascii_letters, digits

#Создали кортедж валидных символов
valid_char = set(ascii_letters + digits + "_")


def valid_log(login):

    for i in login:
        if i not in valid_char:
            return False

    return True

users = [
    {"name":"Витя", "login":"Vity 1990", "password":"QWE12"},
    {"name":"Вася", "login":"Vassya_1992", "password":"Vas_sya_92"},
    {"name":"Игорь", "login":"Игорь_98", "password":"Igor_98"},
    {"name":"Коля", "login":"Ni-kola", "password":"Nik91"},
]

bad_pas = list(filter(lambda users: len(users['password']) <= 5, users))

# Вывести полный словарь данных с неправильным паролем
#pprint(bad_pas)

# Сказать юзеру что у него некоректный пароль
for user in bad_pas:
    print(f"Уважаемы {user['name']}, ваш пароль меньше 5 символов.")


no_valid_log = list(filter(lambda users: not valid_log(users['login']), users))

# Вывести полный словарь данных с невалидным логином
#pprint(no_valid_log)

# Сказать юзеру что у него невалидный логи
for user in no_valid_log:
    print(f"Уважаемы {user['name']}, ваш логин {user['login']} не является корректным.")
