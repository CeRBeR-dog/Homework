"""
*
класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты(свойства):
    - value - текущее значение счетчика
    ...

Определить методы:
    - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
    - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
    - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
    - reset, сбрасывает значение счетчика на стартовое    
    - метод __iter__
    - метод __next__
    
    ** - stat, возвращает среднее количество изменений счетчика в секунду

"""


import time

class Counter:
    value: str = 0

    def __init__(self, value=0):
        if not isinstance(value, int):
            raise ValueError("Значение счетчика должно быть целым числом")

        self.__start_value = value
        self.__value = value
        self.__changes = 0
        self.__start_time = time.time()

    @property
    def value(self):
        return self.__value
    
    def increase(self, num=1):
        if not isinstance(num, int):
            raise ValueError("Увеличением должно быть целым числом")
        
        self.__value += num
        self.__changes += 1

    def decrease(self, num=1):
        if not isinstance(num, int):
            raise ValueError("Уменьшение должно быть целым числом")
        
    def reset(self):
        self.__value = self.__start_value
        self.__changes = 0
        self.__start_time = time.time()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.increase()
        return self.value
    
    def __str__(self):
        return f"Counter(value={self.value})"
    





if __name__ == "__main__":
    
    print("=== Создание счетчика ===")
    c1 = Counter()          # по умолчанию 0
    c2 = Counter(10)        # с произвольным значением

    print(c1.value)  # 0
    print(c2.value)  # 10

    print("\n=== Увеличение ===")
    c1.increase()
    print(c1.value)  # 1

    c2.increase(5)
    print(c2.value)  # 15

    print("\n=== Уменьшение ===")
    c1.decrease()
    print(c1.value)  # 0

    c2.decrease(3)
    print(c2.value)  # 12

    print("\n=== Сброс ===")
    c1.reset()
    print(c1.value)  # 0

    c2.reset()
    print(c2.value)  # 10

    print("\n=== Проверка итератора ===")
    c3 = Counter(5)
    it = iter(c3)
    print(next(it))  # 6
    print(next(it))  # 7
    print(next(it))  # 8

    print("\n=== Проверка типа ошибок ===")
    try:
        c1.increase("abc")
    except ValueError as e:
        print("Ошибка increase:", e)

    try:
        c1.decrease(3.5)
    except ValueError as e:
        print("Ошибка decrease:", e)

    try:
        c_invalid = Counter("abc")
    except ValueError as e:
        print("Ошибка init:", e)

   