import datetime
import os
import sys
import enum

from view import *
from model import Model

START_INDEX = 1


class MenuItems(enum.Enum):
    Add = '1'
    Modify = '2'
    Delete = '3'
    MarkItem = '4'
    DisplayItems = '5'
    DisplaySpecificItem = '6'
    Exit = '0'


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Controller:
    OPTIONS = {'1': 'Add Todo Item',
               '2': 'Modify Item',
               '3': 'Delete Item',
               '4': 'Mark Item',
               '5': 'Display Items',
               '6': 'Display Specific Item',
               '0': 'Exit program'}

    def __init__(self):
        self.model = Model()

    def menu(self):
        cls()
        self.show_menu()

        while True:
            option = input("Choose option: ")
            cls()
            self.show_menu()
            if option in self.OPTIONS.keys():
                if option == MenuItems.Add.value:
                    self.add_todo_item()
                elif option == MenuItems.Modify.value:
                    self.modify_item()
                elif option == MenuItems.Delete.value:
                    self.deleteItem()
                elif option == MenuItems.MarkItem.value:
                    self.mark_as_done()
                elif option == MenuItems.DisplayItems.value:
                    self.display_items()
                elif option == MenuItems.DisplaySpecificItem.value:
                    self.display_specific_item()
                elif option == MenuItems.Exit.value:
                    sys.exit()

    def show_menu(self):
        MenuView.display(self.OPTIONS)

    def add_todo_item(self):
        name = self.ask_name_input()
        description = self.ask_description_input()
        date = self.ask_date_input()
        self.model.add_item(name, description, date)
        AddItemView.display(name)

    def modify_item(self):
        index = self.ask_index_input()
        name = self.ask_name_input()
        description = self.ask_description_input()
        date = self.ask_date_input()
        try:
            self.model.modify_item(index, name, description, date)
            ModifyItemView.display(index)
        except IndexError:
            print("Wrong index!")

    def mark_as_done(self):
        index = self.ask_index_input()
        try:
            self.model.mark_as_done(index)
            MarkItemView.display(index)
        except IndexError:
            print("Wrong index!")

    def deleteItem(self):
        index = self.ask_index_input()
        try:
            self.model.delete_item(index)
            DeleteItemView.display(index)
        except IndexError:
            print("Wrong index!")

    def display_items(self):
        DisplayListView.display(self.model.get_items())

    def display_specific_item(self):
        index = self.ask_index_input()
        try:
            item = self.model.get_specific_item(index)
            DisplaySpecificItemView.display(index, item)
        except IndexError:
            print("Wrong index!")

    @staticmethod
    def ask_index_input():
        while True:
            try:
                index = int(input("Enter index of item: "))
                return index - START_INDEX
            except ValueError:
                print("You need to enter a number!")

    @staticmethod
    def ask_name_input():
        while True:
            return input("Enter item name: ").strip()

    @staticmethod
    def ask_description_input():
        while True:
            return input("Enter item description: ").strip()

    @staticmethod
    def ask_date_input():
        year_index = 0
        month_index = 1
        day_index = 2
        while True:
            try:
                date = input("Enter date: yyyy/mm/dd ")
                if not date:
                    return None
                date = date.split("/")
                deadline = datetime.date(int(date[year_index]), int(date[month_index]), int(date[day_index]))
                return deadline
            except:
                print("Wrong input!")
