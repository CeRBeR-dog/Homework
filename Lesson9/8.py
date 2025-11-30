'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''

a = 5
b = 23


some_list = ["hello", 12 > 4, 1345, a > b, "python", 0, "!!!",
              20<2, 45, 10 == 10, "hehe"]


str_list = list(filter(lambda i: isinstance(i, str), some_list))

print(str_list)

bool_list = list(filter(lambda i: isinstance(i, bool), some_list))

print(bool_list)