# try:
#     num1, num2 = int(input("Enter first number: ")), int(input("Enter second number: "))
#     result = num1 / num2
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Invalid value")
# except Exception as error:
#     print(error)
#
# print("Hello")

###
# Цикли
# - while
# - for

# v1
# i = 0
#
# while i < 10:
#     print(i, end=" ")
#     i += 1  # i = i + 1
#
#
# print("test")
#
# v2
# i = 12
#
# while True:
#     print(i)
#     i += 2

# v3
# i = 0
#
# while True:
#     if i == 5:
#         i += 1
#         print("continue...")
#         continue  # пропустить подальші дії циклу, але цикл не зупиниться
#
#     if i > 10:
#         print("break...")
#         break  # цикл зупиниться (повне завершення циклу)
#
#     print(i)
#
#     i += 1
#
# print("Hello")

###
# Користувач вводить з клавіатури числа
# якщо користувач ввів 0 -> припинити введення чисел
# в кінці вивести середню арифметичну числову послідовність

sum_num = 0
count = 0

# v1
# try:
#     while True:
#         num = int(input("Enter number: "))
#
#         if num == 0:
#             print("end...")
#             break
#
#         sum_num += num
#         count += 1
#
#     average = sum_num / count
#     print(f"sum num: {sum_num}")
#     print(f"count: {count}")
#     print(f"average: {average}")
# except ValueError as e:
#     print("Enter numbers only")
# except Exception as e:
#     print(e)

# v2
# try:
#     while True:
#         try:
#             num = int(input("Enter number: "))
#
#             if num == 0 and count == 0:
#                 print("Please enter a number")
#                 continue
#
#             if num == 0:
#                 print("end...")
#                 break
#
#             sum_num += num
#             count += 1
#         except ValueError as e:
#             print("Enter numbers only")
#
#     average = sum_num / count
#     print(f"sum num: {sum_num}")
#     print(f"count: {count}")
#     print(f"average: {average}")
#
# except Exception as e:
#     print(e)

########################
#
# for i in range(5):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(2, 5):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(1, 5, 2):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# for i in range(start, end + 1):
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# for i in range(end, start - 1, -2):
#     # print("Hello")
#     print(i, end=" ")

####
# for value in 1, 3, "sdfg", True, "Sdfgsdfdg":
#     print(value)

####
# Показати на екран усі прості числа в діапазоні, вказаному користувачем.
#
# Число називається простим, якщо воно ділиться без залишку тільки на себе і на одиницю.
#
# Наприклад, три - це просте число, а чотири - ні.

# start = int(input("Enter start value: "))
# end = int(input("Enter end value: "))
#
# # v1
# if start > end:
#     start, end = end, start

# v2
# if start > end:
#     temp = start
#     start = end
#     end = temp

##
# for number in range(start, end + 1):
#     is_simple = True
#
#     if number < 2:
#         continue
#
#     for i in range(2, number):
#         if number % i == 0:
#             is_simple = False
#             break
#
#     if is_simple:
#         print(number, end=" ")

#############################
# message = "hello world"
# message_1 = 'hello world'
# print(message)
#
# text = ("hello"
#         "world")
# print(text)
#
# # raw строка
# text = '''
# qwerrty
#     asdfadsvf
#         asdvsvb
# '''
#
# print(text)
#
# # v1
# path = r"C:\Users\admin\PycharmProjects\FastAPI_materials"
# print(path)
# # v2
# path = "C:\\Users\\admin\\PycharmProjects\\FastAPI_materials"
# print(path)
#
# #
# print("hello, \"world\"\n\tfrom program")

#
# dogs, cats = 12, 15
# result = f"Dogs {dogs} and cats {cats}"
# print(result)
#
# result = "Dogs {} and cats {}".format(dogs, cats)
# print(result)
#
# result = "Dogs {1} and cats {0}".format(dogs, cats)
# print(result)
#
# result = "Dogs {1} and cats {1}".format(dogs, cats)
# print(result)

###
# message = "hello world"
# # [] -> індексатори
# # Індекс - це порядковий номер елемента в колекції (масиві). Note: не всі колекції підтримують індекси.
# # Індекси рахуються з нуля
# print(message[0])
# print(len(message))  # кількість символів у рядку
# # print(message[len(message)])  # IndexError: string index out of range
# print(message[len(message) - 1])
# print(message[-1])

