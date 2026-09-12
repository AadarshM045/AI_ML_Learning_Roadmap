# 02 — Conditionals

> Teaching your program to make decisions with `if`, `elif`, and `else` — plus your first taste of input validation and the `random` module.

📁 **Folder:** [`Python/02_Conditionals`](./Python/02_Conditionals)

---

## 📂 Projects

| # | Title | File | Description |
|---|-------|------|-------------|
| 01 | **Number Guessing Game** | [`01_Number_Guessing_Game.py`](./Python/02_Conditionals/01_Number_Guessing_Game.py) | Player sets the difficulty by choosing a number range — the computer picks a random number within it, then gives "Too high" / "Too low" hints until the player guesses correctly. Fully validates all inputs. |
| 02 | **Grade Calculator** | [`02_Grade_Calculator.py`](./02_Conditionals/02_Grade_Calculator.py) | Takes a percentage score (0–100) and maps it to a letter grade (A / B / C / D / F) using a chain of `elif` conditions, with a guard for negative inputs. |

---

## 🧠 What You'll Learn

- `if` / `elif` / `else` for branching logic
- Chaining multiple conditions to cover all cases
- Comparison operators — `==`, `!=`, `<`, `>`, `<=`, `>=`
- `while True` loops with `break` to keep asking until valid input
- `try` / `except ValueError` for safe number input
- `continue` to skip the rest of a loop iteration
- The `random` module — `random.randint(a, b)`
- Out-of-range validation

---

## 💡 Key Concepts in Practice

```python
import random

# User-controlled difficulty — validates input with try/except
while True:
    try:
        level = int(input("Enter the level (a positive number): "))
        if level > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Random number in player-defined range
number = random.randint(1, level)

# Higher / lower hint system
if guess > number:
    print("Too high! Try again.")
elif guess < number:
    print("Too low! Try again.")
else:
    print("🎉 Congratulations! You guessed the correct number!")

# Out-of-range guard with continue
if guess < 1 or guess > level:
    print(f"Please guess between 1 and {level}.")
    continue

# Grade mapping with chained elif
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 0:
    grade = "F"
else:
    grade = "Invalid (Score cannot be negative)"
```

---

## ▶️ How to Run

```bash
# Number Guessing Game
python3 Python/02_Conditionals/01_Number_Guessing_Game.py

# Grade Calculator
python3 Python/02_Conditionals/02_Grade_Calculator.py
```

---

## 🖥️ Sample Output — Number Guessing Game

```
🎮 WELCOME TO THE NUMBER GUESSING GAME 🎮
Enter the level (a positive number): 50

I'm thinking of a number between 1 and 50. Can you guess it?
Enter your guess: 25
Too high! Try again.
Enter your guess: 12
Too low! Try again.
Enter your guess: 18
🎉 Congratulations! You guessed the correct number!
```

## 🖥️ Sample Output — Grade Calculator

```
Enter your percentage/score (0-100): 84
Your final grade is: B
```

---

*Part of the [AI/ML Learning Roadmap](../../README.md)*