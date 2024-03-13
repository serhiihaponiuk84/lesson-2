# ^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!*@#$%^&+=]).*$
# ^[0-9a-zA-Z]+[._]?[0-9a-zA-Z]+[@][a-zA-Z0-9]+[.][a-zA-Z]{2,}$
# t_e@s.com
# ^[+]?[380][0-9]{7}$
# "^[a-zA-ZА-Яа-яёЁЇїІіЄєҐґ]+$"

###
# r (Read). Файл відкривається для читання. Якщо файл не знайдено, то генерується виняток FileNotFoundError
#
# w (Write). Файл відкривається для запису. Якщо файл відсутній, він створюється. Якщо такий файл вже є,
# то він створюється заново, і відповідно старі дані в ньому стираються.
#
# a (Append). Файл відкривається для запису. Якщо файл відсутній, він створюється.
# Якщо подібний файл вже є, дані записуються в його кінець.
#
# b (Binary). Використовується для роботи з бінарними файлами. Застосовується разом з іншими режимами – w або r.

# # v1
# try:
#     my_file = open("hello.txt", "w")
#     try:
#         my_file.write("hello world")
#     except Exception as e:
#         print(e)
#     finally:
#         my_file.close()
# except Exception as e:
#     print(e)
#
# # v2
# with open("hello_1.txt", "w") as test_file:
#     test_file.write("one")
#
#
# with open("hello_1.txt", "a") as test_file:
#     test_file.write("two\nthree\n")

#
# with open("hello.txt", "r", encoding="utf-8") as myfile:
#     # v1
#     # result = myfile.read()
#     # print(result)
#     # v2
#     # result = myfile.readline()
#     # print(result)
#     # result = myfile.readline(3)
#     # print(result)
#     # v3
#     # result = myfile.readlines()
#     # print(result)
#     # v4
#     # for line in myfile:
#     #     print(line, end="")
#     # v5
#     line = myfile.readline()
#     while line:
#         print(line, end="")
#         line = myfile.readline()

# ###
# FILENAME = "notes.txt"
# NOTES_COUNT = 3
#
# notes = []
#
# for i in range(NOTES_COUNT):
#     notes.append(input(f"Enter note: {i + 1}: ").strip())
#
# with open(FILENAME, "a") as file:
#     for i in range(NOTES_COUNT):
#         file.write(f"{i + 1}. {notes[i]}\n")
#
# with open(FILENAME, "r") as file:
#     print(file.read())

###
# import pickle
# FILENAME = "notes.dat"
#
# users = [
#     ["John", "123456789"],
#     ["Peter", "987654321"],
#     ["Vasya", "1568654156"]
# ]
#
# with open(FILENAME, "wb") as file:
#     pickle.dump(users, file)  # серіалізація
#
# with open(FILENAME, "rb") as file:
#     users_from_file = pickle.load(file)  # десеріалізація
#     for user in users_from_file:
#         print(f"Name: {user[0]} Phone: {user[1]}")

#
# import shelve
#
# FILENAME = "notes"
#
# with shelve.open(FILENAME) as users:
#     users["John"] = "123456789"
#     users["Peter"] = "987654321"
#     users["Vasya"] = "1568654156"
#
# with shelve.open(FILENAME) as users:
#     users["Petya"] = "12312341234123"
#     print(users["Petya"])
#     print(users["John"])
#
#     for key in users:
#         print(f"{key} - {users[key]}")
#
#     print(users)
#     users.pop("John", "not found")
#
#     print("-" * 10)
#
#     for key in users:
#         print(f"{key} - {users[key]}")

###
##
# import os
#
# # os.mkdir("test_folder")
#
# # os.rmdir("test_folder")
# #
# file_name = "notes.bak"
# if os.path.exists(file_name):
#     os.remove(file_name)
#     print("File removed!")
# else:
#     print("File not found!")

# доп: написати скрипт для видалення всіх файлів вказаної директорії
#
# # відносний шлях - щодо поточної директорії (папки, де знаходиться вихідник, який ви запустили)
# with open("f1/f2/test.txt", "w") as myfile:
#     myfile.write("hello world")
# # #
# with open("../../test1.txt", "w") as myfile:
#     myfile.write("hello world")
# абсолютний шлях - повний шлях починаючи з диска C://test_folder/...

