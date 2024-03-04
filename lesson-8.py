"""
Важливо: не використовувати цикли для реалізації основної логіки.
Потрібно використати рекурсію.
Цикл можна використовувати лише у 4 завданні для знаходження суми чисел.
Завдання 1.
Написати рекурсивну функцію знаходження ступеня числа.
Завдання 2.
Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
Проілюструйте роботу функції прикладом. (Протестувати)
Завдання 3.
Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
Користувач вводить a та b. Проілюструйте роботу функції прикладом.
Додатково:
Завдання 4.
Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим чином
і знаходить позицію, з якої починається послідовність із 10 чисел, сума яких мінімальна.
"""
import random

# 1.
def power(base: int, exponent: int) -> int:
    """
    Рекурсивна функція обчислення ступеня числа.
    Параметри:
    base (int): Число, яке зводиться до ступеня.
    exponent (int): Показник ступеня, у якому зводиться число.
    Повертає:
    int: Результат зведення числа base у ступінь exponent.
    """
    # Базовий випадок
    if exponent == 0:
        return 1
    # Рекурсивний випадок
    return base * power(base, exponent - 1)


base = random.randint(1, 10)
exponent = random.randint(1, 10)
print(f"Результат зведення числа {base} у ступінь {exponent} складає {power(base, exponent)}.")
print()


# 2.
def print_stars(n: int) -> None:
    """
    Рекурсивна функція для виведення N зірок у ряд.
    Параметри:
    n (int): Кількість зірок, які потрібно вивести.
    """
    if n == 0:
        return
    print('*', end='')
    print_stars(n - 1)

number = random.randint(1, 10)
print(f"Кількість зірок, які потрібно вивести: {number}.")
print_stars(number)
print()


# 3.
def sum_range(start: int, end: int) -> int:
    """
    Рекурсивна функція для обчислення суми всіх чисел у діапазоні від start до end.
    Параметри:
    start (int): Початок діапазону.
    end (int): Кінець діапазону.
    Повертає:
    int: Сума всіх чисел у діапазоні.
    """
    if start >= end:
        return 0
    return start + sum_range(start + 1, end)


min_number = random.randint(1, 20)
max_number = random.randint(1, 20)

if min_number > max_number:
    min_number, max_number = max_number, min_number

print(f"Сума всіх чисел від {min_number} до {max_number} дорівнює: {sum_range(min_number, max_number)}")
"""
sum_range(6, 10) = 6 + sum_range(7, 10) = 6 + 24 = 30
sum_range(7, 10) = 7 + sum_range(8, 10) = 7 + 17 = 24
sum_range(8, 10) = 8 + sum_range(9, 10) = 8 + 9 = 17
sum_range(9, 10) = 9 + sum_range(10, 10) = 9 + 0 = 9
sum_range(10, 10) = 0
"""
print()


# 4 (Додаткове).
sequence_length = 10
best_sum = float('inf')
best_start = 0
def find_min_sum_sequence(arr, start=0):
    global best_sum, best_start
    if start > len(arr) - sequence_length:
        return best_start
    current_sum = sum(arr[start:start+sequence_length])
    if current_sum < best_sum:
        best_sum = current_sum
        best_start = start
    return find_min_sum_sequence(arr, start+1)

# Генерація масиву з 100 випадкових чисел
arr = [random.randint(1, 100) for _ in range(100)]

position = find_min_sum_sequence(arr)
print(f"Позиція, з якої починається послідовність із {sequence_length} чисел, сума яких мінімальна: {position}")
print(f"Мінімальна сума послідовності із {sequence_length} чисел з позиції № {best_start}: {best_sum}")
print()