"""
Завдання 1
Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат
повертається із функції.
Завдання 2
Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат
повертається із функції.
Завдання 3
Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий
результат повертається із функції.
Завдання 4
Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість видаленних елементів.
Завдання 5
Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
Завдання 6
Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр,
список також передається як параметр. Функція повертає новий список, який містить отримані результати.
"""

# 1.
import random
def product_of_list_elements(input_list:list) -> int:
    """
    Функція для обчислення добутку елементів списку цілих чисел.
    Параметри:
    input_list (list): Список цілих чисел.
    Повертає:
    int: Добуток усіх елементів списку.
    """
    if not input_list:      # Перевірка на пустий список
        return None         # Повертаємо None, якщо список пустий
    product = 1  # Початкове значення добутку
    for element in input_list:
        product *= element  # Множимо кожен елемент списку
    return product


print("Програма обчислює добуток елементів списку цілих чисел.")

COUNT_ARRAY_NUMBERS = 5    # кількість чисел у списку
MIN_ARRAY_NUMBER = 1       # значення мінімального числа у списку
MAX_ARRAY_NUMBER = 10      # значення максимального числа у списку

# Генерація списку випадкових чисел
test_list = [random.randint(MIN_ARRAY_NUMBER, MAX_ARRAY_NUMBER) for _ in range(COUNT_ARRAY_NUMBERS)]
print(f"Сгенеровано список із {COUNT_ARRAY_NUMBERS} випадкових чисел від {MIN_ARRAY_NUMBER} до {MAX_ARRAY_NUMBER}: {test_list}")
print(f"Добуток усіх елементів списку складає {product_of_list_elements(test_list)}.")
print()

# 2.
def find_minimum_in_list(input_list:list) -> int:
    """
    Функція для для знаходження мінімуму елементів списку цілих чисел.
    Параметри:
    input_list (list): Список цілих чисел.
    Повертає:
    int: Мінімум усіх елементів списку.
    """
    if not input_list:      # Перевірка на пустий список
        return None         # Повертаємо None, якщо список пустий
    minimum = input_list[0] # Припускаємо, що перший елемент мінімальний
    for element in input_list[1:]:  # Проходимо за списком, починаючи з другого елемента
        if element < minimum:
            minimum = element  # Знаходимо нове мінімальне значення
    return minimum


print("Програма знаходить мінімуму у списку цілих чисел.")

COUNT_ARRAY_NUMBERS = 10    # кількість чисел у списку
MIN_ARRAY_NUMBER = -100     # значення мінімального числа у списку
MAX_ARRAY_NUMBER = 100      # значення максимального числа у списку

# Генерація списку випадкових чисел
test_list = [random.randint(MIN_ARRAY_NUMBER, MAX_ARRAY_NUMBER) for _ in range(COUNT_ARRAY_NUMBERS)]
print(f"Сгенеровано список із {COUNT_ARRAY_NUMBERS} випадкових чисел від {MIN_ARRAY_NUMBER} до {MAX_ARRAY_NUMBER}: {test_list}")
print(f"Мінімум усіх елементів списку складає {find_minimum_in_list(test_list)}.")
print()

# 3.