###
# import csv
#
# FILENAME = "users.csv"

# v1
# users = [
#     ["John", "123456789"],
#     ["Peter", "987654321"],
#     ["Vasya", "1568654156"]
# ]
#
# with open(FILENAME, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)
#
# with open(FILENAME, "a", newline="") as file:
#     user = ["Anton", "87347864"]
#     writer = csv.writer(file)
#     writer.writerow(user)
#
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(f"{row[0]} - {row[1]}")

# v2
# users = [
#     {"name": "John", "phone": "111"},
#     {"name": "Petya", "phone": "222"},
#     {"name": "Vasya", "phone": "333"},
# ]
#
# with open(FILENAME, "w", newline="") as file:
#     columns = ["name", "phone"]
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#
#     # all users
#     writer.writerows(users)
#
#     # one user
#     user: dict = {"name": "Test", "phone": "555"}
#     writer.writerow(user)
#
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['name'], " - ", row['phone'])

####
# создать телефонную книгу с сохранением в файл txt
# добавление
# изменение контакта
# удаление
# поиск по имени

import os
import sys

CONTACTS_FILE_PATH = "contacts.txt"


def get_contacts(path_to_file: str) -> str:
    if os.path.exists(path_to_file):
        with open(path_to_file, "r", encoding="utf-8") as file:
            # v1
            # content: list[str] = file.readlines()
            # result: str = ""
            # for i in range(len(content)):
            #     result += str(i + 1) + " " + content[i]
            # v2
            result: str = ""
            current_contact_number: int = 1
            for contact in file:
                result += str(current_contact_number) + " " + contact
                current_contact_number += 1
        return result
    raise FileNotFoundError(f"File {path_to_file} not found!")


def add_contact(path_to_file: str, contact: dict) -> None:
    with open(path_to_file, "a", encoding="utf-8") as file:
        file.write(contact.get("name") + " - " + contact.get("phone") + "\n")


def modify_contact(path_to_file: str, updated_contact: dict, contact_phone_to_update: str) -> None:
    with open(path_to_file, "r", encoding="utf-8") as file:
        is_contact_found: bool = False
        contacts = file.readlines()
        for i in range(len(contacts)):
            if contacts[i].find(contact_phone_to_update) != -1:
                contacts[i] = updated_contact.get("name") + " - " + updated_contact.get("phone") + "\n"
                is_contact_found = True
                break

    if is_contact_found:
        with open(path_to_file, "w", encoding="utf-8") as file:
            file.write("".join(contacts))
        return

    raise Exception(f"Contact {contact_phone_to_update} not found!")


def delete_contact(path_to_file: str, contact_phone_to_delete: str) -> None:
    with open(path_to_file, "r", encoding="utf-8") as file:
        is_contact_found: bool = False
        contacts = file.readlines()
        for i in range(len(contacts)):
            if contacts[i].find(contact_phone_to_delete) != -1:
                contacts.pop(i)
                is_contact_found = True
                break

    if is_contact_found:
        with open(path_to_file, "w", encoding="utf-8") as file:
            file.write("".join(contacts))
        return

    raise Exception(f"Contact {contact_phone_to_delete} not found!")


try:
    user_select = int(input(f"\n1. Add contact\n2. Modify contact\n3. Delete contact\n4. Get contacts\n5. Exit\n"))
    match user_select:
        case 1:
            add_contact(CONTACTS_FILE_PATH, {"name": "Vasya", "phone": "555-555-5555"})
        case 2:
            modify_contact(CONTACTS_FILE_PATH, {"name": "Petya", "phone": "555-555-5555"}, "555-555-5555")
        case 3:
            delete_contact(CONTACTS_FILE_PATH, "555-555-5555")
        case 4:
            print(get_contacts(CONTACTS_FILE_PATH))
        case 5:
            sys.exit()
        case _:
            raise Exception(f"Incorrect input: {user_select}")
except Exception as error:
    print(error)
