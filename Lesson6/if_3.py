'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''
#Фразы для вывода
fraz = "Введите число: "
fraz_max = "Наибольшее число -"

fr = int(input(fraz))
sc = int(input(fraz))
th = int(input(fraz))

#Блок определения наибольшего числа
max_fr = fr >= sc and fr >= th
max_sc = sc >= fr and sc >= th
max_th = th >= fr and th >= sc

#Вывод на экран наибольшего числа
if max_fr:
    print(fraz_max, fr)
elif max_sc:
    print(fraz_max, sc)
elif max_th:
    print(fraz_max, th)



