"""
Описать абстрактный класс Animal у которого:

- атрибут name - кличка (тип str)
- магический метод __init__, который принимает аргумент name
- абстрактный метод says, который не принимает аргументов

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
says таким образом, чтобы он возвращал строку вида:

- "{кличка} - кошка. Говорит МЯУ!" для класса Cat
- "{кличка} - собака. Говорит ГАВ!" для класса Dog
- "{кличка} - корова. Говорит МУ!" для класса Cow
"""

class Animal:
    name: str = "Кличка"

    def __init__(self, name):
        self.name = name

    def says(self):
        """
        Должен будет преропредлён в потомках
        """
        pass


class Cat(Animal):
    def says(self):
        return f"{self.name} - кот. Говорит МЯУ!"
    
class Dog(Animal):
    def says(self):
        return f"{self.name} - собака. Говорит ГАВ!"
    
class Cow(Animal):
    def says(self):
        return f"{self.name} - корова. Говорит МУ!"


pets = [
    Cat("Мурзик"),
    Dog("Тузик"),
    Cow("Мурка")
]

print("Как говорят животные: ")
for a in pets:
    print(a.says())