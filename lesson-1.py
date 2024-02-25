'''
1. Користувач вводить три цифри з клавіатури. Необхідно знайти суму чисел, добуток чисел.
Результат обчислень вивести на екран.

2. Напишіть програму, яка обчислює площу ромба. Користувач із клавіатури вводить довжину двох його діагоналей.
Площа ромба дорівнює половині добутку його діагоналей: S = (AC · BD)/2.

3. Користувач вводить з клавіатури число, що складається із чотирьох цифр. Потрібно знайти добуток цифр.
Наприклад, якщо з клавіатури введено 1324 тоді результат буде - 1*3*2*4 = 24.
'''

#1.
print("Введіть три цифри з клавіатури. Программа обчислить та виведе на екран суму чисел та добуток ввелених чисел.")
num1 = int(input("Введіть перше число:"))
num2 = int(input("Введіть друге число:"))
num3 = int(input("Введіть трерє число:"))
print(f"Сума: {num1 + num2 + num3}, Добуток: {num1 * num2 * num3}")

#1.
num1, num2, num3 = map(int, input("Введіть три числа через проб1іл: ").split())
print(f"Сума: {num1 + num2 + num3}, Добуток: {num1 * num2 * num3}")

#2.
print(f"Програма обчислює площу ромба. Площа ромба дорівнює половині добутку його діагоналей: S = (AC · BD)/2. Введіть з клавіатури довжину двох діагоналей ромба.")
diagonal1 = float(input("Введіть довжину першої діагоналі ромба: "))
diagonal2 = float(input("Введіть довжину другої діагоналі ромба: "))
area = (diagonal1 * diagonal2) / 2
print(f"Площа ромба: {area}")

#3.
number = input("Введіть чотирицифрове число: ")
product = 1
for digit in number:
    product *= int(digit)
print(f"Добуток цифр числа {number} дорівнює {product}")

#3.
print("Введіть з клавіатури число, що складається із чотирьох цифр. Программа знайде добуток цифр.")
number = int(input("Введіть чотирицифрове число: "))
num1 = number // 1000
num2 = number // 100 % 10
num3 = number // 10 % 10
num4 = number % 10
product = num1 * num2 * num3 * num4
print(f"Добуток цифр числа {number} дорівнює {product}")
