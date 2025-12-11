"""
Создать класс Student.


Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""

from faker import Faker



class Student:

    surname = "Ivanov"
    name = "Ivan"
    group = "0a"
    
    def __init__(self, surname, name, group):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = []

    def __str__(self):
        return f"{self.surname}, {self.name}, {self.group}"

    
    def add_grade (self, *grades):
        if len(grades) == 1 and isinstance(grades[0], (list, tuple)):
            grades = tuple(grades[0])
        
        for grade in grades:
            try: 
                grade = int(grade)
            
            except:
                raise ValueError("Оценка ддолжна быть целым числом")
            
            if not (1 <= grade <= 10):
                raise ValueError("Оценка должна быть в диапозоне от 1 до 10")
            
            self.grads.append(grade)


    def average_grade(self):
        if not self.grads:
            #Не правильно
            #return ("Нету оценок для расчёта среднего балла")
           
            return 0
        
        return sum(self.grads)/len(self.grads)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()
    
    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() != other.average_grade()
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()
    
    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()
    
    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() >= other.average_grade()



students = [ 
    Student("Ivanov", "Andrey", "a12"),
    Student("Andreev", "Ivan", "b31"),
    Student("Gregorev", "Gregore", "a12"),
    Student("Bruev", "Anton", "b31"),
    Student("Mischenko", "Ivan", "a12")
]

students[0].add_grade(9,5,10,8,9)
students[1].add_grade(4,7,6,8)
students[2].add_grade(9,10,8,9,9)
students[3].add_grade(9,8,9)
students[4].add_grade(9,5,10,9)

increase = sorted(students)
decrease = sorted(students, reverse = True)

print("По возрастанию: ")
for s in increase:
    print(s)

print("\nПо убыванию: ")
for s in decrease:
    print(s)

print("\nС средним балом больше 8: ")
for s in students:
    if s.average_grade() > 8:
        print(s)




#print(f'По возрастанию: {[s for s in increase]}')
#print(f'По возрастанию: {[s for s in increase]}')
 

#Student(Faker.sur_name(), Faker.name_male(), Faker.bothify(text = f'{Faker.random_digit(3)}-???-##', letters='ABCDEF'))