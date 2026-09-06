# ============================================
#   CONTACT BOOK - Learn Python Dictionaries!
# ============================================
# A dictionary looks like this:
#   contact = {"name": "Alice", "phone": "123"}
#              key     value     key     value

# Our contact book is a dictionary of dictionaries!
contact_book = {}

# ---- FUNCTIONS ----


def add_contact(name, phone, email=""):
    """Add a new contact to the book."""
    contact_book[name] = {
        "phone": phone,
        "email": email
    }
    print(f"✅ Contact '{name}' added!")


def view_contact(name):
    """Look up one contact by name."""
    if name in contact_book:           # Check if key exists
        info = contact_book[name]      # Get the value (another dict)
        print(f"\n📇 {name}")
        print(f"   Phone : {info['phone']}")
        print(f"   Email : {info['email'] or 'Not set'}")
    else:
        print(f"❌ No contact named '{name}'.")


def list_contacts():
    """Show all contacts."""
    if not contact_book:
        print("📭 Your contact book is empty.")
        return
    print("\n📒 All Contacts:")
    for name, info in contact_book.items():   # .items() gives key + value
        print(f"  • {name} — {info['phone']}")


def delete_contact(name):
    """Remove a contact."""
    if name in contact_book:
        del contact_book[name]          # del removes a key
        print(f"🗑️  '{name}' deleted.")
    else:
        print(f"❌ No contact named '{name}'.")


def update_phone(name, new_phone):
    """Change a contact's phone number."""
    if name in contact_book:
        contact_book[name]["phone"] = new_phone   # Update a value
        print(f"✅ Phone updated for '{name}'.")
    else:
        print(f"❌ No contact named '{name}'.")


def search_contact(keyword):
    """Search contacts by name (partial match)."""
    found = [n for n in contact_book if keyword.lower() in n.lower()]
    if found:
        print(f"\n🔍 Found {len(found)} result(s):")
        for name in found:
            print(f"  • {name} — {contact_book[name]['phone']}")
    else:
        print(f"🔍 No contacts matching '{keyword}'.")

# ---- MENU ----


def menu():
    print("\n" + "="*40)
    print("       📱 CONTACT BOOK")
    print("="*40)
    print(" 1. Add contact")
    print(" 2. View contact")
    print(" 3. List all contacts")
    print(" 4. Delete contact")
    print(" 5. Update phone")
    print(" 6. Search contact")
    print(" 7. Quit")
    print("="*40)

# ---- MAIN PROGRAM ----


# Add some sample contacts to start
add_contact("Alice", "9841000001", "alice@email.com")
add_contact("Bob",   "9841000002", "bob@email.com")
add_contact("Carol", "9841000003")

while True:
    menu()
    choice = input("Choose (1-7): ").strip()

    if choice == "1":
        name = input("  Name  : ").strip()
        phone = input("  Phone : ").strip()
        email = input("  Email (press Enter to skip): ").strip()
        add_contact(name, phone, email)

    elif choice == "2":
        name = input("  Enter name: ").strip()
        view_contact(name)

    elif choice == "3":
        list_contacts()

    elif choice == "4":
        name = input("  Enter name to delete: ").strip()
        delete_contact(name)

    elif choice == "5":
        name = input("  Enter name: ").strip()
        phone = input("  New phone : ").strip()
        update_phone(name, phone)

    elif choice == "6":
        keyword = input("  Search keyword: ").strip()
        search_contact(keyword)

    elif choice == "7":
        print("👋 Bye!")
        break

    else:
        print("⚠️  Please enter a number from 1 to 7.")
