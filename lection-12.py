import json

# # json string data
# employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'
#
# # check data type with type() method
# print(type(employee_string))
#
# # convert string to  object
# json_object = json.loads(employee_string)
#
# # check new data type
# print(type(json_object))
#
# # output
# # <class 'dict'>
#
# # access first_name in dictionary
# print(json_object["first_name"])
#
# ####################
# employees_string = '''
# {
#     "employees" : [
#        {
#            "first_name": "Michael",
#            "last_name": "Rodgers",
#            "department": "Marketing"
#
#         },
#        {
#            "first_name": "Michelle",
#            "last_name": "Williams",
#            "department": "Engineering"
#         }
#     ]
# }
# '''
#
# data = json.loads(employees_string)
#
# print(type(data))
# # output
# # <class 'dict'>
#
# # access first_name
# for employee in data["employees"]:
#     print(employee["first_name"])
#
# json_str = json.dumps(data)
# print(json_str)
# print(type(json_str))

###############
# import json
# import os
#
# PATH_TO_TODO_LIST = "myTodoList.json"
#
#
# def create_todo_list_json_file(path_to_storage: str) -> None:
#     if not os.path.exists(path_to_storage):
#         with open(path_to_storage, "w", encoding="utf-8") as file:
#             todos_dict: dict = {"todos": []}
#             file.write(json.dumps(todos_dict))
#     else:
#         raise FileExistsError("File already exists!")
#
#
# def get_todo_items(path_to_storage: str) -> dict:
#     with open(path_to_storage, 'r', encoding="utf-8") as file:
#         return json.load(file)
#
#
# def add_todo_item(path_to_storage: str, todo_item: str) -> str:
#     current_todos = get_todo_items(path_to_storage)
#     current_todos["todos"].append(todo_item)
#     with open(path_to_storage, 'w', encoding="utf-8") as file:
#         json.dump(current_todos, file, indent=4)
#         return todo_item
#
#
# def remove_todo_item(path_to_storage: str, todo_item: str) -> str:
#     current_todos = get_todo_items(path_to_storage)
#     current_todos["todos"].remove(todo_item)
#     with open(path_to_storage, 'w', encoding="utf-8") as file:
#         json.dump(current_todos, file, indent=4)
#         return todo_item
#
#
# if __name__ == "__main__":
#     if not os.path.exists(PATH_TO_TODO_LIST):
#         create_todo_list_json_file(PATH_TO_TODO_LIST)
#
#     print(get_todo_items(PATH_TO_TODO_LIST))
#     # add_todo_item(PATH_TO_TODO_LIST, "first item")
#     # remove_todo_item(PATH_TO_TODO_LIST, "first item")
#     # print(get_todo_items(PATH_TO_TODO_LIST))
#
# # дописать меню
# # добавить функцию изменения по порядковому номеру (от 1 до ...)
# # протестировать все функции

#####
# ООП - об'єктно орієнтоване програмування
# Клас - кастомний тип даних, який описує деякий об'єкт.
# Клас - креслення майбутнього екземпляра об'єкта.

# Інкапсуляція - приховування внутрішньої реалізації та надання санкціонованого доступу
# до інтерфейсу класу. Як чорна скринька.
# Абстрагуємося від внутрішньої реалізації.

# Спадкування - створення нового класу на основі вже існуючого.
# Розширення базового класу – дочірніми/дочірніми класами.
# Абстрагуємось від базового класу/класів, використовуючи дочірній клас.

# Поліморфізм - один інтерфейс та багато реалізацій.
# Абстрагуємося від конкретної реалізації
####
# class Test:
#     конструктор без параметрів (не за замовчуванням)
#     def __init__(self):
#         self.text = "some text"
#
#     конструктор класу - створює екземпляр об'єкту
#     def __new__(cls):
#         pass
#
#     для ініціалізації об'єкту
#     якщо явно не визначити конструктор __new__ -> то __init__ він створиться автоматично
#     def __init__(self):
#         pass
# __init__ Конструктор класу – дозволяє створити екземпляр класу. Можливо з параметрами та без параметрів.
# # self - посилання на контекст класу, екземпляр класу
###
# статичний метод (функція), поле (змінна) відносяться до класу, і до екземпляра
# статичний ел-т можна використовувати не створюючи екземпляр класу
# Найчастіше статичні класи використовують для опису конфігів та інших службових об'єктів, там де немає сенсу
# створювати екземпляри


# class Car:
#     company = "Toyota"  # static field
#
#     def __init__(self, color, year):
#         self.year = year
#         self.color = color
#
#     def show_info(self):
#         print("I am a Car")
#         print(f"Year: {self.year} Color: {self.color}")
#
#     @staticmethod
#     def show_company_name():  # static method
#         print(f"Company Name: {Car.company}")
#
#
# car1: Car = Car("green", 2024)
# # Car.show_info()
# # print(Car.year)
# print(Car.company)
# Car.show_company_name()
# car1.show_company_name()

# car1: Car = Car("green", 2024)
# car1.show_info()
# print(type(car1))
#
# car_info = {
#     "year": 2023,
#     "color": "red"
# }
# car2: Car = Car(car_info.get("color"), car_info.get("year"))
# car2.show_info()
# print(type(car2))