def is_prime(n: int) -> bool:
    """Перевіряє, чи є число простим."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes_in_list(input_list:list) -> int:
    """
    Функція для визначення кількості простих чисел у списку цілих чисел.
    Параметри:
    input_list (list): Список цілих чисел.
    Повертає:
    int: Кількість простих чисел у списку.
    """
    if not input_list:      # Перевірка на пустий список
        return None         # Повертаємо None, якщо список пустий
    return sum(is_prime(element) for element in input_list)


print("Програма визначає кількість простих чисел у списку цілих чисел.")

COUNT_ARRAY_NUMBERS = 10    # кількість чисел у списку
MIN_ARRAY_NUMBER = -100     # значення мінімального числа у списку
MAX_ARRAY_NUMBER = 100      # значення максимального числа у списку

# Генерація списку випадкових чисел
test_list = [random.randint(MIN_ARRAY_NUMBER, MAX_ARRAY_NUMBER) for _ in range(COUNT_ARRAY_NUMBERS)]
print(f"Сгенеровано список із {COUNT_ARRAY_NUMBERS} випадкових чисел від {MIN_ARRAY_NUMBER} до {MAX_ARRAY_NUMBER}: {test_list}")
print(f"Кількість простих чисел у списку складає {count_primes_in_list(test_list)}.")
print()

# 4.
def remove_number_from_list(input_list: list, number_to_remove: int) -> int:
    """
    Функція видаляє всі входження заданого числа зі списку та повертає кількість видалених елементів.
    Параметри:
    input_list (list): Список цілих чисел, з якого потрібно видалити елементи.
    number_to_remove (int): Число, яке потрібно видалити зі списку.
    Повертає:
    int: Кількість видалених елементів.
    """
    if not input_list:      # Перевірка на пустий список
        return None         # Повертаємо None, якщо список пустий

    initial_length = len(input_list)  # Запам'ятовуємо початкову довжину списку
    input_list[:] = [item for item in input_list if item != number_to_remove]  # Видаляємо задане число
    final_length = len(input_list)  # Запам'ятовуємо кінцеву довжину списку
    return initial_length - final_length  # Повертаємо різницю між початковою та кінцевою довжиною списку


print("Програма видаляє зі списку ціле задане число.")

COUNT_ARRAY_NUMBERS = 20    # кількість чисел у списку
MIN_ARRAY_NUMBER = -10      # значення мінімального числа у списку
MAX_ARRAY_NUMBER = 10       # значення максимального числа у списку

# Генерація списку випадкових чисел
test_list = [random.randint(MIN_ARRAY_NUMBER, MAX_ARRAY_NUMBER) for _ in range(COUNT_ARRAY_NUMBERS)]
print(f"Сгенеровано список із {COUNT_ARRAY_NUMBERS} випадкових чисел від {MIN_ARRAY_NUMBER} до {MAX_ARRAY_NUMBER}:")
print(test_list)

while True:
    try:
        number_to_remove = int(input("Введіть ціле число для видалення:"))
        # if isinstance(number_to_remove, int):
        break

    except Exception:
        print("Помилка! Введіть ціле число для видалення зі списку.")

result = remove_number_from_list(test_list, number_to_remove)
print(f"Кількість видалених елементів зі значенням {number_to_remove} у списку складає {result}.") # Повертаємо кількість видалених елементів
print("Модифікований список:") # Повертаємо модифікований список
print(test_list)
print()

# 5.
def merge_lists(list_1:list, list_2:list) -> list:
    """
    Функція об'єднує два списки в один.
    Параметри:
    list1 (list): Перший список.
    list2 (list): Другий список.
    Повертає:
    list: Список, що містить елементи обох списків.
    """
    if not list_1 and not list_2i:      # Перевірка на пустий список
        return None                     # Повертаємо None, якщо список пустий
    return list_1 + list_2


print("Програма повертає список, що містить елементи обох двох отриманих списків.")

COUNT_ARRAY_NUMBERS = 5     # кількість чисел у списку
MIN_ARRAY_NUMBER = -100     # значення мінімального числа у списку
MAX_ARRAY_NUMBER = 100      # значення максимального числа у списку

# Генерація списку випадкових чисел
test_list_1 = [random.randint(MIN_ARRAY_NUMBER, MAX_ARRAY_NUMBER) for _ in range(COUNT_ARRAY_NUMBERS)]
test_list_2 = [random.randint(MIN_ARRAY_NUMBER, MAX_ARRAY_NUMBER) for _ in range(COUNT_ARRAY_NUMBERS)]
print(f"Сгенеровано перший список із {COUNT_ARRAY_NUMBERS} випадкових чисел від {MIN_ARRAY_NUMBER} до {MAX_ARRAY_NUMBER}: {test_list_1}")
print(f"Сгенеровано другий список із {COUNT_ARRAY_NUMBERS} випадкових чисел від {MIN_ARRAY_NUMBER} до {MAX_ARRAY_NUMBER}: {test_list_2}")
result = merge_lists(test_list_1, test_list_2)
print(f"Список, що містить елементи обох списків: {result}")
print()

# 6.
def raise_elements_to_powers(input_list: list, degree: int) -> list:
    """
    Функція зводить кожен елемент списку в заданий рівень.
    Параметри:
    input_list (list): Список цілих чисел.
    degree (int): Ступінь, у яку потрібно звести кожен елемент списку.
    Повертає:
    list: Новий список із результатами зведення у ступінь.
    """
    if not input_list:      # Перевірка на пустий список
        return None         # Повертаємо None, якщо список пустий
    return [element ** degree for element in input_list]


print("Програма обчислює ступінь кожного елемента списку цілих чисел та відображає новий список,"
      " який містить отримані результати.")

COUNT_ARRAY_NUMBERS = 5       # кількість чисел у списку
MIN_ARRAY_NUMBER = -100       # значення мінімального числа у списку
MAX_ARRAY_NUMBER = 100        # значення максимального числа у списку

# Генерація списку випадкових чисел
test_list = [random.randint(MIN_ARRAY_NUMBER, MAX_ARRAY_NUMBER) for _ in range(COUNT_ARRAY_NUMBERS)]
print(f"Сгенеровано список із {COUNT_ARRAY_NUMBERS} випадкових чисел від {MIN_ARRAY_NUMBER} до {MAX_ARRAY_NUMBER}:")
print(test_list)

while True:
    try:
        degree = int(input("Введіть ціле число значення ступеня для обчислення:"))
        # if isinstance(degree, int):
        break

    except Exception:
        print("Помилка! Введіть ціле число для видалення зі списку.")

result = raise_elements_to_powers(test_list, degree)
print("Модифікований список:")
print(result)
print()
