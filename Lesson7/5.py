'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''

sp = input("Ведите слова через пробел: ").split()

for idndex, iteam in enumerate(sp):
    ite = iteam
    ite = list(ite)
    let = ite[idndex]
    print(f"{idndex + 1} - {iteam} - {let}")