'''
У всіх завданнях використовувати обробку винятків
1. Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.
2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання
3. Користувач вводить два числа та матем дію: + - * або / Залежно від введеної матем дії вивести результат

Проект завантажити на гітхаб і надіслати посилання на public репозиторій (всі інші дз здавати так само)
'''

# 1.
print("Програма відобразить на екран назву введенного дня тижня.")
try:
    day = int(input("Вводіть із клавіатури номер дня тижня (1-7): "))
    match day:
        case 1:
            print("Це понеділок. It's Monday.")
        case 2:
            print("Це вівторок. It's Tuesday.")
        case 3:
            print("Це середа. It's Wednesday.")
        case 4:
            print("Це четвер. It's Thursday.")
        case 5:
            print("Це п'ятниця. It's Friday.")
        case 6:
            print("Це субота. It's Saturday.")
        case 7:
            print("Це неділя. It's Sunday.")
        case _:
            print("Некорректне введення. В тижні 7 днів.")

except Exception:
    print("Некорректне введення.")

# 2.
print("Потрібно ввести два числа. Програма визначить, чи рівні ці числа. Якщо ні, программа виведе їх на екран у порядку зростання")
try:
    number1 = float(input("Введіть перше число для порівняння: "))
    number2 = float(input("Введіть друге число для порівняння: "))
    if number1 == number2:
        print("Числа рівні.")
    else:
        print("Числа не рівні.")
        if number1 < number2:
            print(number1, number2)
        else:
            print(number2, number1)
except Exception:
    print("Некорректне введення.")
finally:
    print("The program completed.")

# 3.
print("Калькулятор")
print("Користувач вводить два числа та матем дію: + - * або / Залежно від введеної матем дії вивести результат")

class ExceptionAction(Exception):
  pass

try:
    number1 = float(input("Введіть перше число: "))
    number2 = float(input("Введіть друге число: "))
    action = input("Введіть дію (лише + - * або /): ")
    match action:
        case "+":
            result = number1 + number2
        case "-":
            result = number1 - number2
        case "*":
            result = number1 * number2
        case "/":
            result = number1 / number2
        case _:
            raise ExceptionAction("Некорректне введення. Немає такої математичної операції.")
    print(f"Результат: {result}")

except ExceptionAction as error:
    print(error)
except Exception:
    print("Некорректне введення.")
finally:
    print("The program completed.")