###
# # string - immutable тип даних, рядок змінити не можна
# name = "Petya"
# print(name)
# # name[1] = "r"  # TypeError: 'str' object does not support item assignment
# user_name = "Vasya"
# name = user_name
# print(name)

# # v1
# sentence = "Hello, world"
# for letter in sentence:
#     print(letter, end=" ")
#
# print()
#
# # v2
# for i in range(len(sentence)):
#     print(sentence[i], end=" ")

# slices (срезы)
# sentence = "Hello, world"
# print(sentence[:])
# print(sentence[0:])
# print(sentence[2:])
# print(sentence[2:8])
# print(sentence[1:10:2])
# print(sentence[::-1])

#
# name = "Vasya"
# surname = "Petrov"
# age = 33
#
# fullname = name + " " + surname + " " + str(age)  # конкатенація (додавання рядків)
# print(fullname)

#
# text = "Hello, world" * 3
# print(text)

# print("---" * 10)

# a1 = "abc"
# a2 = "abs"
#
# if a1 > a2:
#     print(a1)
# else:
#     print(a2)\
#
# print(ord("A"))
# print(chr(98))

####
# text = "helLo woRlD"
#
# # isalpha(): повертає True, якщо рядок складається лише з алфавітних символів
#
# print(text.isalpha())
#
# # islower(): повертає True, якщо рядок складається лише із символів у нижньому регістрі
#
# print(text.islower())
#
# # isupper(): повертає True, якщо всі символи рядка у верхньому регістрі
#
# print(text.isupper())
#
# # isdigit(): повертає True, якщо всі символи рядка - цифри
#
# print(text.isdigit())
#
# # isnumeric(): повертає True, якщо рядок є числом
#
# print(text.isnumeric())
#
# # startswith(str): повертає True, якщо рядок починається з підрядка str
#
# print(text.startswith("helLo"))
#
# # endswith(str): повертає True, якщо рядок закінчується на підрядок str
#
# print(text.endswith("D"))
#
# # lower(): перекладає рядок у нижній регістр
#
# print(text.lower())
#
# # upper(): перекладає рядок у верхній регістр
#
# print(text.upper())
#
# # title(): початкові символи всіх слів у рядку перекладаються у верхній регістр
#
# print(text.title())
#
# # capitalize(): перекладає у верхній регістр першу літеру тільки першого слова рядка
#
# print(text.capitalize())

# fio = input("Enter fio: ").title()
# print(fio)

#
# # lstrip(): видаляє початкові пробіли з рядка
# text = "helLo woRlD"
# print(text)
# print(text.lstrip())
#
# # rstrip(): видаляє кінцеві пробіли з рядка
# print(text)
# print(text.rstrip())
#
# # strip(): видаляє початкові та кінцеві пробіли з рядка
# print(text)
# print(text.strip())
#
# # ljust(width): якщо довжина рядка менша за параметр width, то праворуч від рядка додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється по лівому краю
# text = "hello world"
# print(text)
# print(text.ljust(20))
#
# # rjust(width): якщо довжина рядка менша за параметр width, то зліва від рядка додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється праворуч
# text = "hello world"
# print(text)
# print(text.rjust(20))
#
# # center(width): якщо довжина рядка менша за параметр width, то ліворуч і праворуч від рядка рівномірно додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється по центру
# text = "hello world"
# print(text)
# print(text.center(20))

# find(str[, start [, end]): повертає індекс підрядка у рядку. Якщо підрядок не знайдено, повертається число -1
# text = "hello world"
# print(text.find("hello"))  # 0
# print(text.find("l"))  # 2
# print(text.rfind("l"))  # 9
#
# first_found_index = text.find("l")
# print(text.find("l", first_found_index + 1))
#
# print(text.find("p"))  # -1
#
# # v1
# for i in range(len(text)):
#     if text[i] == "l":
#         print(i)
#
# # v2
# index = 0
#
# for letter in text:
#     if letter == "l":
#         print(index)
#     index += 1

#

# # replace(old, new[, num]): замінює в рядку один підрядок на інший
# text = "hello world hello"
# print(text)
#
# text = text.replace("hello", "goodbye", 1)
# print(text)

