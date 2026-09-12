# 07 — Lists

> Storing, organising, and managing ordered collections of data — the most-used data structure in Python.

---

## 📂 Projects

| # | Title | File | Description |
|---|-------|------|-------------|
| 01 | **To-Do List** | [`01_To_Do_List.py`](./01_To_Do_List.py) | Full task manager — add tasks, view them numbered, and remove by index using `.append()` and `.pop()`. Validates empty input and out-of-range numbers. |
| 02 | **Grade Tracker** | [`02_Grade_Tracker.py`](./02_Grade_Tracker.py) | Stores float grades (0–100), displays them numbered, and calculates the average with `sum()` and `len()`. Validates both range and type of input. |
| 03 | **Shopping List Manager** | [`03_Shopping_List_Manager.py`](./03_Shopping_List_Manager.py) | Five-option shopping list — add (with duplicate detection and auto-capitalise), remove by index, view, and clear the entire list with `.clear()`. |

---

## 🧠 What You'll Learn

- Creating and passing lists between functions
- `.append()` to add items, `.pop(index)` to remove by position
- `.clear()` to wipe an entire list in one call
- `enumerate(list, start=1)` for clean numbered displays
- `len()` and `sum()` for counting and totalling
- The `in` operator to check for duplicates before adding
- `.strip()` and `.capitalize()` to clean user input
- `not list` as a readable way to check if a list is empty
- Range validation — `1 <= number <= len(tasks)`

---

## 💡 Key Concepts in Practice

```python
tasks = []      # start with an empty list
grades = []
shopping_list = []

# Add to a list
tasks.append(new_task)

# Remove by position — pop() returns the removed item
removed_task = tasks.pop(number - 1)
print(f"'{removed_task}' is removed!")

# enumerate() for numbered display (starts at 1, not 0)
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

# Check if a list is empty
if not tasks:
    print("No tasks yet.")

# Range validation before popping
if 1 <= number <= len(tasks):
    tasks.pop(number - 1)
else:
    print(f"Choose between 1 and {len(tasks)}.")

# sum() + len() for average
avg = sum(grades) / len(grades)
print(f"Average Grade: {avg:.2f}")

# Duplicate check with 'in'
if item in shopping_list:
    print(f"'{item}' is already on your list!")
else:
    shopping_list.append(item)

# Auto-capitalise and strip whitespace from input
item = input("Enter item: ").strip().capitalize()

# Clear entire list
shopping_list.clear()
```

---

## ▶️ How to Run

```bash
# To-Do List
python3 01_To_Do_List.py

# Grade Tracker
python3 02_Grade_Tracker.py

# Shopping List Manager
python3 03_Shopping_List_Manager.py
```

---

## 🖥️ Sample Output — To-Do List

```
==============================
          TO-DO LIST
==============================
1. View tasks
2. Add a task
3. Remove a task
4. Exit

Choose an option (1-4): 2
Enter the task you want to add: Buy groceries
'Buy groceries' is added successfully!

Choose an option (1-4): 1

--- YOUR TASKS ---
1. Buy groceries

Choose an option (1-4): 3

--- YOUR TASKS ---
1. Buy groceries

Enter the number of the task to remove: 1
'Buy groceries' is removed!
```

## 🖥️ Sample Output — Grade Tracker

```
Choose an option (1-4): 2
Enter the grade (0-100): 85
Grade 85.0 added successfully!

Choose an option (1-4): 3
Average Grade: 85.00
```

## 🖥️ Sample Output — Shopping List Manager

```
Choose an option (1-5): 2
Enter the item to add: milk
'Milk' added to the list.

Choose an option (1-5): 2
Enter the item to add: milk
'Milk' is already on your shopping list!

Choose an option (1-5): 4
Shopping list cleared successfully!
```

---

*Part of the [AI/ML Learning Roadmap](../../README.md)*