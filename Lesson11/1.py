"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: 
        <Бренд-Модель> - Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""



class Phone:
    
        brand = "Motorola"
        model = "DynaTAC8000X"
        issue_year = "1983"

        #Иницилизируем 
        def __init__(self, brand, model, issue_year):
        
                self.brand = brand
                self.model = model
                self.issue_year = issue_year

        
        #Функция которая принимает имя звонящего и выводит на экран
        def receive_call(self, name,):

                print(f"'{self.brand}'-'{self.model}' - Звонит {name}")

        
        #Dозвращаtn кортеж (brand, model, issue_year)
        def get_info(self):

                return ( self.brand, self.model, self.issue_year)
        

        #Выводит на экран информацию об устройстве
        def __str__(self):

                return f"Бренд: {self.brand} \nМодель: {self.model} \nГод выпуска: {self.issue_year}"




phone_1 = Phone('Samsung', 'Galaxy S24', '2024')
phone_2 = Phone('Apple', 'iPhone 17', '2025')
phone_3 = Phone('Xiaomi', '17 Pro Max', '2025')



print(phone_1.get_info())
print(phone_2.get_info())
print(phone_3.get_info())



print(phone_1)
print(phone_2)
print(phone_3)



#phrase = 'Введите имя: '
#name1 = input(phrase)
#name2 = input(phrase)
#name3 = input(phrase)

name1, name2, name3 = ['Vasya', 'Sergey', 'Igory']

phone_1.receive_call(name1)
phone_2.receive_call(name2)
phone_3.receive_call(name3)