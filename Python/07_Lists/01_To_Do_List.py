def show_menu():
    print("\n" + "=" * 30)
    print("          TO-DO LIST")
    print("=" * 30)
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")


def view_tasks(tasks):
    if not tasks:
        print("You have not added any tasks.")
    else:
        print("\n--- YOUR TASKS ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def add_task(tasks):

    new_task = input("Enter the task you want to add: ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"'{new_task}' is added successfully!")
    else:
        print("Task cannot be empty.")


def remove_task(tasks):
    if not tasks:
        print("You have not added any tasks to remove.")
    else:
        view_tasks(tasks)

        try:
            number = int(input("\nEnter the number of the task to remove: "))

            if 1 <= number <= len(tasks):
                removed_task = tasks.pop(number - 1)
                # Use 'removed_task' instead of looking up the popped index
                print(f"'{removed_task}' is removed!")
            else:
                print(
                    f"Invalid number. Please choose between 1 and {len(tasks)}.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = []
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()
