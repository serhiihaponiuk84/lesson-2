"""
Завдання 1:
Створіть клас "Місто". Необхідно зберігати в полях класу: назву міста, назву регіону, назву країни, кількість жителів
міста, поштовий індекс міста, телефонний код міста. Реалізуйте доступ до окремих полів (Інкапсуляція).
Завдання 2:
Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту, кількість жителів країни,
телефонний код країни, назву столиці, назву міст країни. Реалізуйте доступ до окремих полів (Інкапсуляція).
"""
class City:
    def __init__(self, name, region, population, postal_code, phone_code):
        self.__name = name
        self.__region = region
        self.__country = None
        self.__population = population
        self.__postal_code = postal_code
        self.__phone_code = phone_code

    @property
    def name(self):
        return self.__name

    @property
    def region(self):
        return self.__region

    def add_country(self, country):
        self.__country = country

    @property
    def population(self):
        return self.__population

    @property
    def postal_code(self):
        return self.__postal_code

    @property
    def phone_code(self):
        return self.__phone_code

    def __str__(self):
        return f"Місто: {self.__name}, Регіон: {self.__region}, Країна: {self.__country.name}, " \
               f"Населення: {self.__population}, Поштовий індекс: {self.__postal_code}, " \
               f"Телефонний код: {self.__phone_code}"


class Country:
    __cities = []
    def __init__(self, name, continent, population, phone_code):
        self.__name = name
        self.__continent = continent
        self.__population = population
        self.__phone_code = phone_code
        self.__capital = None

    @property
    def name(self):
        return self.__name

    @property
    def continent(self):
        return self.__continent

    @property
    def population(self):
        return self.__population

    @property
    def phone_code(self):
        return self.__phone_code

    def add_capital(self, capital):
        self.__capital = capital

    def add_city(self, city):
        self.__cities.append(city)

    def __str__(self):
        cities_names = ", ".join(city.name for city in self.__cities)
        return f"Країна: {self.__name}, Континент: {self.__continent}, Населення: {self.__population}, " \
               f"Телефонний код: {self.__phone_code}, Столиця: {self.__capital.name}, Міста: {cities_names}"


city_1 = City("Львів", "Львівська область", 721301, "79000", "+380 32")
city_2 = City("Київ", "Київська область", 2967360, "01001", "+380 44")
ukraine = Country("Україна", "Європа", 41600000, "+380")
city_1.add_country(ukraine)
city_2.add_country(ukraine)
ukraine.add_city(city_1)
ukraine.add_city(city_2)
ukraine.add_capital(city_2)

print(city_1)
print()
print(city_2)
print()
print(ukraine)
