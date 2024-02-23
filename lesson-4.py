'''
1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран. (використовувати цикл)
2. Користувач вводить з клавіатури рядок та символ для пошуку. Порахуйте скільки разів у рядку зустрічається потрібний символ. Отримане число виведіть на екран.
3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни. Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.
4. Дано рядок. (зробити зрізи)
- Спершу виведіть третій символ цього рядка.
- У другому рядку виведіть передостанній символ цього рядка.
- У третьому рядку виведіть перші п'ять символів цього рядка.
- У четвертому рядку виведіть весь рядок, крім двох останніх символів.
- У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться з першого).
- У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
- У сьомому рядку виведіть усі символи у зворотному порядку.
- У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
- У дев'ятому рядку виведіть довжину цього рядка.

Додатково:
Є певний текст. Реалізуйте наступну функціональність:
■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;
■ Порахуйте скільки разів цифри зустрічаються у тексті;
■ Порахуйте скільки разів розділові знаки зустрічаються в тексті;
■ Порахуйте кількість знаків оклику в тексті.
'''

# 1.
print("Перше завдання.")
# Запитуємо у користувача рядок
print("Програма порахує кількість літер, цифр у введеному рядку та виведе обидві кількості на екран.")
text = input("Введіть рядок з клавіатури: ")

# Ініціалізація лічильників
letters = 0
digits = 0

# Перебираємо кожен символ в рядку
for char in text:
    if char.isalpha():  # Перевіряємо, чи є символ літерою
        letters += 1
    elif char.isdigit():  # Перевіряємо, чи є символ цифрою
        digits += 1

# Виводимо результати
print(f"Введено рядок: {text}")
print(f"Довжина рядка: {len(text)}")
print(f"Кількість літер: {letters}")
print(f"Кількість цифр: {digits}")
print()

# 2.
print("Друге завдання.")
print("Програма порахує скільки разів у введеному рядку зустрічається потрібний символ для пошуку. Отримане число буде відображено на екран.")

# Запитуємо у користувача рядок
text = input("Введіть рядок з клавіатури: ")

# Запитуємо символ для пошуку
search_char = input("Введіть з клавіатури символ для пошуку: ")

# Підрахунок кількості входжень символу в рядок
count = text.count(search_char)

# Виведення результату
print(f"Введено рядок: {text}")
print(f"Символ '{search_char}' зустрічається в рядку {count} разів.")
print()

# 3.
print("Третє завдання.")
print("Введіть з клавіатури рядок, слово для пошуку, слово для заміни.")
print("Програма зробить у рядку заміну одного слова на інше. Отриманий рядок відобразиться на екрані.")
print("Це приклад рядку: Це приклад тексту, де потрібно замінити слово.")
print("Це приклад слова для пошуку: слово")
print("Це приклад слова для заміни: вираз")

# Запитуємо у користувача
text = input("Введіть рядок: ")
search_word = input("Введіть слово для пошуку: ")
replace_word = input("Введіть слово для заміни: ")

# Виконуємо заміну
modified_text = text.replace(search_word, replace_word)

# Виводимо результат
print("Рядок до заміни:")
print(text)
print(f"Слово для пошуку: {search_word}")
print(f"Слово для заміни: {replace_word}")
print("Рядок після заміни:")
print(modified_text)
print()

# 4.
print("Четверте завдання.")
print("Програма робить зрізи по технічному завданню.")

# Припустимо, що рядок заданий наступним чином:
text = "Привіт, це демонстраційний рядок для прикладу."

print(text)
print("Третій символ рядка:", text[2])
print("Передостанній символ рядка:", text[-2])
print("Перші п'ять символів рядка:", text[:5])
print("Весь рядок, крім двох останніх символів:", text[:-2])
print("Символи з парними індексами:", text[::2])
print("Символи з непарними індексами:", text[1::2])
print("Символи у зворотному порядку:", text[::-1])
print("Символи через один у зворотному порядку, починаючи з останнього:", text[::-2])
print("Довжина рядка:", len(text))
print()

# 5.
print("П'яте завдання (додаткове).")
# Приклад тексту
text = "це приклад тексту. він містить цифри 12345. також він містить різні розділові знаки, включаючи крапки, коми та знаки оклику.!!"
print(f"Є певний текст: {text}")
# Аналіз тексту
# Зміна тексту так, щоб кожне речення починалося з великої літери
capitalized_text = '. '.join([sentence.strip().capitalize() for sentence in text.split('.')])

# Підрахунок кількості цифр у тексті
digits_count = sum(char.isdigit() for char in text)

