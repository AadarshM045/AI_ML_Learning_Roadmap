# 04 — Loops

> Automating repetition with `for` and `while` — the backbone of almost every real program.

---

## 📂 Projects

| # | Title | File | Description |
|---|-------|------|-------------|
| 01 | **Multiplication Table** | [`01_Multiplication_Table.py`](./01_Multiplication_Table.py) | Takes a number from the user and prints its multiplication table from 1 to 10 using a `for` loop with `range()`. |
| 02 | **FizzBuzz** | [`02_FizzBuzz.py`](./02_FizzBuzz.py) | Classic programming challenge — loops from 1 to n, printing "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both. |
| 03 | **Number Guessing** | [`03_Number_Guessing.py`](./03_Number_Guessing.py) | Loops-based guessing game with a fixed secret number (1–100) and a 7-attempt limit. Tracks attempts used, shows remaining attempts each round, and reveals the answer if the player runs out. |

---

## 🧠 What You'll Learn

- `for` loops with `range(start, stop)` to iterate a fixed number of times
- `while` loops with a counter condition for attempt-limited games
- `break` to exit a loop early when a goal is met
- The modulo operator `%` for divisibility checks
- Tracking state across loop iterations (attempt counters, remaining attempts)
- Wrapping loop logic inside a function and calling it from `main()`
- `if __name__ == "__main__"` entry point pattern

---

## 💡 Key Concepts in Practice

```python
import random

# for loop with range — fixed iterations
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")

# Modulo for FizzBuzz — check both conditions first
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:   # must come before the individual checks
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# while loop with attempt counter
secret_number = random.randint(1, 100)
max_attempts = 7
attempts_used = 0

while attempts_used < max_attempts:
    guess = int(input("Your guess: "))
    attempts_used = attempts_used + 1
    remaining = max_attempts - attempts_used

    if guess == secret_number:
        print(f"Bingo! You guessed it in {attempts_used} attempts!")
        break

    if remaining > 0:
        print(f"You have {remaining} attempts left")
    if remaining == 0 and guess != secret_number:
        print(f"You ran out of attempts. The secret number is {secret_number}")
```

---

## 🔍 02 vs 04 Guessing Game — What Changed?

You've now written a guessing game twice — once in Conditionals, once here. Here's what's different:

| | `02_Conditionals` Guessing Game | `04_Loops` Guessing Game |
|---|---|---|
| Range | Player chooses the range | Fixed 1–100 |
| Attempts | Unlimited | 7 max (`max_attempts`) |
| Loop type | `while True` + `break` | `while attempts_used < max_attempts` |
| Tracking | No counter | Tracks attempts used + remaining |
| Reveal on loss | ❌ | ✅ Shows the secret number |

Same game idea, but the `while` condition itself now controls the game flow instead of a bare `while True`.

---

## ▶️ How to Run

```bash
# Multiplication Table
python3 01_Multiplication_Table.py

# FizzBuzz
python3 02_FizzBuzz.py

# Number Guessing Game
python3 03_Number_Guessing.py
```

---

## 🖥️ Sample Output — Multiplication Table

```
=== Multiplication Table Generator ===
Enter a number: 6

Multiplication Table for 6:
----------------------------
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
...
6 x 10 = 60
```

## 🖥️ Sample Output — FizzBuzz

```
Enter a number to start FizzBuzz: 15
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

## 🖥️ Sample Output — Number Guessing Game

```
=== Number Guessing Game ===
I'm thinking of a number between 1 and 100.
You have 7 attempts to guess it!

What is Your First Guess: 50
High
You have 6 attempts left
What is Your First Guess: 25
low
You have 5 attempts left
What is Your First Guess: 33

Bingo! You guessed it in 3 attempts!
```

---

*Part of the [AI/ML Learning Roadmap](../../README.md)*