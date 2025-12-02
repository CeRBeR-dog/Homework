"""
Написать функцию hello, которая принимает 2 аргумента name и surname и
выводит принтом "Привет, {name} {surname}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
Выполняеся функция <имя> с аргусентами <аргументы> 
После выполнения функции напечатать строку "<имя функции> - завершена"
"""


def log_decorator (func):
    
    def wrapper(*args):
        print(f"Выполняеся функция {func.__name__} с аргусентами {args} ")
        result = func(*args)
        print(f"{func.__name__} - завершена")
        return result
    return wrapper

if __name__ == "__main__":

    @log_decorator
    def hello(name, surname):
        print(f"Привет, {name} {surname}")
    

    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")

    hello(name, surname)

