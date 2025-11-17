'''
Буква "a" стоит 10 очков, "b" - 20, "c" - 30, "d" - 40
Запросить кодовою фразу из пяти символов используя только a, b, c, d.
Вывести на экран общее количество очков введенной фразы.

'''
points = {"a":10, "b":20, "c":30, "d":40}

kod = input('Кодовою фраза из пяти символов используя только a, b, c, d: ')

kod = list(map(str, kod))
zn_1, zn_2, zn_3, zn_4, zn_5 = kod


zn_kod = points[zn_1], points[zn_2], points[zn_3], points[zn_4], points[zn_5]
sum_kod = sum(zn_kod)

print(sum_kod)