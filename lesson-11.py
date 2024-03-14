"""
1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова, що
складаються не менше ніж з семи літер.
2. Даний текстовий файл. Підрахувати кількість слів у ньому.
3. Створіть програму, яка перевіряє текст на неприпустимі слова.
Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
За підсумками роботи програми необхідно показати статистику дій.
Наприклад, якщо й у нас є такий текст:
To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of
outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more;
and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep
Неприпустиме слово: die.
Результат:
To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of
outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To ***: to sleep; No more;
and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To ***, to sleep.
Статистика: 2 заміни слова die.
Нотатка:
Текст для всіх завдань можна написати самостійно або взяти з Інтернету.
Логіка має працювати з будь-яким текстом.
"""

# 1.
# Спершу, створимо приклад текстового файлу для демонстрації.
example_text = """To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more;
and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to,
'tis a consummation Devoutly to be wish'd. To die, to sleep
"""
input_file_path = "example_file.txt"
output_file_path = "long_words_file.txt"
censored_file_path = "censored_file.txt"

# Записуємо приклад тексту в файл
with open(input_file_path, "w", encoding="utf-8") as file:
    file.write(example_text)

# Функція для копіювання слів з першого файлу в другий за умовою
def copy_words(input_file_path, output_file_path):
    with open(input_file_path, "r", encoding="utf-8") as input_file, \
         open(output_file_path, "w", encoding="utf-8") as output_file:
        for line in input_file:
            words = line.split()
            long_words = [word for word in words if len(word) >= 7]
            output_file.write(" ".join(long_words) + "\n")


# Викликаємо функцію для створення нового файлу з довгими словами
copy_words(input_file_path, output_file_path)

# Функція для виводу контенту з файлу
def print_file_content(input_file_path):
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            print(line, end="")


print(f"Вміст файла {input_file_path}:")
print_file_content(input_file_path)
print()
print(f"Вміст файла {output_file_path}:")
print_file_content(output_file_path)
print()


# 2.
# Функція для підрахунку кількості слів у файлу.
def count_words(file_path) -> int:
    count = 0
    with open(file_path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            words = line.split()
            count += len(words)
    return  count


print(f"Кількість слів у файлі {input_file_path} дорівнює {count_words(input_file_path)}")
print(f"Кількість слів у файлі {output_file_path} дорівнює {count_words(output_file_path)}")
print()

# 3.
def censor_text(input_file_path, output_file_path, forbidden_words:list) -> int:
    """
    Замінює неприпустимі слова в тексті на набір символів * і виводить статистику.
    :param file: текст для перевірки
    :param forbidden_words: список неприпустимих слів
    :return: модифікований текст і статистика
    """
    replaced_count = 0
    with open(input_file_path, "r", encoding="utf-8") as input_file, \
         open(output_file_path, "w", encoding="utf-8") as output_file:
        for line in input_file:
            for word in forbidden_words:
                if word in line:
                    replaced_count += 1
                    line = line.replace(word, '*' * len(word))
            output_file.write("".join(line))
    return replaced_count


forbidden_words = input("Введіть неприпустимі слова через пробіл: ").split()
replaced_count = censor_text(input_file_path, censored_file_path, forbidden_words)
print(f"Текст після цензури:")
print_file_content(censored_file_path)
print(f"Загальна кількість замінених слів: {replaced_count}")