# Підрахунок кількості розділових знаків у тексті (крапки, коми, двокрапки, крапки з комою, питальні та окличні знаки)
punctuation_marks = ',.?!:;'
punctuation_count = sum(char in punctuation_marks for char in text)

# Підрахунок кількості знаків оклику в тексті
exclamation_marks_count = text.count('!')

# Виведення результатів
print("Текст з великими літерами на початку кожного речення:")
print(capitalized_text)
print("Кількість цифр у тексті:", digits_count)
print("Кількість розділових знаків у тексті:", punctuation_count)
print("Кількість знаків оклику в тексті:", exclamation_marks_count)
print()

# 6.
print("Шосте завдання (додаткове).")
star = "* "
whitespaces = "  "
border = "- "

print("а)")
stars_count = 5
whitespaces_count = 0
border_count = 7
for i in range(border_count):
    if i == 0 or i == border_count - 1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(border, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            print(star, end="")
        print(border, end="")
        whitespaces_count += 1
        stars_count -= 1
    print()
print()

print("б)")
stars_count= 1
whitespaces_count = 4
border_count = 7
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(border, end="")
        for j in range(stars_count):
            print(star, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        print(border, end="")
        whitespaces_count -= 1
        stars_count += 1
    print()
print()

print("в)")
stars_count = 5
whitespaces_count = 0
border_count = 7
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(border, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            print(star, end="")
        if stars_count > 0:
            stars_count -= 2
            whitespaces_count += 1
        for j in range(whitespaces_count - 1):
            print(whitespaces, end="")
        print(border, end="")
    print()
print()

# производная из варианта "д"
print("г)")
stars_count = 5
whitespaces_count = 0
border_count = 7
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(border, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            if i < 3:
                print(whitespaces, end="")
            else:
                print(star, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        print(border, end="")
        if i < border_count // 2:
            stars_count -= 2
            whitespaces_count += 1
        else:
            stars_count += 2
            whitespaces_count -= 1
    print()
print()

# производная из варианта "д"
print("г)")
stars_count = 5
whitespaces_count = 0
border_count = 7
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(border, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            if i > 2:
                print(star, end="")
            else:
                print(whitespaces, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        print(border, end="")
        if i < border_count // 2:
            stars_count -= 2
            whitespaces_count += 1
        else:
            stars_count += 2
            whitespaces_count -= 1
    print()
print()

print("д)")
stars_count = 5
whitespaces_count = 0
border_count = 7
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(border, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            print(star, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        print(border, end="")
        if i < border_count // 2:
            stars_count -= 2
            whitespaces_count += 1
        else:
            stars_count += 2
            whitespaces_count -= 1
    print()
print()

print("е)")
stars_count = 1
whitespaces_count = 3
border_count = 7
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(border, end="")
        for j in range(stars_count):
            print(star, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            if j < (border_count // 2 - 1):
                print(star, end="")
        print(border, end="")
        if (i < border_count // 2):
            stars_count += 1
            whitespaces_count -= 2
        else:
            stars_count -= 1
            whitespaces_count += 2
    print()
print()

# производная из варианта "е"
print("ж)")
stars_count = 1
whitespaces_count = 3
border_count = 7
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(border, end="")
        for j in range(stars_count):
            print(star, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            if j < (border_count // 2 - 1):
                print(whitespaces, end="")
        print(border, end="")
        if (i < border_count // 2):
            stars_count += 1
            whitespaces_count -= 2
        else:
            stars_count -= 1
            whitespaces_count += 2
    print()
print()

# производная из варианта "е"
print("з)")
stars_count = 1
whitespaces_count = 3
border_count = 7
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(border, end="")
        for j in range(stars_count):
            if j < (border_count // 2 - 1):
                print(whitespaces, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
                print(star, end="")
        print(border, end="")
        if (i < border_count // 2):
            stars_count += 1
            whitespaces_count -= 2
        else:
            stars_count -= 1
            whitespaces_count += 2
    print()
print()

print("и)")
stars_count = 5
whitespaces_count = 0
border_count = 7
for i in range(border_count):
    if i == 0 or i == border_count - 1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(border, end="")
        for j in range(stars_count):
            print(star, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        print(border, end="")
        whitespaces_count += 1
        stars_count -= 1
    print()
print()

print("к)")
stars_count = 1
whitespaces_count = 4
border_count = 7
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(border, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            print(star, end="")
        print(border, end="")
        whitespaces_count -= 1
        stars_count += 1
    print()
print()