# 01 — Basics, Variables & Math

> First steps in Python: storing data in variables, doing arithmetic, and building interactive menu-driven programs.

📁 **Folder:** [`Python/01_Basics_Variables_Math`](./Python/01_Basics_Variables_Math)

---

## 📂 Projects

| # | Title | File | Description |
|---|-------|------|-------------|
| 01 | **Calculator** | [`01_Calculator.py`](./Python/01_Basics_Variables_Math/01_Calculator.py) | Menu-driven calculator supporting addition, subtraction, multiplication, division, square, cube, square root, cube root, and power — with division-by-zero protection. |
| 02 | **Temperature Converter** | [`02_Temperature_Converter.py`](./Python/01_Basics_Variables_Math/02_Temperature_Converter.py) | Converts temperatures between Celsius, Fahrenheit, and Kelvin using dedicated conversion functions and a looping menu. |
| 03 | **BMI Calculator** | [`03_BMI_Calculator.py`](./Python/01_Basics_Variables_Math/03_BMI_Calculator.py) | Calculates Body Mass Index from weight (kg) and height (m), then classifies the result as Underweight, Normal weight, Overweight, or Obese. |

---

## 🧠 What You'll Learn

- Declaring and using variables (`int`, `float`, `str`)
- Arithmetic operators — `+`, `-`, `*`, `/`, `**`, `%`
- Getting user input with `input()` and converting types with `float()`
- Writing and calling functions with `def` and `return`
- Building interactive loops with `while True` and `break`
- Formatting output with f-strings

---

## 💡 Key Concepts in Practice

```python
# Variables and arithmetic
weight = float(input("Enter Your Weight in kg: "))
height = float(input("Enter Your Height in meters: "))
bmi = weight / (height ** 2)

# Functions with return values
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Menu-driven loop
while True:
    choice = input("Enter your choice: ")
    if choice == "0":
        break
    # ... handle each option

# Division-by-zero guard
if b == 0:
    print("Error! Division by zero.")
else:
    print(f"Result: {a / b}")

# f-string formatting
print(f"Your BMI is: {bmi:.2f}")
```

---

## ▶️ How to Run

```bash
# Calculator
python3 Python/01_Basics_Variables_Math/01_Calculator.py

# Temperature Converter
python3 Python/01_Basics_Variables_Math/02_Temperature_Converter.py

# BMI Calculator
python3 Python/01_Basics_Variables_Math/03_BMI_Calculator.py
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

Enter your choice: 1
Enter the first Number: 10
Enter the second Number: 5
Result: 15.0
```

## 🖥️ Sample Output — BMI Calculator

```
Welcome to the BMI Calculator!

========== BMI CALCULATOR MENU ==========
1. Calculate BMI
2. Exit
=========================================

Enter Your Choice: 1
Enter Your Weight in kg: 70
Enter Your Height in meters: 1.75
Your BMI is: 22.86
You are classified as: Normal weight
```

---

*Part of the [AI/ML Learning Roadmap](../../README.md)*