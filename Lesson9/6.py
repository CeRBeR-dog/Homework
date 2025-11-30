"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""


dict_temp = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

increase_temp = dict(sorted(dict_temp.items(), key = lambda iteam: iteam[1]))
print(increase_temp)

decrease_temp = dict(sorted(dict_temp.items(), key = lambda iteam: iteam[-1], reverse=True))
print(decrease_temp)