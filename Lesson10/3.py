"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""
def check_brackets (new_line: str) -> bool:

    new_line = list(new_line)
   
    #Быстрая проверка на скобки
    count_open = new_line.count("(")
    count_close = new_line.count(")")

    if count_open != count_close:
        return ("False")
    
    # Проверка на порядок
    balance = 0
    for ch in new_line:
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1
            if balance < 0:
                return ("False")

    
    return("True")

if __name__ == '__main__':
    
   new_line = input("Введите строку со скобками: ")

   print(check_brackets(new_line))