###
# class InvoiceTypes:
#     SimpleInvoice = "simple"
#     UrgentInvoice = "urgent"
#     CashInvoice = "cash"
#
#     @staticmethod
#     def show_all_types():
#         print(InvoiceTypes.SimpleInvoice)
#         print(InvoiceTypes.UrgentInvoice)
#         print(InvoiceTypes.CashInvoice)
#
#
# InvoiceTypes.show_all_types()

##########
# інкапсуляція
# v1
# class User:
#     __name: str = "no name"  # private поле, доступне тільки всередині цього класу
#     __age: int = 0
#     __secret: int = 12345
#
#     def __init__(self, name=None, age=None):
#         # self.__name = name
#         # self.__age = age
#         # застосуємо інкапсуляцію
#         self.set_age(age)
#         self.set_name(name)
#
#     def set_name(self, name):
#         if 2 < len(name) < 50:
#             self.__name = name
#         else:
#             print("Incorrect name length!")
#
#     def get_name(self):
#         return self.__name
#
#     def set_age(self, age):
#         if 18 < age < 150:
#             self.__age = age
#         else:
#             print("Incorrect age!")
#
#     def get_age(self):
#         return self.__age
#
#     def show_info(self):
#         print(f"Name: {self.__name} age: {self.__age}")
#         # self.__secret_info()
#
#     def __secret_info(self):
#         print(f"Secret code: {self.__secret}")
#
#
# vasya = User("Vasya", -44)
# vasya.show_info()
# vasya.set_age(100)
# vasya.show_info()
# vasya.set_age(-100)
# vasya.show_info()
# vasya.__secret_info()
# vasya._User__secret_info()  # так робити не треба так як це ламає інкапсуляцію

####
# print(vasya.__name)
# подводный камень ниже!
# vasya.__name = "qqqq"
# print(vasya.__name)  # динамічно створилося нове поле в цьому примірнику, але це поле не має жодного відношення до
# # приватному полю __name яке ми створили у класі
# vasya.hobby = "wwww"
# print(vasya.hobby)
# vasya.show_info()
#
# petya = User("Petya", 55)
# petya.show_info()

###
# v2 реалізація інкапсуляції використовуючи анотації властивостей
# class User:
#     __name: str = "no name"  # private поле, доступне тільки всередині цього класу
#     __age: int = 0
#     __secret: int = 12345
#
#     def __init__(self, name=None, age=None):
#         # self.__name = name
#         # self.__age = age
#         # застосуємо інкапсуляцію
#         self.name = name
#         self.age = age
#
#     # getter - для отримання значення приватного поля
#     @property
#     def name(self):
#         return self.__name
#
#     # setter - для санкціонованого доступу до приватної змінної (поля)
#     @name.setter
#     def name(self, name):
#         if 2 < len(name) < 50:
#             self.__name = name
#         else:
#             print("Incorrect name length!")
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 18 < age < 150:
#             self.__age = age
#         else:
#             print("Incorrect age!")
#
#     # public method - публічна (доступна зовні) функція
#     def show_info(self):
#         print(f"Name: {self.__name} age: {self.__age}")
#         # self.__secret_info()
#
#     # private method - приватна (недоступна зовні) функція
#     def __secret_info(self):
#         print(f"Secret code: {self.__secret}")
#
#
# anton = User("Anton", -34)
# anton.show_info()
# anton.age = 40  # setter
# print(anton.age)  # getter
# anton.show_info()
# anton.age = 400  # setter
# anton.show_info()
# print(anton.name)  # getter

##
# class MyConverter:
#     __money_sum = 0
#     __uah_rate = 37.4
#     __converter_direction = 1
#
#     def __init__(self, input_money, convert_dir):
#         self.money_sum = input_money
#         self.converter_direction = convert_dir
#
#     @property
#     def converter_direction(self):
#         return self.__converter_direction
#
#     @converter_direction.setter
#     def converter_direction(self, convert_dir):
#         if convert_dir == 1 or convert_dir == 2:
#             self.__converter_direction = convert_dir
#         else:
#             raise Exception("Provide correct converter direction!")
#
#     @property
#     def money_sum(self):
#         return self.__money_sum
#
#     @money_sum.setter
#     def money_sum(self, input_sum):
#         if 0 < input_sum < 1000000000:
#             self.__money_sum = input_sum
#         else:
#             raise Exception("Provide valid money sum!")
#
#     # readonly property
#     @property
#     def uah_rate(self):
#         return self.__uah_rate
#
#     def show_uah_rate(self):
#         print(f"Current UAH rate: {self.__uah_rate}")
#
#     def show_result(self):
#         print(self.__getMoneyResult())
#
#     def __getMoneyResult(self):
#         match self.__converter_direction:
#             case 1:
#                 return f"{self.__money_sum} UAH = {self.__get_usd_sum()} USD"
#             case 2:
#                 return f"{self.__money_sum} USD = {self.__get_uah_sum()} UAH"
#             case _:
#                 raise Exception("Incorrect converter direction!")
#
#     def __get_usd_sum(self):
#         return self.__money_sum / self.__uah_rate
#
#     def __get_uah_sum(self):
#         return self.__money_sum * self.__uah_rate
#
#
# try:
#     converter = MyConverter(5000, convert_dir=2)
#     converter.show_result()
# except Exception as error:
#     print(error)
