# print("Hello world!")
# print('hello')

# однорядковий коментар

'''
три одинарні лапки
багаторядковий
коментар
тут можна писати будь-який текст і він буде проігнорований інтерпретатором
'''

# Ctrl + / -> comment или uncomment

# print("hello11")
# print("hello22")
#
# aljfjklsdfjkvskjfd
# print("qwerty")

########
# escape послідовності
# \n -> перенесення на новий рядок
# print("Hello\nworld")
# \t -> табуляція -> 4 пробіли. (буває в консолі 2 або 8 пробіли)
# print("Hello\n\tworld")
# \ -> дзеркалювання, екранування – якщо необхідно службовий символ зробити друкованим
# print("Hello\\n\\t\"world\"")
# print("\\\\\\\\\\")
# print("\n" * 10)

###
# print("Hello world", "Text1", "Text2", sep=", ", end=" ")
# print("Hello world")
# print('test')

#####
# int -> ціле число 12
# float -> дробове число 12.5
# bool -> логічний тип даних: True False
# str -> рядок - масив (набір) символів

# Змінна - це іменована область оперативної пам'яті значення можна змінювати
# number = 10  # = оператор присвоєння
# print(number)
# print(type(number))
# number = 20.5
# print(number)
# print(type(number))
# number = "Vasya"
# print(number)
# print(type(number))
# number = True
# print(number)
# print(type(number))

# userName = "Petya"
# print(userName)
# user_name = "Vasya"
# print(user_name)

###########
# + - * /
# print(2 + 3)
# print(2 - 3)
# print(2 * 3)
# print(2 / 3)
# print(2 ** 3)  # основа ** показник (зведення в ступінь
# print(2 // 3)  # ціла частина від розподілу
# print(2 % 3)  # залишок від ділення
#
# num1 = 15
# num2 = 8
# print(num1 // num2)
# print(num1 % num2)

####
# ввести з клавіатури тризначне число та вивести суму цифр цього числа
# // %
# int() - так як input поверне str, нам потрібно цей рядок привести до типу int (ціле число)
# щоб можна було застосовувати арифметичні оператори
# input -> буде очікувати на введення даних з клавіатури в консолі і поверне за замовчуванням значення типу даних str
# number = int(input("Enter 3-digit number: "))
# # 146
# n1 = number // 100
# # v1
# # n2 = number // 10 % 10
# # v2
# n2 = number % 100 // 10
# n3 = number % 10
#
# result = n1 + n2 + n3
# # інтерполяція рядка - вбудовування змінних у рядок завдяки функції format (вивчимо докладніше пізніше)
# print(f"n1: {n1} n2: {n2} n3 {n3}")
# print(f"Result: {result}")

# number = 10
# print(number)

################
# number1 = input("Enter first number: ")
# number2 = input("Enter second number: ")
# result = number1 + number2  # конкатенація - складання рядків. Рядок + рядок -> один великий рядок
# print(result)
#
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# result = number1 + number2
# print(result)

