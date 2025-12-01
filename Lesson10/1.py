'''
Добавить несколько черепах 
    - или сразу 
    * или в течении игры по одной через определенное количество кликов
    - на каждой забиндить клик через одну и туже функцию cath

'''



from turtle import *
from random import randint


def on_click(x, y):
    global clicks
    clicks += 1

def catch1(x,y):
    ts[0].goto(0, 0)
    ts[0].left(randint(0, 360))
    
    
def catch2(x,y):
    ts[1].goto(0,0)
    ts[1].left(randint(0, 360))
    
def catch3(x,y):
    ts[2].goto(0,0)
    ts[2].left(randint(0, 360))

def catch4(x,y):
    ts[3].goto(0,0)
    ts[3].left(randint(0, 360))

def catch5(x,y):
    ts[4].goto(0,0)
    ts[4].left(randint(0, 360))



t1 = Turtle('turtle') # создаем черепаху
t2 = Turtle('turtle')
t3 = Turtle('turtle')
t4 = Turtle('turtle')
t5 = Turtle('turtle')

t1.speed(0) # 0 самая быстрая, 1 - самая медленная, чем выше скорость тем быстрее
t2.speed(0)
t3.speed(0)
t4.speed(0)
t5.speed(0)

t1.color('red')
t2.color('blue')
t3.color('green')
t4.color('orange')
t5.color('pink')

t2.left(72) # повернуть в градусах
t3.left(144) #
t4.left(216)
t5.left(288)

t1.onclick(catch1)
t2.onclick(catch2)
t3.onclick(catch3)
t4.onclick(catch4)
t5.onclick(catch5)


# добавляем всех в один список
ts = []
ts.append(t1)
ts.append(t2)
ts.append(t3)
ts.append(t4)
ts.append(t5)

while 1:
    for t in ts: # берем каждую черепаху из списка
        # t.fd(2) # вперед на 2 пикселя
        t.forward(3) # вперед на 3 пикселя

mainloop()
