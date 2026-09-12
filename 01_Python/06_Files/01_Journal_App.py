import datetime as dt


def add_entry():

    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    thought = input("\nWhat's on your mind? ")

    with open("journal.txt", "a") as file:
        file.write(f"[{now}]\n{thought}\n" + "-" * 20 + "\n")

    print("Entry saved successfully!")


def view_entries():
    print("\n" + "=" * 30)
    print("         YOUR JOURNAL")
    print("=" * 30)

    try:

        with open("journal.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("Your journal is empty.")
            else:
                print(content)
    except FileNotFoundError:

        print("No journal file found yet. Write your first entry!")


def main():
    while True:
        print("\n--- Personal Journal ---")
        print("1. Write a new entry")
        print("2. Read past entries")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
