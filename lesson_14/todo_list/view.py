START_INDEX = 1


class MenuView:
    @staticmethod
    def display(options):
        print("Todo Application. Select your choice: ")
        for key, value in options.items():
            print("{}. {}".format(key, value))
        print("\n")


class AddItemView:
    @staticmethod
    def display(name):
        print("Item {} successfully added to list!".format(name))


class ModifyItemView:
    @staticmethod
    def display(index):
        print("Item {} successfully modified!".format(index + START_INDEX))


class DeleteItemView:
    @staticmethod
    def display(index):
        print("Item {} has been successfully deleted!".format(index + START_INDEX))


class MarkItemView:
    @staticmethod
    def display(index):
        print("Item {} successfully marked as done!".format(index + START_INDEX))


class DisplayListView:
    @staticmethod
    def display(items):
        if not items:
            print("List is empty!")
        else:
            for i in range(len(items)):
                print(items[i])


class DisplaySpecificItemView:
    @staticmethod
    def display(index, item):
        #  print(index + START_INDEX, item.deadline if item.deadline else '', item, ' -> ', item.description)
        print(f"{index + START_INDEX}. {item}")
