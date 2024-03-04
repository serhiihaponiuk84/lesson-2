# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

# import random
#
#
# def is_prime(number: int) -> bool:
#     is_number_prime = True
#
#     for num in range(2, number):
#         if number % num == 0:
#             is_number_prime = False
#             break
#
#     return is_number_prime
#
#
# def get_prime_numbers(numbers: list[int]) -> int:
#     prime_numbers_counter = 0
#
#     for num in numbers:
#         if is_prime(num):
#             print(num, end=" ")
#             prime_numbers_counter += 1
#
#     print()
#     return prime_numbers_counter
#
#
# my_numbers = [random.randint(1, 20) for _ in range(10)]
# print(my_numbers)
# result = get_prime_numbers(my_numbers)
# print(f"Prime numbers count: {result}")

####################
# def delete_item(numbers: list[int], number: int) -> int:
#     deleted_item_counter = 0
#
#     for item in numbers:
#         if item == number:
#             numbers.remove(item)
#             deleted_item_counter += 1
#
#     return deleted_item_counter
#
#
# nums = [1, 3, 1, 5, 2, 6, 1, 3, 2, 5]
# print(nums)
# result = delete_item(nums, 1)
# print(result)
# print(nums)

##################
# def hello(): print("Hello")
#
#
# print(hello)
# message = hello  # надав посилання на функцію в іншу змінну
# print(message)
#
# hello()
# message()

#######
# def add(a, b): return a + b
# def sub(a, b): return a - b
# def mult(a, b): return a * b
# def division(a, b): return a / b
#
#
# def select_math_operation(user_choice):
#     match user_choice:
#         case "+":
#             return add
#         case "-":
#             return sub
#         case "*":
#             return mult
#         case "/":
#             return division
#         case _:
#             raise Exception("Invalid operation!")
#
#
# try:
#     operation = input("Enter math operation: ")
#     math_operation = select_math_operation(operation)
#     result = math_operation(4, 9)
#     print(f"Result: {result}")
# except Exception as error:
#     print(error)

############
# message = lambda: print("Hello world!")
# message()

####
# square = lambda side_1, side_2: side_1 * side_2
# print(square(2, 4))

####
# def calculate(a, b, math_operation) -> None:
#     print(f"Result: {math_operation(a, b)}")
#
#
# calculate(2, 5, lambda n1, n2: n1 + n2)
# calculate(2, 5, lambda n1, n2: n1 / n2)

################
# def select_math_operation(user_choice):
#     match user_choice:
#         case "+":
#             return lambda a, b: a + b  # повернення посилання на функцію
#         case "-":
#             return lambda a, b: a - b
#         case "*":
#             return lambda a, b: a * b
#         case "/":
#             return lambda a, b: a / b
#         case _:
#             raise Exception("Invalid operation!")
#
#
# try:
#     operation = input("Enter math operation: ")
#     math_operation = select_math_operation(operation)
#     result = math_operation(4, 9)
#     print(f"Result: {result}")
# except Exception as error:
#     print(error)

############
# LEGB - почитати
# https://www.bestprog.net/uk/2020/07/29/python-the-scopes-of-names-in-python-local-names-visibility-rules-for-names-legb-rule-the-global-keyword-overriding-names-in-functions-ua/

#####
# області видимості
# number = 10
#
#
# def test() -> None:
#     number: int = 11  # перекриття глобальної змінної
#
#     if 1:
#         # number = 12
#
#         if 1:
#             # number = 13
#             print(number)
#     print(number)
#
#
# print(number)
# test()
# print(number)
# number = 35
# print(number)

##########
# number = 10
#
#
# def test():
#     global number
#     number = 11  # змінюємо значення глобальної змінної
#     print(number)
#
#
# print(number)
# test()
# print(number)

#########
# def outer():
#     number = 1
#
#     def inner():
#         nonlocal number
#         number = 2
#         print(number)
#
#     inner()
#     print(number)
#
#
# outer()

#############
###
# number = 10
#
#
# def outer():
#     global number
#     number = 1
#     new_number = number
#
#     def inner():
#         global number
#         nonlocal new_number
#         new_number = 2
#         print(new_number)
#         test = "Hello World!"
#         number = 2
#
#         def inner_number_2():
#             global number
#             nonlocal new_number
#             nonlocal test
#             print(new_number)
#             new_number = 3
#             print(new_number)
#             number = 3
#             test = "qqqqq"
#             print(test)
#
#         inner_number_2()
#
#     inner()
#     print(new_number)
#
#
# outer()
# print(number)

#####################
# Замикання (closure) представляє функцію, яка запам'ятовує своє лексичне оточення навіть у тому випадку,
# коли вона виконується поза своєю областю видимості.

# Зовнішня функція, яка визначає деяку область видимості і в якій визначені деякі
# Змінні та параметри - лексичне оточення
#
# Змінні та параметри (лексичне оточення), які визначені у зовнішній функції
#
# вкладена функція, яка використовує змінні та параметри зовнішньої функції

# def outer():
#     number = 10
#     print("outer")
#     test = 10
#     test_2 = 111
#
#     def inner():
#         nonlocal number
#         number += 1
#         # print(test)
#         print(number)
#         # print("hello")
#
#     return inner
#
#
# inner_func = outer()
# inner_func()
# inner_func()
# inner_func()

#####
# v1
# def multiply(num1):
#     def inner(num2): return num1 * num2
#     return inner

# v2
# def multiply(num1): return lambda num2: num1 * num2


# def multiply_v2(num1, num2):
#     return num1 * num2
#
#
# for i in range(1, 10):
#     print(f"{3} * {i} = {multiply_v2(3, i)}")


# number1 = 3
# mult_func = multiply(number1)
# print(mult_func(4))
# print(mult_func(5))
# print(mult_func(7))
#
# for number2 in range(1, 10):
#     print(f"{number1} * {number2} = {mult_func(number2)}")

# додаткове завдання:
# Вкладені функції, замикання, lambda -> почитати, продебажити та написати конспект

##########
#
# Рекурсія – коли функція викликає сама себе
# 1. продумати, яке або які параметри функції будуть змінені при рекурсивному виклику
# 2. визначити умову або умови виходу з рекурсії
# 3. запустити рекурсію (виклик цієї ж функції)

# 5! => 1 * 2 * ... * 5
# def factorial(number):
#     if number <= 1:
#         return 1
#
#     # factorial(number - 1) -> запуск рекурсії
#     return number * factorial(number - 1)
#
#
# print(factorial(5))
# #
# #
# # factorial(5) -> 5 * factorial(4) => 120
# # factorial(4) -> 4 * factorial(3) => 24
# # factorial(3) -> 3 * factorial(2) => 6
# # factorial(2) -> 2 * factorial(1) => 2
# # factorial(1) => 1

####
# Написати рекурсивну функцію знаходження ступеня числа.
# def my_pow(number, power):
#     if power <= 1:
#         return number
#
#     return number * my_pow(number, power - 1)
#
#
# print(my_pow(2, 3))

# my_pow(2, 3) -> 2 * my_pow(2, 2) => 8
# my_pow(2, 2) -> 2 * my_pow(2, 1) => 4
# my_pow(2, 1) => 2
