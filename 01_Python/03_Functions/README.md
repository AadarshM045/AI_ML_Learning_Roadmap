# 03 — Functions

> Wrapping logic into named, reusable blocks — the step that turns a script into proper, organised code.

---

## 📂 Projects

| # | Title | File | Description |
|---|-------|------|-------------|
| 01 | **Calculator** | [`01_Calculator.py`](./01_Calculator.py) | Full refactor of the basics calculator — every operation (`add`, `sub`, `multiply`, `divide`, `square`, `cube`, `sqroot`, `cbroot`, `power`) lives in its own function. Adds `time.sleep()` pacing and graceful `KeyboardInterrupt` handling. |
| 02 | **Unit Converter** | [`02_Unit_Conversion.py`](./02_Unit_Conversion.py) | Converts between km ↔ miles and Celsius ↔ Fahrenheit using four dedicated conversion functions, a clean menu, and a single-run entry point. |

---

## 🧠 What You'll Learn

- Defining functions with `def` and returning values with `return`
- Separating logic into single-purpose functions (one function = one job)
- Calling functions from other functions (`calculator()` calls `add()`, `divide()`, etc.)
- `try` / `except` inside a function to handle errors at the source
- `if __name__ == "__main__"` — the standard Python entry point pattern
- `KeyboardInterrupt` — catching Ctrl+C for a graceful exit
- `time.sleep()` for pacing output in interactive programs
- `.strip()` to clean whitespace from user input

---

## 💡 Key Concepts in Practice

```python
import time

# Single-purpose functions — each does exactly one thing
def add(a, b):
    return a + b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero."

def square(a):
    return a * a

def power(a, b):
    return a ** b

# A controller function that calls the others
def calculator():
    while True:
        n = input("Enter: ")
        if n == "0":
            break
        if n == "1":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            print(f"Result: {add(a, b)}")
            time.sleep(1.5)

# Standard Python entry point
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting gracefully...")

# Conversion functions with a formula in the return
def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# .strip() removes accidental leading/trailing spaces
choice = input("Select a conversion (1-4): ").strip()
```

---

## 🔍 01 vs 03 Calculator — What Changed?

The calculator from `01_Basics_Variables_Math` and this one do the same thing, but the code is very different:

| | `01_Basics` Calculator | `03_Functions` Calculator |
|---|---|---|
| Operations | Inline `if/elif` blocks | Separate named functions |
| Error handling | Inline `if b == 0` check | `try/except` inside `divide()` |
| Exit handling | `break` only | `break` + `KeyboardInterrupt` catch |
| Pacing | None | `time.sleep()` between results |
| Structure | One big block | `calculator()` → `main()` → `__main__` |

This is what **refactoring** looks like — same output, cleaner structure.

---

## ▶️ How to Run

```bash
# Calculator (functions version)
python3 01_Calculator.py

# Unit Converter
python3 02_Unit_Conversion.py
```

---

## 🖥️ Sample Output — Calculator

```
Welcome to Our first Python Calculator

========== CALCULATOR MENU ==========
1. Add
2. Subtract
3. Multiply
4. Divide
5. Square
6. Cube
7. Square Root
8. Cube Root
9. Power
0. Exit
=====================================

Enter: 4
Enter the first Number: 10
Enter the second Number: 0
Result: Error! Division by zero.
```

## 🖥️ Sample Output — Unit Converter

```
=== Unit Converter ===
1. Kilometers to Miles
2. Miles to Kilometers
3. Celsius to Fahrenheit
4. Fahrenheit to Celsius

Select a conversion (1-4): 1
Enter value to convert: 100
100 km = 62.14 miles
```

---

*Part of the [AI/ML Learning Roadmap](../../README.md)*