"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Декущего ля года
  издания дополнительно проверить на валидность (> 0, <= тгода).

Аксессоры реализоваться через property.
"""

from datetime import datetime



class BookCard:
    __author: str = "author"
    __title: str ="title"
    __year: int = 0
  
    def __init__(self, author, title, year):
        
        self.author = author
        self.title = title
        self.year = year
    
    def __str__(self):
        return f"{self.title} - {self.author}, {self.year}"


    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self,value):
        if not isinstance(value, str):
            raise ValueError("Автор не типа string")
        self.__author = value
        

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self,value):
        if not isinstance(value, str):
            raise ValueError("Название книги не типа string")
        self.__title = value
        
    
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self,value):
        if not isinstance(value, int):
            raise ValueError("Год издания книги не типа integer")
        if not (0 < value <= datetime.now().year):
            raise ValueError("Год издания книги указан не верно")
        self.__year = value
        
    #Сравнение    
    def __eq__(self, other):
        if not isinstance(other, BookCard):
            return NotImplemented
        return self.year == other.year
    
    def __ne__(self, other):
        if not isinstance(other, BookCard):
            return NotImplemented
        return self.year != other.year
    
    def __lt__(self, other):
        if not isinstance(other, BookCard):
            return NotImplemented
        return self.year < other.year
    
    def __le__(self, other):
        if not isinstance(other, BookCard):
            return NotImplemented
        return self.year <= other.year
    
    def __gt__(self, other):
        if not isinstance(other, BookCard):
            return NotImplemented
        return self.year > other.year
    
    def __ge__(self, other):
        if not isinstance(other, BookCard):
            return NotImplemented
        return self.year >= other.year
    


if __name__ == "__main__":

  books = [
    BookCard("Толстой", "Муму", 1854),
    BookCard("Bradbury", "Fahrenheit 451", 1953),
   #BookCard("Глуховский","Метро2033",2033),
    BookCard("Глуховский","Метро2033",2005)
  ]

  increase = sorted(books)
  print("По возрастанию: ")
  for b in increase:
    print(b)
