'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''

def rect(a1: int, a2: int, squar: bool = False) -> int:
    try:
        a1 = int(a1)
        a2 = int(a2)

    except ValueError:
        print('Не подходит')

    else:
        if squar:
            print("Площадь", a1*a2)
        
        else:
            print("Периметр", 2*(a1 + a2))

st1 = input("введите первую сторону: ")
st2 = input("введите вторую сторону: ")

rect(st1, st2, squar=True)