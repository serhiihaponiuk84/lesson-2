from todo_item import TodoItem

FILENAME = "todo_items.txt"


class Model:
    # def __init__(self):
    #     self.todo_items = []

    @staticmethod
    def add_item(name, description, deadline):
        todo_item = TodoItem(name, description, deadline)
        with open(FILENAME, 'a') as f:
            f.write(str(todo_item))

    def modify_item(self, index, name, description, deadline):
        all_items = self.get_items()
        all_items[index] = str(TodoItem(name, description, deadline))

        with open(FILENAME, 'w') as f:
            f.write("".join(all_items))

    def mark_as_done(self, index):
        # self.todo_items[index].mark_as_done()
        all_items = self.get_items()
        # можно распарсить (разобрать) строчку и сформировать экземпляр TodoItem или делаем как ниже
        current_task = all_items[index]
        all_items[index] = current_task[:1] + 'X' + current_task[2:]
        with open(FILENAME, 'w') as f:
            f.write("".join(all_items))

    def delete_item(self, index):
        all_items = self.get_items()
        all_items.pop(index)

        with open(FILENAME, 'w') as f:
            f.write("".join(all_items))

    @staticmethod
    def get_items():
        with open(FILENAME, 'r') as f:
            todo_items = f.readlines()
        return todo_items

    def get_specific_item(self, index):
        # result = self.get_items()
        # print(result)
        # print(f"selected item: {result[index]}")
        return self.get_items()[index]
