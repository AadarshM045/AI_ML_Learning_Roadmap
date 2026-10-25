import json
from abc import ABC, abstractmethod
from pathlib import Path

database = Path(__file__).parent / "School_data.json"
data = {
    "Students": [],
    "Teacher": []
}

if database.exists():
    with open(database, "r") as f:
        content = f.read()
        if content:
            data = json.loads(content)


def save():
    with open(database, "w") as f:
        json.dump(data, f, indent=4)


class Person(ABC):

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False


class Students(Person):

    def show_details(self):
        pass

    def get_role(self):
        return "Students"

    def register(self):
        name = input("Enter Your name: ")
        age = int(input("Enter your age: "))
        email = input("tell your mail :- ")
        roll_no = int(input("tell your roll number :- "))

        if not Person.validate_email(email):
            print("Invalid Email")
            return

        for i in data["Students"]:
            if i["roll_no"] == roll_no:
                print(f"Students with Roll Number {roll_no} already exists")
                return

        data["Students"].append({
            "name": name,
            "age": age,
            "email": email,
            "roll_no": roll_no,
            "grades": {}
        })
        save()
        print(f"Students {name} registred!!")

    def add_grade(self):
        roll_no = int(input("Enter your Roll Number: "))
        Subject = input("Enter the Subjects: ")
        Marks = float(input("Enter Your mark: "))
        for i in data["Students"]:
            if i["roll_no"] == roll_no:
                i["grades"][Subject] = Marks
                save()
                return
        print("Student Not found!!")


class Teacher(Person):

    def show_details(self):
        pass

    def get_role(self):
        return "Teacher"

    def register(self):
        name = input("Enter Your name: ")
        age = int(input("Enter your age: "))
        email = input("tell your mail :- ")
        emp_id = input("tell your employee id number :- ")

        if not Person.validate_email(email):
            print("Invalid Email")
            return

        for i in data["Teacher"]:
            if i["emp_id"] == emp_id:
                print(f"Teacher with Employee Id {emp_id} already exists")
                return

        data["Teacher"].append({
            "name": name,
            "age": age,
            "email": email,
            "emp_id": emp_id,
        })

        save()

        print(f"Teacher {name} registred!!")


print("Press 1 for Regeister as a Student")
print("Press 2 for Regeister as a Teacher")
print("Press 3 to add grades")
print("Press 4 to show Student details")
print("Press 5 to show Teacher details")

choice = int(input("Enter your Choice: "))

Stud = Students()
teach = Teacher()
if choice == 1:
    Stud.register()
if choice == 2:
    teach.register()
if choice == 3:
    Stud.add_grade()
