# 05 — Strings

> Manipulating, analysing, and transforming text — one of the most common tasks in real-world Python.

---

## 📂 Projects

| # | Title | File | Description |
|---|-------|------|-------------|
| 01 | **Word Counter** | [`01_Word_Counter.py`](./01_Word_Counter.py) | Analyses a block of text and reports character count, word count, and sentence count (detected via `.`, `!`, `?`). Raises a `ValueError` for empty input. |
| 02 | **Palindrome Checker** | [`02_Palindrome_Checker.py`](./02_Palindrome_Checker.py) | Checks if a word or phrase reads the same forwards and backwards — strips spaces and lowercases everything before comparing, so "Race Car" correctly passes. |
| 03 | **Caesar Cipher** | [`03_Caesar_Cipher.py`](./03_Caesar_Cipher.py) | Encrypts or decrypts a message by shifting each letter through the alphabet by a given amount. Non-letter characters (spaces, punctuation) are preserved as-is. |
| 04 | **Password Strength Checker** | [`04_Password_Strength_Checker.py`](./04_Password_Strength_Checker.py) | Scores a password out of 5 across length, lowercase, uppercase, digits, and special characters — then rates it from 💀 Very Weak to 🟢 Very Strong with specific improvement tips. |

---

## 🧠 What You'll Learn

- `.split()` to break text into a list of words
- `.strip()` to remove leading/trailing whitespace
- `.lower()` for case-insensitive comparisons
- `"".join()` to collapse a list back into a string
- String slicing `[::-1]` to reverse a string
- `.count()` to find occurrences of a substring
- `.index()` to find a character's position in a string
- Modulo `%` for wrap-around (Caesar cipher alphabet cycling)
- `any()` with a generator expression to scan a string for a character type
- The `string` module — `string.ascii_lowercase`, `string.digits`, `string.punctuation`
- Raising and catching custom `ValueError` messages

---

## 💡 Key Concepts in Practice

```python
import string

# Word / character / sentence counting
words = text.split()
word_count = len(words)
char_count = len(text)
sentence_count = text.count('.') + text.count('!') + text.count('?')

# Raising a ValueError for bad input
if not text.strip():
    raise ValueError("You didn't enter any text!")

# Palindrome — normalise then reverse
cleaned = "".join(text.lower().split())   # remove spaces, lowercase
reversed_text = cleaned[::-1]             # slice trick to reverse
is_palindrome = cleaned == reversed_text

# Caesar cipher — shift with wrap-around using %
alphabet = "abcdefghijklmnopqrstuvwxyz"
position = alphabet.index(letter)
new_position = (position + shift) % 26    # % keeps it within 0-25
result += alphabet[new_position]

# Preserve non-letter characters
if letter in alphabet:
    result += alphabet[new_position]
else:
    result += letter                       # spaces, punctuation unchanged

# Password scoring with any() + generator
if any(char in string.ascii_uppercase for char in password):
    score += 1
else:
    feedback.append("❌ Add an UPPERCASE letter")

# Strength rating from score
def get_strength(score):
    if score == 5:   return "🟢 Very Strong"
    elif score == 4: return "🟡 Strong"
    elif score == 3: return "🟠 Medium"
    elif score == 2: return "🔴 Weak"
    else:            return "💀 Very Weak"
```

---

## ▶️ How to Run

```bash
# Word Counter
python3 01_Word_Counter.py

# Palindrome Checker
python3 02_Palindrome_Checker.py

# Caesar Cipher
python3 03_Caesar_Cipher.py

# Password Strength Checker
python3 04_Password_Strength_Checker.py
```

---

## 🖥️ Sample Output — Word Counter

```
Enter text to count: Hello world! How are you?

---- Text Statistics ----
Characters: 25
Words: 5
Sentences: 2
```

## 🖥️ Sample Output — Palindrome Checker

```
Enter The text: Race Car
Is Palindrom
```

## 🖥️ Sample Output — Caesar Cipher

```
🔐 Caesar Cipher
--------------------
Enter your message: hello world
Encode or decode? encode
Enter shift number (e.g. 3): 3

Result: khoor zruog
```

## 🖥️ Sample Output — Password Strength Checker

```
🔐 Password Strength Checker
------------------------------
Enter a password to check: hello
Score    : 1/5
Strength : 💀 Very Weak

To improve your password:
❌ Use at least 8 characters
❌ Add an UPPERCASE letter
❌ Add a number
❌ Add a special character (!@#$...)
```

```
Enter a password to check: MyP@ssw0rd
Score    : 5/5
Strength : 🟢 Very Strong

✅ Perfect! Your password passes all checks.
```

---

*Part of the [AI/ML Learning Roadmap](../../README.md)*