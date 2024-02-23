'''
Завдання 1
У списку цілих, заповненому випадковими числами обчислити:
■ Суму негативних чисел;
■ Суму парних чисел;
■ Суму непарних чисел;
■ Добуток елементів з кратними індексами 3;
■ Добуток елементів між мінімальним та максимальним елементом;
■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.

Завдання 2
Є список цілих, заповнений випадковими числами.
На підставі даних цього масиву потрібно:
■ Створити список цілих, що містить лише парні числа з першого списку;
■ Створити список цілих, що містить лише непарні числа з першого списку;
■ Створити список цілих, що містить лише негативні числа з першого списку;
■ Створити список цілих, що містить лише позитивні числа з першого списку.

Додаткові завдання по матрицях:
створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
вивести на екран
- вивести суму чисел головної діагоналі матриці
- вивести мінімальне та максимальне значення побічної діагоналі матриці
- ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
- ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю (аналогічно зробити з рядком)
'''

import random

# 1.
print("Перше завдання.")
# Генерація списку випадкових чисел
numbers = [random.randint(-100, 100) for _ in range(20)]
print("Список чисел:", numbers)

# Ініціалізація змінних для підсумовування і добутку
sum_negative = 0
sum_even = 0
sum_odd = 0
product_of_elements_index_3 = 1
product_between_min_max = 1
sum_between_positives = 0

# Пошук мінімального і максимального елемента та їх індексів
min_value = float('inf')
max_value = float('-inf')
min_index = max_index = -1
first_positive_index = last_positive_index = -1
i = 0  # Індекс поточного елемента

for num in numbers:
    if num < min_value:
        min_value = num
        min_index = i
    if num > max_value:
        max_value = num
        max_index = i
    if num < 0:
        sum_negative += num
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
    if i % 3 == 2:
        product_of_elements_index_3 *= num
    if first_positive_index == -1 and num > 0:
        first_positive_index = i
    if num > 0:
        last_positive_index = i
    i += 1

# Обчислення добутку між мінімальним та максимальним елементом
if min_index < max_index:
    for i in range(min_index + 1, max_index):
        product_between_min_max *= numbers[i]
else:
    product_between_min_max = None

# Обчислення суми між першим та останнім позитивними елементами
if first_positive_index != -1 and last_positive_index != -1 and first_positive_index < last_positive_index:
    for num in numbers[first_positive_index + 1:last_positive_index]:
        sum_between_positives += num

# Виведення результатів
print("Сума негативних чисел:", sum_negative)
print("Сума парних чисел:", sum_even)
print("Сума непарних чисел:", sum_odd)
print("Добуток елементів з кратними індексами 3:", product_of_elements_index_3)
print("Добуток елементів між мінімальним та максимальним елементом:", product_between_min_max if product_between_min_max is not None else "Не може бути обчислений")
print("Сума елементів між першим та останнім позитивними елементами:", sum_between_positives)
print()

# 2.
print("Друге завдання.")
# Генерація списку цілих чисел
numbers = [random.randint(-100, 100) for _ in range(20)]
print("Початковий список чисел:", numbers)

# Створення списків для парних, непарних, негативних та позитивних чисел
even_numbers = []
odd_numbers = []
negative_numbers = []
positive_numbers = []

# Заповнення списків без використання спискових включень
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

    if num < 0:
        negative_numbers.append(num)
    elif num > 0:
        positive_numbers.append(num)

# Виведення результатів
print("Список парних чисел:", even_numbers)
print("Список непарних чисел:", odd_numbers)
print("Список негативних чисел:", negative_numbers)
print("Список позитивних чисел:", positive_numbers)
print()

# 3.
print("Третє завдання (додаткове).")
# Генерація матриці 10 на 10 без використання inline list comprehension
matrix = []
for _ in range(10):
    row = []
    for _ in range(10):
        row.append(random.randint(10, 99))
    matrix.append(row)

# Виведення матриці на екран
for row in matrix:
    print(row)

# Сума чисел головної діагоналі матриці
sum_main_diagonal = 0
for i in range(10):
    sum_main_diagonal += matrix[i][i]

