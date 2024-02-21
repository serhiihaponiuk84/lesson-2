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

# 2.
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

# 3.
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

# 4.
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

# 5.
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