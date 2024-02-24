"""
Завдання:

множини, списки, рядки:
1. Створити список чисел. Заберіть дублікати значень. Вивести унікальні значення.
2. Дано два списки чисел.
Порахуйте, скільки унiкальних чисел міститься як у першому списку, і у другому.
3. Даний текст: у першому рядку записано число рядків, далі йдуть самі рядки.
Визначте, скільки унiкальних слів міститься у цьому тексті.
Словом вважається послідовність непробільних символів, що йдуть поспіль, слова розділені одним або більшим числом пробілів або символами кінця рядка.

словники:
1. Наведено список країн і міст кожної країни. Для кожного міста вкажіть, в якій країні воно знаходиться.
Приклад результату:
{
"Ukraine": ["Kyiv", "Lviv", "Dnipro"],
"USA": ["Los Angeles", "Las Vegas"]
}
2. Дано два списки однакової довжини. Необхідно створити з них словник таким чином, щоб елементи першого списку були ключами, а елементи другого відповідно значеннями нашого словника.
"""
import random

# 1.
print("Перше завдання.")
ARRAY_NUMBERS = 10
# Генерація списку випадкових чисел
numbers = [random.randint(-5, 5) for _ in range(ARRAY_NUMBERS)]
print("Список чисел:", numbers)
print("Програма прибере дублікати значень в списку та виведе на екран унікальні значення.")
unique_numbers = []
for number in numbers:
    if numbers.count(number) == 1:
        unique_numbers.append(number)
print("Унікальні значення зі списку: ", unique_numbers)
print()

# 2.
print("Друге завдання.")
ARRAY_NUMBERS = 10
# Генерація списку випадкових чисел
numbers_1 = [random.randint(-5, 5) for _ in range(ARRAY_NUMBERS)]
numbers_2 = [random.randint(-5, 5) for _ in range(ARRAY_NUMBERS)]
print("Дано два списки чисел.")
print("Список чисел № 1:", numbers_1)
print("Список чисел № 2:", numbers_2)
print("Програма порахує кількість унiкальних чисел, котра міститься як у першому списку, так у другому.")
print("Унікальні значення зі списку № 1:", list(set(numbers_1)))
print("Унікальні значення зі списку № 2:", list(set(numbers_2)))
# спеціально нижче використав обидва методи ^ та symmetric_difference()
print("Унікальні значення з обох списків:", list(set(numbers_1) ^ set(numbers_2)))
print("Кількість Унікальних значень з обох списків:", len(set(numbers_1).symmetric_difference(set(numbers_2))))
print()

# 3.
print("Третє завдання.")
# Припустимо, ми маємо наступний текстовий ввід (для прикладу, використаємо мультисрічковий рядок)
text = """4
Це приклад тексту що містить кілька унікальних слів
Деякі слова повторюються слова
Унікальність слів визначається без урахування регістру
це дозволяє врахувати слова та Слова як одне слово"""
print(text)

# Розділимо текст на рядки
lines = text.split('\n')

unique_words = set()

for line in lines[1:]:
    # Додамо кожне слово в множину, перетворивши його на нижній регістр для ігнорування регістру
    unique_words.update(word.lower() for word in line.split())

print("Унікальні слова: ", unique_words)
print("Кількість Унікальних слів у тексті: ", len(unique_words))
print()

# 4.
print("Четверте завдання.")
print("Наведено список країн і міст кожної країни.")
cities_in_countries = {
    "Україна"   : ["Київ", "Львів", "Одеса"],
    "Франція"   : ["Париж", "Марсель", "Ліон"],
    "Італія"    : ["Рим", "Мілан", "Венеція"],
    "Іспанія"   : ["Мадрид", "Барселона", "Валенсія"],
    "Німеччина" : ["Берлін", "Мюнхен", "Гамбург"],
    "США"       : ["Нью-Йорк", "Лос-Анджелес", "Чикаго"],
    "Канада"    : ["Торонто", "Ванкувер", "Монреаль"],
    "Австралія" : ["Сідней", "Мельбурн", "Брісбен"],
    "Японія"    : ["Токіо", "Осака", "Кіото"],
    "Китай"     : ["Пекін", "Шанхай", "Гуанчжоу"]
}
for country, cities in cities_in_countries.items():
    print(f"{country}: {cities}")
print("Програма для кожного міста вкаже, в якій країні воно знаходиться.")
for country, cities in cities_in_countries.items():
    for city in cities:
        print(f"{city}: {country}")
print()

# 5.
print("П'яте завдання.")
print("Дано два списки однакової довжини.")
list_1 = ["Ім'я", "Dік", "Місто", "Професія"]
list_2 = ['Олександр', 28, 'Київ', 'розробник']
print(f"Перший спысок : {list_1}")
print(f"Другий спысок : {list_2}")
print("Програма створить з наведених списків словник таким чином, щоб елементи першого списку були ключами, а елементи другого відповідно значеннями нашого словника.")
student = {}
if len(list_1) == len(list_2):
    for i in range(len(list_1)):
        student[list_1[i]] = list_2[i]
print(f"Результат : {student}")
