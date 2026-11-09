import json
from abc import ABC, abstractmethod
from pathlib import Path

database = Path(__file__).parent / "School_data.json"

data = {
    "Students": [],
    "Teacher": []
}

# Load existing data
if database.exists():
    with open(database, "r") as f:
        content = f.read()
        if content:
            data = json.loads(content)


# Save data to JSON file
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
        return "@" in email and "." in email


class Students(Person):

    def get_role(self):
        return "Student"

    def register(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        email = input("Enter your email: ")
        roll_no = input("Enter your roll number: ")

        if not Person.validate_email(email):
            print("Invalid email!")
            return

        for student in data["Students"]:
            if student["roll_no"] == roll_no:
                print(f"Student with roll number {roll_no} already exists.")
                return

        data["Students"].append({
            "name": name,
            "age": age,
            "email": email,
            "roll_no": roll_no,
            "grades": {}
        })

        save()
        print(f"Student {name} registered successfully!")

    def add_grade(self):
        roll_no = input("Enter student roll number: ")

        subject = input("Enter subject: ")
        marks = float(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        for student in data["Students"]:
            if student["roll_no"] == roll_no:
                student["grades"][subject] = marks
                save()
                print("Grade added successfully!")
                return

        print("Student not found!")

    def show_details(self):
        roll_no = input("Enter student roll number: ")

        for student in data["Students"]:
            if student["roll_no"] == roll_no:
                grades = student["grades"]

                average = (
                    sum(grades.values()) / len(grades)
                    if grades else 0
                )

                print("\n----- STUDENT DETAILS -----")
                print(f"Name       : {student['name']}")
                print(f"Age        : {student['age']}")
                print(f"Email      : {student['email']}")
                print(f"Roll Number: {student['roll_no']}")

                print("\nGrades:")
                if grades:
                    for subject, marks in grades.items():
                        print(f"{subject}: {marks}")
                else:
                    print("No grades added yet.")

                print(f"\nAverage Marks: {average:.2f}")
                return

        print("Student not found!")


class Teacher(Person):

    def get_role(self):
        return "Teacher"

    def register(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        email = input("Enter your email: ")
        emp_id = input("Enter your employee ID: ")

        if not Person.validate_email(email):
            print("Invalid email!")
            return

        for teacher in data["Teacher"]:
            if teacher["emp_id"] == emp_id:
                print(f"Teacher with employee ID {emp_id} already exists.")
                return

        data["Teacher"].append({
            "name": name,
            "age": age,
            "email": email,
            "emp_id": emp_id
        })

        save()
        print(f"Teacher {name} registered successfully!")

    def show_details(self):
        emp_id = input("Enter teacher employee ID: ")

        for teacher in data["Teacher"]:
            if teacher["emp_id"] == emp_id:
                print("\n----- TEACHER DETAILS -----")
                print(f"Name        : {teacher['name']}")
                print(f"Age         : {teacher['age']}")
                print(f"Email       : {teacher['email']}")
                print(f"Employee ID : {teacher['emp_id']}")
                return

        print("Teacher not found!")


# Create objects
stud = Students()
teach = Teacher()


# Main menu
while True:
    print("\n===== SCHOOL MANAGEMENT SYSTEM =====")
    print("1. Register a student")
    print("2. Register a teacher")
    print("3. Add student grades")
    print("4. Show student details")
    print("5. Show teacher details")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        stud.register()

    elif choice == 2:
        teach.register()

    elif choice == 3:
        stud.add_grade()

    elif choice == 4:
        stud.show_details()

    elif choice == 5:
        teach.show_details()

    elif choice == 6:
        print("Thank you for using the School Management System!")
        break

    else:
        print("Invalid choice. Please select 1-6.")
