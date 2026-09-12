def show_menu():
    print("\n" + "=" * 30)
    print("          GRADE TRACKER")
    print("=" * 30)
    print("1. View grades")
    print("2. Add a grade")
    print("3. Calculate average")
    print("4. Exit")


def view_grades(grades):
    if not grades:
        print("\nNo grades recorded yet.")
    else:
        print("\n--- YOUR GRADES ---")
        for index, grade in enumerate(grades, start=1):
            print(f"{index}. {grade}")


def add_grade(grades):
    try:
        new_grade = float(input("\nEnter the grade (0-100): "))
        if 0 <= new_grade <= 100:
            grades.append(new_grade)
            print(f"Grade {new_grade} added successfully!")
        else:
            print("Please enter a valid grade between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")


def calculate_average(grades):
    if not grades:
        print("\nNo grades available to calculate an average.")
    else:
        # sum() adds up all numbers in the list, len() counts how many items there are
        avg = sum(grades) / len(grades)
        print(f"\nAverage Grade: {avg:.2f}")


def main():
    grades = []
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            view_grades(grades)
        elif choice == "2":
            add_grade(grades)
        elif choice == "3":
            calculate_average(grades)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()
