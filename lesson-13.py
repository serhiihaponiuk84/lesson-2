"""
Створити ієрархію класів для опису академії.
Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
Продумати архітектуру: реалізувати принципи ООП
"""
import random

MIN_AGE = 15
MAX_AGE = 99
MIN_LENGTH_NAME = 5
MAX_LENGTH_NAME = 30

class Person:
    __name: str = "no name"
    __age: int = 0

    def __init__(self, name:str=None, age:int=None):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name=None):
        if MIN_LENGTH_NAME < len(name) < MAX_LENGTH_NAME:
            self.__name = name
        else:
            print("Incorrect name length!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age:int):
        if MIN_AGE < age < MAX_AGE:
            self.__age = age
        else:
            print("Incorrect age!")

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")


class Teacher(Person):
    def __init__(self, name:str=None, age:int=None):
        super().__init__(name, age)
        self._subject = None

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject=None):
        self._subject = subject

    def display_info(self):
        super().display_info()
        print(f"Teaches: {self.subject.name}")


class Student(Person):
    def __init__(self, name=None, age=None, student_id=None, group=None):
        super().__init__(name, age)
        self.student_id = student_id
        self.group = group
        group.add_student(self)

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Group: {self.group.group_name if self.group else 'No group assigned'}")


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.teacher.subject = self

    def display_info(self):
        print(f"Subject: {self.name}, Taught by: {self.teacher.name}")

class Group:
    def __init__(self, group_name):
        self.students = []
        self._group_name = group_name

    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, group_name=None):
        self._group_name = group_name

    def add_student(self, student):
        self.students.append(student)

    def display_info(self):
        print(f"Group Name: {self._group_name}."
              f"Students:")
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Student ID: {student.student_id}")


class Academy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []
        self.groups = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_group(self, group):
        self.groups.append(group)

    def display_info(self):
        print(f"Academy: {self.name}\n")
        self.display_group("Teachers:", self.teachers)
        self.display_group("Groups:", self.groups)
        self.display_group("Students:", self.students)
        self.display_group("Subjects:", self.subjects)

    def display_group(self, title, group):
        print(title)
        for item in group:
            item.display_info()
        print()

# Example
teachers_data = [
    ("John Doe", 35),
    ("Jane Smith", 31),
    ("Emily Johnson", 29),
    ("Michael Brown", 22),
    ("Sarah Wilson", 27),
    ("David Miller", 31),
    ("Elizabeth Davis", 39),
    ("James Taylor", 25),
    ("Jessica White", 22),
    ("Christopher Harris", 19),
]

students_data = [
    ("Daniel Roberts", 20, "STDNT12345"),
    ("Laura Thompson", 19, "STDNT12346"),
    ("Brian Walker", 21, "STDNT12347"),
    ("Megan Anderson", 18, "STDNT12348"),
    ("Anthony Clark", 22, "STDNT12349"),
    ("Sophia Martinez", 20, "STDNT12350"),
    ("Alexander Lewis", 21, "STDNT12351"),
    ("Olivia Allen", 19, "STDNT12352"),
    ("Ethan Young", 21, "STDNT12353"),
    ("Chloe King", 20, "STDNT12354"),
]

subjects_names = [
    "Mathematics",
    "Biology",
    "Chemistry",
    "Physics",
    "History",
    "English Literature",
    "Computer Science",
    "Geography",
    "Physical Education",
    "Art and Design",
]

academy = Academy("Elite Academy")

group_1 = Group("Software Engineering A101")
group_2 = Group("Cyber Security A102")

academy.add_group(group_1)
academy.add_group(group_2)

for name, age in teachers_data:
    teacher = Teacher(name, age)
    academy.add_teacher(teacher)

for name, age, student_id in students_data:
    if random.choice([True, False]):
        student = Student(name, age, student_id, group_1)
    else:
        student = Student(name, age, student_id, group_2)
    academy.add_student(student)

for subject_name, teacher in zip(subjects_names, academy.teachers):
    subject = Subject(subject_name, teacher)
    academy.add_subject(subject)

academy.display_info()