# Визначення мінімального та максимального значення побічної діагоналі матриці
min_secondary_diagonal = matrix[0][9]
max_secondary_diagonal = matrix[0][9]
for i in range(10):
    value = matrix[i][9-i]
    if value < min_secondary_diagonal:
        min_secondary_diagonal = value
    if value > max_secondary_diagonal:
        max_secondary_diagonal = value

# Виведення результатів
print()
print("Сума чисел головної діагоналі:", sum_main_diagonal)
print("Мінімальне значення побічної діагоналі:", min_secondary_diagonal)
print("Максимальне значення побічної діагоналі:", max_secondary_diagonal)
print()

class InvalidNumber(Exception):
  pass

# Для виводу стовпця і рядка матриці
# Вивід стовпця за номером
while True:
    try:
        column_index = int(input("Введіть номер стовпця матриці, котрий потрібно вивести на екран (1-10): "))
        if column_index < 0 or column_index > 10:
            raise InvalidNumber("Некорректне введення. В матриці усього 10 стовпців.")
            continue
        else:
            print(f"Програма відобразить стовпець {column_index} на екран...")
            break

    except InvalidNumber as error:
        print(error)
    except Exception:
        print("Некорректне введення. Введене значення повинно бути цілим числом від 1 до 10.")

column = []

for i in range(10):
    column.append(matrix[i][column_index - 1])

print(column)
print()

# Вивід рядка за номером
while True:
    try:
        row_index = int(input("Введіть номер рядка матриці, котрий потрібно вивести на екран (1-10): "))
        if row_index < 0 or row_index > 10:
            raise InvalidNumber("Некорректне введення. В матриці усього 10 рядків.")
            continue
        else:
            print(f"Програма відобразить рядок {column_index} на екран...")
            break

    except InvalidNumber as error:
        print(error)
    except Exception:
        print("Некорректне введення. Введене значення повинно бути цілим числом від 1 до 10.")

print(matrix[row_index - 1])
print()

# Для заміни стовпців місцями
while True:
    try:
        column_index_1 = int(input("Введіть перший з номерів стовпців, котрі потрібно змінити місцями (1-10): "))
        column_index_2 = int(input("Введіть другий з номерів стовпців, котрі потрібно змінити місцями (1-10): "))
        if column_index_1 < 0 or column_index_1 > 10 or column_index_2 <0 or column_index_2 > 10:
            raise InvalidNumber("Некорректне введення. В матриці усього 10 стовпців.")
            continue
        elif column_index_1 == column_index_2:
            raise InvalidNumber("Некорректне введення. Потрібно ввести різні номери стовпців для заміни.")
            continue
        else:
            print(f"Програма замінить стовпці {column_index_1} та {column_index_2} місцями...")
            break

    except InvalidNumber as error:
        print(error)
    except Exception:
        print("Некорректне введення. Введене значення повинно бути цілим числом від 1 до 10.")

# Заміна стовпів місцями
for i in range(10):
    matrix[i][column_index_1 - 1], matrix[i][column_index_2 - 1] = matrix[i][column_index_2 - 1], matrix[i][column_index_1 - 1]

print(f"Матриця після зміни стовпців {column_index_1} та {column_index_2} місцями:")
for row in matrix:
    print(row)
print()

# Для заміни рядків місцями
while True:
    try:
        row_index_1 = int(input("Введіть перший з номерів рядків, котрі потрібно змінити місцями (1-10): "))
        row_index_2 = int(input("Введіть другий з номерів рядків, котрі потрібно змінити місцями (1-10): "))
        if row_index_1 < 0 or row_index_1 > 10 or row_index_2 <0 or row_index_2 > 10:
            raise InvalidNumber("Некорректне введення. В матриці усього 10 рядків.")
            continue
        elif row_index_1 == row_index_2:
            raise InvalidNumber("Некорректне введення. Потрібно ввести різні номери рядків для заміни.")
            continue
        else:
            print(f"Програма замінить рядки {row_index_1} та {row_index_2} місцями...")
            break

    except InvalidNumber as error:
        print(error)
    except Exception:
        print("Некорректне введення. Введене значення повинно бути цілим числом від 1 до 10.")

# Заміна рядків місцями
matrix[row_index_1 - 1], matrix[row_index_2 - 1] = matrix[row_index_2 - 1], matrix[row_index_1 - 1]

print(f"Матриця після заміни рядків {row_index_1} та {row_index_2} місцями:")
for row in matrix:
    print(row)
