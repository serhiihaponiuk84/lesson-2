# ввести з клавіатури тризначне число та вивести суму цифр цього числа
# // %
# int() - так як input поверне str, нам потрібно цей рядок привести до типу int (ціле число)
# щоб можна було застосовувати арифметичні оператори
# number = int(input("Enter 4-digit number: "))
# # # 3467
# n1 = number // 1000  # 3
# n2 = number // 100 % 10
# n3 = number % 100 // 10
# n4 = number % 10
#
# result = n1 + n2 + n3 + n4
# print(f"n1: {n1} n2: {n2} n3 {n3} n4 {n4}")
# print(f"Result: {result}")

# number = 10
# print(number)

###############
# 1. Користувач вводить три цифри з клавіатури. Необхідно знайти суму чисел, добуток чисел.
# Результат обчислень вивести на екран.
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# number3 = int(input("Enter third number: "))
# numbers_sum = number1 + number2 + number3
# numbers_mult = number1 * number2 * number3
# print(f"Sum: {numbers_sum}")
# print(f"Mult: {numbers_mult}")

# 2. Напишіть програму, яка обчислює площу ромба. Користувач із клавіатури вводить довжину двох його діагоналей.
# Площа ромба дорівнює половині добутку його діагоналей: S = (AC · BD)/2.
# first_diagonal = int(input("Enter the first diagonal: "))
# second_diagonal = int(input("Enter the second diagonal: "))
# area = (first_diagonal * second_diagonal) / 2
# print("Area:", area)

#######
# умови
# v1
# n1 = 10
# n2 = 20
# v2
# n1, n2 = 10, 20  # множинне привласнення
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2)  # поверне True якщо обидва операнди рівні (однакові)
# print(n1 != n2)  # поверне True якщо обидва операнди різні
#
# print(1 == 1 and 3 == 3)  # поверне True якщо обидва операнди рівні True, інакше False
# print(1 == 1 or 2 == 3)  # поверне True якщо хоча б один операнд дорівнює True, інакше False
#
# is_valid = False
# print(is_valid)
# print(not is_valid)  # not -> інверсія, якщо значення False стане True, і навпаки
#
# print("hello" in "hello world")

#############
# hours = int(input("Enter hours: "))
#
# if 12 <= hours <= 23:
#     print("PM")
# elif 0 <= hours < 12:
#     print("AM")
# else:
#     print("Incorrect hours!")

##
# ввести рейтинг фільму: якщо рейтинг дорівнює 5 або 4 - ок, інакше - погано
# film_rating = int(input("Enter film rating: "))
#
# if film_rating > 0 and film_rating <= 5:
#     if film_rating == 4 or film_rating == 5:
#         print("OK!")
#     else:
#         print("Not OK!")
# else:
#     print("Incorrect rating!")
#
# print("Hello world!")

###############
