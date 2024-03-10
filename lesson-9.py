"""
Вивчення основних алгоритмів сортувань
Алгоритми пошуку: бінарний та лінійний
Приклади використання алгоритмів
Додаткове завдання:
Продебажити алгоритми розглянуті на уроці, написати короткі тези про кожен алгоритм.
Написати гру "Вгадай число" використовуючи бінарний пошук: гравець загадує число, пк відгадує і показує кількість спроб.
Усі результати надсилати мені в особисті повідомлення.
"""

import random

MIN_VALUE = -99
MAX_VALUE = 99
NUMBERS_OF_VALUE = 20

def bubbleSort(arr):
    swapped = False
    rearrangement = 0   # количество перестановок
    comparison = 0      # количество сравнений
    for i in range(len(arr) - 1):

        for j in range(len(arr) - i - 1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                rearrangement += 1
            comparison += 1

        if not swapped:
            return [rearrangement, comparison]

    return [rearrangement, comparison]


def selectionSort(arr):
    rearrangement = 0
    comparison = 0
    for index in range(len(arr)):
        min_index = index

        for j in range(index + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            comparison += 1
        arr[index], arr[min_index] = arr[min_index], arr[index]
        rearrangement += 1
    return [rearrangement, comparison]


def insertion_sort(array):
    rearrangement = 0
    comparison = 0
    for i in range(1, len(array)):
        key = array[i]
        j = i
        while (j - 1 >= 0) and (array[j - 1] > key):
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
            rearrangement += 1
            comparison += 1
        array[j] = key
        comparison += 1
    return [rearrangement, comparison]


arr = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(NUMBERS_OF_VALUE)]
arr_bubbleSort = arr.copy()
arr_selectionSort = arr.copy()
arr_insertion_sort = arr.copy()

print("Generated random array is:")
print(arr)

rearrangement, comparison = bubbleSort(arr_bubbleSort)
print()
print("The array after sorting in Ascending Order by BubbleSort sort is:")
print(arr_bubbleSort)
print(f"BubbleSort. Rearrangement: {rearrangement}, Comparison: {comparison}.")

rearrangement, comparison = selectionSort(arr_selectionSort)
print()
print('The array after sorting in Ascending Order by Selection sort is:')
print(arr_selectionSort)
print(f"BubbleSort. Rearrangement: {rearrangement}, Comparison: {comparison}.")

rearrangement, comparison = insertion_sort(arr_insertion_sort)
print()
print('The array after sorting in Ascending Order by Insertion sort is:')
print(arr_insertion_sort)
print(f"BubbleSort. Rearrangement: {rearrangement}, Comparison: {comparison}.")
print()

left_border = 1
right_border = 100

def guess_number(left_border=left_border, right_border=right_border):
    attempts = 0
    print(f"Загадайте число від {left_border} до {right_border}, і я спробую його вгадати.")
    print("Відповідайте ' < ' (менше), ' > ' (більше) , або ' + ' (вірно), щоб допомогти мені вгадати.")

    while True:
        guess = (left_border + right_border) // 2
        attempts += 1
        print(f"Моє припущення: {guess}. Ваша відповідь:", end=" ")
        response = input()

        match response:
            case "+":
                print(f"Ура! Я вгадав число за {attempts} спроб.")
                break
            case "<":
                right_border = guess - 1
            case ">":
                left_border = guess + 1
            case _:
                print("Будь ласка, введіть '<', '>', або '+'.")
                attempts -= 1

        if left_border > right_border:
            print("Здається, ви допустили помилку у своїх підказках. Давайте спробуємо ще раз.")
            break

guess_number()
