# 1
# абстрактні методи

# from abc import ABC, abstractmethod
#
#
# абстрактний клас - містить у собі абстрактні методи, тобто методи без реалізації помічені
# декоратором @abstractmethod з модуля abc, а також методи з реалізацією (звичайні методи)
# Оскільки абстрактний клас містить у собі абстрактні методи -
# всі дочірні класи мають надати реалізації цих методів,
# так само не можна створити екземпляр класу, у якого є хоча б один абстрактний метод

# інтерфейс - це клас, у якого тільки абстрактні методи,
# такий клас необхідний якщо вам потрібно створити якийсь контракт, зобов'язання надати реалізацію цих методів для
# інших класів спадкоємців
# class Polygon(ABC):
#     @abstractmethod  # цей метод без реалізації і всі дочірні класи повинні надати реалізацію цього методу
#     def noofsides(self):
#         pass
#
#     def show_info(self):
#         print("I am from polygon")
#
#
# class Triangle(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 3 sides")
#
#
# class Pentagon(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 5 sides")
#
#
# class Hexagon(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 6 sides")
#
#
# class Quadrilateral(Polygon):
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 4 sides")


# TypeError: Can't instantiate abstract class Polygon with abstract method noofsides
# test = Polygon()
# test.noofsides()

# Driver code
# R = Triangle()
# R.noofsides()
#
# K = Quadrilateral()
# K.noofsides()
#
# R = Pentagon()
# R.noofsides()
#
# K = Hexagon()
# K.noofsides()
# K.show_info()

# 2
# Поліморфізм функцій
# print(len("Програміст"))
# print(len(["Яблоко", "Банан", "Груша"]))
# print(len({"Имя": "Максим", "Address": "Киев"}))
#
# #Поліморфізм класів
# class Cat:
#     def __init__(self, klichka, vozrast):
#         self.klichka = klichka
#         self.vozrast = vozrast
#
#     def status(self):
#         print(f"Я кішка. Мене звуть {self.klichka}. Мій вік {self.vozrast} років")
#
#     def say(self):
#         print("Мяу")
#
#
# class Dog:
#     def __init__(self, klichka, vozrast):
#         self.klichka = klichka
#         self.vozrast = vozrast
#
#     def status(self):
#         print(f"Я пес. Мене звуть {self.klichka}. Мій вік {self.vozrast} років")
#
#     def say(self):
#         print("Гав")
#
#     def hello(self):
#         print(f"Hello {self.klichka}")
#
#
# class PetDog(Dog):
#     def __init__(self, klichka, vozrast, owner):
#         super().__init__(klichka, vozrast)
#         self.owner = owner
#
#     # перевизначення методу
#     def hello(self):
#         super().hello()
#         print(f"Owner: {self.owner}")
#
#
# test = PetDog("test", 1, "Vasya")
# test.hello()
#
# cat_obj = Cat("Муська", 10)
# dog_obj = Dog("Барон", 12)
#
# for pet in (cat_obj, dog_obj):
#     pet.say()
#     pet.status()
#     pet.say()


# # Поліморфізм та успадкування
# from math import pi
# from abc import ABC, abstractmethod
#
#
# # інтерфейс
# class BaseShape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Shape(BaseShape):
#     def __init__(self, name):
#         self.name = name
#
#     # def area(self):
#     #     pass
#
#     def info(self):
#         return "Я двухмерная форма."
#
#     # строковое представление объекта
#     def __str__(self):
#         return "строковое представление объекта Shape"
#
#
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Квадрат")
#         self.length = length
#
#     def area(self):
#         return self.length ** 2
#
#     def info(self):
#         return "Квадраты имеют каждый угол равный 90 градусам."
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Круг")
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
#
# class AreaCalculator:
#     def __init__(self, geom_object):
#         self.geom_object = geom_object
#
#     def get_area(self):
#         print(self.geom_object.area())
#
#
# # my_shape = Shape("my_shape")
# # print(my_shape)
# #
# kvadrat = Square(8)
# krug = Circle(14)
# # print(kvadrat)
# # print(kvadrat.info())
# # print(krug.info())
# # print(kvadrat.area())
#
# areaCalculator = AreaCalculator(kvadrat)
# areaCalculator.get_area()
# areaCalculator = AreaCalculator(krug)
# areaCalculator.get_area()
# print(Square.mro())
# print(AreaCalculator.mro())
