def show_menu():
    print("\n" + "=" * 30)
    print("      SHOPPING LIST MANAGER")
    print("=" * 30)
    print("1. View shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear entire list")
    print("5. Exit")


def view_list(shopping_list):
    if not shopping_list:
        print("\nYour shopping list is empty.")
    else:
        print("\n--- YOUR SHOPPING LIST ---")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")


def add_item(shopping_list):
    item = input("\nEnter the item to add: ").strip().capitalize()
    if item:
        # Check if the item is already in the list using the 'in' operator
        if item in shopping_list:
            print(f"'{item}' is already on your shopping list!")
        else:
            shopping_list.append(item)
            print(f"'{item}' added to the list.")
    else:
        print("Item name cannot be empty.")


def remove_item(shopping_list):
    if not shopping_list:
        print("\nYour list is empty, nothing to remove.")
    else:
        view_list(shopping_list)
        try:
            number = int(input("\nEnter the number of the item to remove: "))
            if 1 <= number <= len(shopping_list):
                removed = shopping_list.pop(number - 1)
                print(f"'{removed}' removed from the list.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")


def clear_list(shopping_list):
    if not shopping_list:
        print("\nYour list is already empty.")
    else:
        shopping_list.clear()
        print("\nShopping list cleared successfully!")


def main():
    shopping_list = []
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            view_list(shopping_list)
        elif choice == "2":
            add_item(shopping_list)
        elif choice == "3":
            remove_item(shopping_list)
        elif choice == "4":
            clear_list(shopping_list)
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()
