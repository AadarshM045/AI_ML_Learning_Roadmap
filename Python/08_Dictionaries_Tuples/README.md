# 08 — Dictionaries & Tuples

> Storing structured, labelled data with key-value pairs — the step up from lists when your data has names, not just positions.

---

## 📂 Projects

| # | Title | File | Description |
|---|-------|------|-------------|
| 01 | **Contact Book** | [`01_Contact_Book.py`](./01_Contact_Book.py) | Full contact manager using a dictionary of dictionaries — add, view, list, delete, update phone, and partial-name search. Pre-loads three sample contacts on startup. |
| 02 | **Word Frequency Counter** | [`02_Word_Frequency_Counter.py`](./02_Word_Frequency_Counter.py) | Counts word occurrences in any text using a dictionary as a frequency map. Features top-N ranking, word search, unique-word listing, and summary statistics with visual bar charts. |
| 03 | **Simple Inventory System** | [`03_Simple_Inventory_System.py`](./03_Simple_Inventory_System.py) | Tracks product stock levels using dictionaries — add items, update quantities, and display inventory. |

---

## 🧠 What You'll Learn

- Creating dictionaries with `{}` and `key: value` pairs
- Dictionaries of dictionaries (nested dicts) for structured records
- Accessing values — `dict[key]` and `dict[key][nested_key]`
- Adding and updating keys — `dict[key] = value`
- Deleting keys — `del dict[key]`
- Checking membership — `if key in dict`
- Iterating with `.items()` to get both key and value
- `.keys()`, `.values()` for targeted iteration
- `sum(dict.values())` and `len(dict)` for aggregation
- `max()` / `min()` with `key=dict.get` to find highest/lowest value
- `sorted()` with `key=dict.get, reverse=True` for ranking
- List comprehension over a dictionary for filtering
- Global dictionary state shared across functions
- Default parameter values — `def add_contact(name, phone, email="")`

---

## 💡 Key Concepts in Practice

```python
# Nested dictionary — contact book
contact_book = {}

contact_book["Alice"] = {
    "phone": "9841000001",
    "email": "alice@email.com"
}

# Access nested value
print(contact_book["Alice"]["phone"])     # 9841000001

# Check before accessing
if name in contact_book:
    info = contact_book[name]
    print(info['email'] or 'Not set')     # fallback if email is empty

# Delete a key
del contact_book["Alice"]

# Iterate key + value pairs
for name, info in contact_book.items():
    print(f"{name} — {info['phone']}")

# Partial-name search with list comprehension
found = [n for n in contact_book if keyword.lower() in n.lower()]

# Frequency counter — the core dictionary trick
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1  # seen before → increment
    else:
        word_count[word] = 1                      # first time → set to 1

# Sort dictionary by value, highest first
sorted_words = sorted(word_count, key=word_count.get, reverse=True)
top_5 = sorted_words[:5]      # slice for top N

# Aggregate over all values
total = sum(word_count.values())
most_common = max(word_count, key=word_count.get)

# Filter with list comprehension
unique = [w for w in word_count if word_count[w] == 1]

# Visual bar from count
bar = "█" * count     # e.g. count=3 → "███"
```

---

## ▶️ How to Run

```bash
# Contact Book
python3 01_Contact_Book.py

# Word Frequency Counter
python3 02_Word_Frequency_Counter.py

# Simple Inventory System
python3 03_Simple_Inventory_System.py
```

---

## 🖥️ Sample Output — Contact Book

```
✅ Contact 'Alice' added!
✅ Contact 'Bob' added!
✅ Contact 'Carol' added!

========================================
       📱 CONTACT BOOK
========================================
 1. Add contact
 2. View contact
 ...

Choose (1-7): 2
  Enter name: Alice

📇 Alice
   Phone : 9841000001
   Email : alice@email.com

Choose (1-7): 6
  Search keyword: al

🔍 Found 1 result(s):
  • Alice — 9841000001
```

## 🖥️ Sample Output — Word Frequency Counter

```
Choose (1-8): 2
  Sample texts:
  1. the cat sat on the mat the cat is fat...

  Choose sample (1-3): 1
  Text: the cat sat on the mat the cat is fat
✅ Counted 9 words, 6 unique words.

Choose (1-8): 3

📊 All word counts:
  the             3  ███
  cat             2  ██
  sat             1  █
  on              1  █
  mat             1  █
  fat             1  █

Choose (1-8): 7

📈 Text Statistics:
   Total words   : 9
   Unique words  : 6
   Most common   : 'the' (3 times)
   Least common  : 'sat' (1 times)
```

---

*Part of the [AI/ML Learning Roadmap](../../README.md)*