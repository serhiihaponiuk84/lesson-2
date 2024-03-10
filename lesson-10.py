"""
Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
- домашній номер телефону (тільки цифри та довжина номера)
- Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
- email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
- ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
додатково:
- Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ, довжина пароля – від 8 до 16 символів)
"""

import re
import random
import string

MIN_SIZE_PASSWORD = 8
MAX_SIZE_PASSWORD = 16

def generate_password(length:int=MIN_SIZE_PASSWORD) -> str:
    """
    Генерує пароль, який відповідає наступним вимогам:
    - мінімум одна велика літера
    - мінімум одна маленька літера
    - мінімум одна цифра
    - мінімум один символ
    - загальна довжина пароля - від 8 до 16 символів (за замовчуванням 8)
    """
    if not (MIN_SIZE_PASSWORD <= length <= MAX_SIZE_PASSWORD):
        raise ValueError(f"Довжина пароля повинна бути від {MIN_SIZE_PASSWORD} до {MAX_SIZE_PASSWORD} символів")

    # Визначаємо набори символів
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "@$!%*?&"

    # Гарантуємо наявність хоча б одного символу з кожного набору
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Додаємо випадкові символи для досягнення бажаної довжини пароля
    all_chars = lower + upper + digits + symbols
    password += [random.choice(all_chars) for _ in range(length - 4)]

    # Перемішуємо символи, щоб уникнути передбачуваності
    random.shuffle(password)

    # Повертаємо пароль як рядок
    return ''.join(password)


def validation(pattern:str, expression:str) -> bool:
    return bool(re.match(pattern, expression))
    # Повертає True, якщо вираз відповідає шаблону, інакше - False


# 1.
expression = ""
pattern = r"^\d{5,7}$"
print("1. Home phone number can be from 5 to 7 digits long.")
while not validation(pattern, expression):
    expression = input("Enter your home phone number to verify: ")
    if not validation(pattern, expression):
        print("Validation Error. Please try again.")
    else:
        print(f"Validation OK. Number {expression} is valid. It looks like your home phone.")
print()

# 2.
pattern = r"^\+?\d{1,3}\s?\d{1,5}\s?\d{5,8}$"
"""
Код країни в міжнародних номерах зазвичай складається з 1 до 3 цифр. Довжина коду країни залежить від конкретної
країни і може змінюватись.
Код оператора мобільного зв'язку або міста у телефонних номерах може складатися з різної кількості цифр, залежно
від країни та конкретної телефонної системи. Загалом, для мобільних операторів та міських телефонних систем кількість
цифр у коді може змінюватись від 1 до 5.
Локальний номер телефону без урахування коду країни та коду оператора або міста зазвичай складається з 5 до 8 цифр,
залежно від країни та конкретної телефонної системи.
"""
print("2. Mobile phone number can be from 10 to 12 digits long and may optionally contain + at the beginning"
      " or spaces after the country code and operator code.")
expression = ""
while not validation(pattern, expression):
    expression = input("Enter your mobile phone number to verify: ")
    if not validation(pattern, expression):
        print("Validation Error. Please try again.")
    else:
        print(f"Validation OK. Number {expression} is valid. It looks like your mobile phone.")
print()

# 3.
expression = ""
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# Цей патерн розбивається на такі частини:
# ^[a-zA-Z0-9._%+-]+ - початок рядка повинен містити один або більше символів, які можуть бути літерами (a-z, A-Z),
# цифрами (0-9), точками (.), підкресленнями ( _), відсотками (%), плюсами (+) чи мінусами (-).
# @ - символ собаки, що розділяє ім'я користувача та домен поштового сервісу.
# [a-zA-Z0-9.-]+ - доменне ім'я, що складається з літер, цифр, точок або дефісів.
# \. - точка, що відокремлює доменне ім'я від доменного суфікса.
# """[a-zA-Z]{2,} - доменний суфікс, що складається з двох або більше букв (наприклад, "com", "org", "net").
# Це базовий патерн і він підходить для більшості звичайних адрес електронної пошти, проте варто зауважити, що існують
# специфічні випадки адрес, які можуть не задовольняти цей вираз через особливі символи або нові доменні зони.
print("3. Example for e-mail address : press@google.com")
while not validation(pattern, expression):
    expression = input("Enter your e-mail adress to verify: ")
    if not validation(pattern, expression):
        print("Validation Error. Please try again.")
    else:
        print(f"Validation OK. Expression {expression} is valid. It looks like e-mail adress.")
print()

# 4.
expression = ""
pattern = r"^([A-Za-zА-Яа-яҐЄІЇґєії]{2,20}\s){2}[A-Za-zА-Яа-яҐЄІЇґєії]{2,20}$"
print("4. Last name, first name and patronymic of the client (3 words, minimum 2 char, maximum 20 char).")
while not validation(pattern, expression):
    expression = input("Enter last name, first name and patronymic of the client to verify: ")
    if not validation(pattern, expression):
        print("Validation Error. Please try again.")
    else:
        print(f"Validation OK. Expression {expression} is valid. It looks like last name, first name and patronymic of the client.")
print()

# 5.
expression = ""
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$"
# Розшифровка компонентів цього виразу:
#^ і $ - позначають початок і кінець рядка відповідно, що гарантує перевірку всього рядка.
#(?=.*[a-z]) - позитивна попередня перевірка, щоб забезпечити наявність хоча б однієї маленької літери.
#(?=.*[A-Z]) - позитивна попередня перевірка, щоб забезпечити наявність хоча б однієї великої літери.
#(?=.*\d) - позитивна попередня перевірка, щоб забезпечити наявність хоча б однієї цифри.
#(?=.*[@$!%*?&]) - позитивна попередня перевірка, щоб забезпечити наявність хоча б одного символу з вказаного набору.
# [A-Za-z\d@$!%*?&]{8,16} - вказує на те, що дозволені літери (великі та маленькі), цифри та символи з вказаного набору,
#а довжина рядка має бути від 8 до 16 символів.
#Цей регулярний вираз гарантує, що пароль буде відповідати всім вказаним вимогам: міститиме велику та маленьку літери,
#цифру, спеціальний символ і матиме довжину від 8 до 16 символів.
print(f"5. Password (minimum: one capital letter, one small letter, one number, one symbol, password length -"
      f" from {MIN_SIZE_PASSWORD} to {MAX_SIZE_PASSWORD} characters). Example for password:"
      f" {generate_password()}")
while not validation(pattern, expression):
    expression = input("Enter your home password to verify: ")
    if MIN_SIZE_PASSWORD <= len(expression) <= MAX_SIZE_PASSWORD:
        if not validation(pattern, expression):
            print("Validation Error. Please try again.")
        else:
            print(f"Validation OK. Expression {expression} is valid. It looks like your password.")
    else:
        print("Validation Error. Please try again.")
print()
