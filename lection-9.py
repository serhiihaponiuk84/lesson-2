# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)
import math
from random import randint


# def show_star(symbol, symbol_counter):
#     if symbol_counter <= 0:
#         return
#
#     print(symbol, end=" ")
#     show_star(symbol, symbol_counter - 1)
#
#
# show_star("*", 5)

# show_star("*", 3) -> show_star(symbol, 2)
# show_star(symbol, 2) -> show_star(symbol, 1)
# show_star(symbol, 1) -> show_star(symbol, 0) => return

###
# Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим
# чином і знаходить позицію, з якої починається послідовність із 10 чисел, сума яких мінімальна.

# def find_min_sum_index(numbers: list[int], start_index: int, end_index: int, min_sum=math.inf, min_index=0) -> int:
#     if end_index < len(numbers):
#         current_sum = sum(numbers[start_index:end_index + 1])
#
#         if current_sum < min_sum:
#             min_sum = current_sum
#             min_index = start_index
#
#         print(f"Current sum: {current_sum} Min sum: {min_sum}, min_index: {min_index}")
#
#         return find_min_sum_index(numbers, start_index + 1, end_index + 1, min_sum, min_index)
#
#     return min_index
#
#
# nums = [randint(1, 10) for _ in range(100)]
# print(nums)
# print(f"Result: {find_min_sum_index(nums, 0, 9)}")

##################

def bubble_sort(arr):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True


def selection_sort(arr):
    for i in range(len(arr)):
        lowest_value_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j
        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item_to_insert


def merge(left_arr, right_arr):
    merged_arr = []
    left_arr_index = right_arr_index = 0
    left_arr_length, right_arr_length = len(left_arr), len(right_arr)

    for _ in range(left_arr_length + right_arr_length):
        if left_arr_index < left_arr_length and right_arr_index < right_arr_length:
            # порівнюємо перші елементи на початку кожного списку
            # якщо перший елемент лівого підписку менший - додаємо його
            if left_arr[left_arr_index] <= right_arr[right_arr_index]:
                merged_arr.append(left_arr[left_arr_index])
                left_arr_index += 1
            else:
                merged_arr.append(right_arr[right_arr_index])
                right_arr_index += 1

        # якщо досягнуто кінця лівого списку - елементи правого списку додамо до кінця sorted_list
        elif left_arr_index == left_arr_length:
            merged_arr.append(right_arr[right_arr_index])
            right_arr_index += 1
        # якщо досягнуто кінця правого списку - елементи лівого списку додамо до кінця sorted_list
        elif right_arr_index == right_arr_length:
            merged_arr.append(left_arr[left_arr_index])
            left_arr_index += 1
    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


###
def partition(arr, low_index, high_index):
    # вибираємо середній елемент як опорний
    # так само можливий вибір першого, останнього або довільного ел-тов як опорного
    pivot = arr[(low_index + high_index) // 2]
    i = low_index - 1
    j = high_index + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j
        # Якщо елемент з індексом i (ліворуч від опорного) більше ніж елемент з індексом j (праворуч від опорного) -
        # то міняємо їх місцями
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr):
    def _quick_sort(items, low_index, high_index):
        if low_index < high_index:
            split_index = partition(items, low_index, high_index)
            _quick_sort(items, low_index, split_index)
            _quick_sort(items, split_index + 1, high_index)

    _quick_sort(arr, 0, len(arr) - 1)


# numbers = [randint(1, 100) for i in range(6)]
# numbers = [3, 3, 1, 4, 2, 6, 1, 9]
# print(numbers)
# # 1
# # bubble_sort(numbers)
# # 2
# # selection_sort(numbers)
# # 3
# # insertion_sort(numbers)
# # 4
# # numbers = merge_sort(numbers)
# # 5
# quick_sort(numbers)
# print(numbers)

####
# def linear_search(arr, item):
#     for i in range(len(arr)):
#         if arr[i] == item:
#             return i
#     return -1  # -1 означає, що значення не знайдено
#
#
# numbers = [3, 3, 1, 4, 2, 6, 1, 9]
# print(linear_search(numbers, 41))

###
# бінарний пошук працює ТІЛЬКИ на відсортованому масиві
def binary_search(arr, search_value):
    first_index = 0
    last_index = len(arr) - 1

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        if arr[mid_index] == search_value:
            return mid_index
        else:
            if search_value < arr[mid_index]:
                last_index = mid_index - 1
            else:
                first_index = mid_index + 1
    return -1  # -1 означає, що значення не знайдено


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(binary_search(numbers, 2))















