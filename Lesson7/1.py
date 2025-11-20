"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.

"""
fraz_1 = "Ведите оценку ученику: "
fraz_2 = "Это не оценка"
ev = int(input(fraz_1))
step = None
count = 1

while step != 0:
    # Проверка типа
    try:
        step = int(input(fraz_1))
        if 0 <= step <= 10:
            ev = ev + step
            count += 1
        else:
            print(fraz_2)
   # Если вели строку
    except ValueError:
        print (fraz_2)


print ("Средний балл:", round(ev/count, 2))