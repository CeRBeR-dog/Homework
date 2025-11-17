"""
2. Создать структуру данных сотрудников фирмы с 
    тремя сотрудниками. каждый сотрудник должен иметь:
        ФИО, 
        должность, 
        год рождения, 
        список навыков, 
        список детей с их именем и годом рождения. 
    
    Запросить ФИО сотрудника и вывести по нему информацию.
    
    ** задать вопрос о желании добавить сотрудника,
        если ответ да - добавить сотрудника через несколько input
        (после добавления сотрудника вывести всю структуру консоль)

"""

users = {
     "Vasya":{"name":"Vasya", "post":"developer",  "year_b":1983, "skill":"hard skills",
       "children":{"name_1":"Vitya","year_b_1":2003, "name_2":"Masha","year_b_2":2005}},    
     "Vanya":{"name":"Vanya", "post":"developer",  "year_b":1995, "skill":"soft skills",
      "children":{"name_1":"Varya","year_b_1":2019, "name_2":"Masha","year_b_2":2022}},
     "Roma":{"name":"Roma", "post":"tester",  "year_b":1997, "skill":"soft skills",
      "children":{"name_1":"Vanya","year_b_1":2020, "name_2":"Masha","year_b_2":2024},},    
     
}

nam = input("Введите имя сотрудника: ")
print(users[nam])

