# # створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
# import random
#
# numbers = []
#
# for i in range(5):
#     numbers.append([])
#     for j in range(5):
#         numbers[i].append(random.randint(10, 99))
#
# for i in range(5):
#     for j in range(5):
#         print(numbers[i][j], end=" ")
#     print()
#
# # - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю
# # (аналогічно зробити з рядком)
#
# first_col = 2
# second_col = 4
#
# if 0 < first_col <= 5 and 0 < second_col <= 5:
#     for i in range(5):
#         numbers[i][first_col - 1], numbers[i][second_col - 1] = numbers[i][second_col - 1], numbers[i][first_col - 1]
# else:
#     print("Invalid columns!")
#
# print()
# for i in range(5):
#     for j in range(5):
#         print(numbers[i][j], end=" ")
#     print()
#
# print()
# first_row = 2
# second_row = 4
#
# if 0 < first_row <= 5 and 0 < second_row <= 5:
#     numbers[first_row - 1], numbers[second_row - 1] = numbers[second_row - 1], numbers[first_row - 1]
#     # print(numbers[first_row - 1])
#     # print(numbers[second_row - 1])
# else:
#     print("Invalid rows!")
#
# for i in range(5):
#     for j in range(5):
#         print(numbers[i][j], end=" ")
#     print()
#
# print()

#############
# def say_hello():
#     print("Hello")
#
#
# try:
#     number = 10
#     print(number)
#     print(say_hello)
#     say_hello()  # виклик функції (функція починає працювати)
#     say_hello()
# except Exception:
#     print("Something went wrong")
#
#
# def say_hello():
#     print("Hello Friends!")
#
#
# say_hello()
#
#
# def say_hello(name):
#     print(f"Hello {name}!")
#     name = "qqqq"
#     print(f"Hello {name}!")
#
#
# say_hello("Test user")
# name = "Anton"
# say_hello(name)
# print(name)

# def say_hello_name(username):
#     print(f"Hello, {username}")
#
#
# say_hello_name("Vasya")
# name = "Petya"
# say_hello_name(name)
#
# number: int = 10
# print(number)

# def user_info(name: str, age: int, hobby: str) -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# try:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     user_hobby = input("Enter your hobby: ")
#     user_info(name, age, user_hobby)
# except Exception as e:
#     print(e)

########
# після того як відпрацює ключове слово return - функція припиняє свою роботу (тільки функція)
# return – поверне результат роботи функції. Після відпрацьовування return - решта дій функції не відпрацюють
# та функція завершить свою роботу. Якщо у функції є цикл - у циклi return працює як break,
# але на відміну від break – поверне результат, а не просто
# Зупинить дії. Якщо функції є цикли, і в одному з циклів спрацював return - функція припинить свою роботу.
# ключове слово return може зустрічатися в тілі функції скільки завгодно разів

# if isinstance(n1, int) or isinstance(n1, float)
# def add(n1, n2): return n1 + n2
#
#
# def sub(n1, n2):
#     return n1 - n2
#
#
# def mult(n1, n2):
#     return n1 * n2
#
#
# def division(n1, n2):
#     return n1 / n2
#
#
# def calculate() -> None:
#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
#     math_operation = input("Enter math operation + - * / ")
#
#     match math_operation:
#         case "+":
#             print(f"{first_number} {math_operation} {second_number} = {add(first_number, second_number)}")
#         case "-":
#             print(f"{first_number} {math_operation} {second_number} = {sub(first_number, second_number)}")
#         case "*":
#             print(f"{first_number} {math_operation} {second_number} = {mult(first_number, second_number)}")
#         case "/":
#             print(f"{first_number} {math_operation} {second_number} = {division(first_number, second_number)}")
#         case _:
#             raise Exception("Invalid math operation!")
#
#
# try:
#     calculate()
# except ZeroDivisionError:
#     print("Do not divide by zero please!")
# except Exception as error:
#     print(error)

###
# def test():
#     return 10
#
#
# print(test())
#
#
# def test():
#     print("hello")
#
#
# print(test())
###

# def user_info(name: str, age: int = 18, hobby: str = "no hobby") -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# # user_info("Vasya", 33, "test")
# # user_info("Vasya", 33)
# # user_info("Vasya")
#
# # user_info("walking", "Petya", 33)
# user_info(hobby="walking", name="Petya", age=33)

#####
## Усі параметри,
# які розташовуються праворуч від символу *, отримують значення лише на ім'я:

# def print_person(name, *, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Bob", age=41, company="Microsoft")
#
#
# def print_person(*, name, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person(name="Bob", age=41, company="Microsoft")

# Якщо навпаки треба визначити параметри, яким можна передавати значення лише за позицією,
# тобто позиційні параметри, можна використовувати символ /: всі параметри, які йдуть до символу / ,
# є позиційними і можуть отримувати значення лише за позицією

# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Tom", company="JetBrains", age=24)  # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)

#
# def print_person(name, /, age=18, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Sam", company="Google")  # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company="JetBrains")  # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", company="Microsoft", age=42)  # Name: Bob  Age: 42  company: Microsoft

####
# import random
# import string
#
# PASSWORD_DATA = string.ascii_letters + string.digits + string.punctuation
# MIN_PASSWORD_LENGTH = 16
# MAX_PASSWORD_LENGTH = 32
#
#
# def generate_password(password_length: int, initial_password_data: str) -> str:
#     if password_length < MIN_PASSWORD_LENGTH or password_length > MAX_PASSWORD_LENGTH:
#         raise Exception(f"Provided password length must be between {MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH}")
#     password = ""
#     for _ in range(password_length):
#         password += random.choice(initial_password_data)
#
#     return password
#
#
# try:
#     new_password = generate_password(1, PASSWORD_DATA)
#     print(f"New password: {new_password}")
# except Exception as error:
#     print(error)

###############
# import random
#
# words = ["Cat", "Apple", "Dog", "Letter", "Helicopter"]
#
# secret_word = random.choice(words)
# # print(secret_word)
#
# # print("_" * len(secret_word))
# user_word = ["_"] * len(secret_word)
#
# attempts_counter = 0
#
# while True:
#     # v1
#     if "".join(user_word).find("_") == -1:
#         print(f"\nYou guessed the word {secret_word}!\nAttempts: {attempts_counter}")
#         break
#     # v2
#     # if "".join(user_word).lower() == secret_word.lower():
#     #     print(f"\nYou guessed the word {secret_word}!\nAttempts: {attempts_counter}")
#     #     break
#
#     print(" ".join(user_word))
#
#     letter = input("Enter a letter: ").strip().lower()
#
#     if not letter.isalpha() or len(letter) != 1:
#         print("Please enter only one letter!")
#         continue
#
#     attempts_counter += 1
#
#     for i in range(len(secret_word)):
#         if letter == secret_word[i].lower():
#             user_word[i] = letter

# добавить ограничение на кол-во попыток, если не уложились в кол-во - проиграли

# добавить:
# - два уровня сложности
# легкий уровень: кол-во попыток равно длина слова * 2 -> если не угадал - вывести сообщение об этом
# сложный уровень: кол-во попыток равно длина слова * 1.5 -> если не угадал - вывести сообщение об этом
# показывать сколько попыток осталось
# - обработку исключений
