# 06 — Files

> Reading from and writing to files so your data survives after the program closes.

---

## 📂 Projects

| # | Title | File | Description |
|---|-------|------|-------------|
| 01 | **Journal App** | [`01_Journal_App.py`](./01_Journal_App.py) | A personal diary with a looping menu — write timestamped entries (appended to `journal.txt`) or read all past entries. Handles a missing file gracefully on first run. |
| 02 | **Log File Analyzer** | [`02_Log_File_Analyzer.py`](./02_Log_File_Analyzer.py) | Reads `server.log` line by line, counts `[INFO]`, `[WARNING]`, and `[ERROR]` messages, then prints a summary report with all error lines listed separately. Auto-generates a sample log if none exists. |

---

## 🧠 What You'll Learn

- Opening files with `open()` and the `with` statement (auto-closes the file)
- File modes — `"a"` (append), `"r"` (read), `"w"` (write)
- Reading an entire file at once with `.read()`
- Reading a file line by line with a `for` loop (memory-efficient for large files)
- Appending structured data with timestamps using `datetime`
- Checking if a file exists with `os.path.exists()`
- Catching `FileNotFoundError` for a clean first-run experience
- Collecting matching lines into a list while scanning a file

---

## 💡 Key Concepts in Practice

```python
import datetime as dt
import os

# Timestamped entry — datetime formatted as a readable string
now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")

# Append mode — adds to the file without overwriting
with open("journal.txt", "a") as file:
    file.write(f"[{now}]\n{thought}\n" + "-" * 20 + "\n")

# Read mode — load entire file contents at once
with open("journal.txt", "r") as file:
    content = file.read()
    if content.strip() == "":
        print("Your journal is empty.")

# FileNotFoundError — handles the very first run cleanly
try:
    with open("journal.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("No journal file found yet. Write your first entry!")

# Check before creating — don't overwrite an existing file
if not os.path.exists("server.log"):
    with open("server.log", "w") as file:
        file.write(sample_data)

# Read line by line — efficient for large log files
errors = []
for line in file:
    if "[INFO]" in line:
        info_count += 1
    elif "[ERROR]" in line:
        error_count += 1
        errors.append(line.strip())   # collect error lines for later
```

---

## ▶️ How to Run

```bash
# Journal App
python3 01_Journal_App.py

# Log File Analyzer (auto-creates server.log on first run)
python3 02_Log_File_Analyzer.py
```

---

## 📄 Files Created at Runtime

| File | Created by | Purpose |
|------|-----------|---------|
| `journal.txt` | `01_Journal_App.py` | Stores all journal entries with timestamps |
| `server.log` | `02_Log_File_Analyzer.py` | Sample log file (only created if one doesn't exist) |

> These files are created in the same folder you run the script from. You can add `journal.txt` and `server.log` to your `.gitignore` if you don't want them committed.

---

## 🖥️ Sample Output — Journal App

```
--- Personal Journal ---
1. Write a new entry
2. Read past entries
3. Exit
Choose an option (1-3): 1

What's on your mind? Started learning file I/O today!
Entry saved successfully!

--- Personal Journal ---
Choose an option (1-3): 2

==============================
         YOUR JOURNAL
==============================
[2026-09-04 14:30]
Started learning file I/O today!
--------------------
```

## 🖥️ Sample Output — Log File Analyzer

```
Created a sample 'server.log' file for you!

===================================
        LOG FILE ANALYSIS REPORT
===================================
Total INFO messages:    2
Total WARNING messages: 2
Total ERROR messages:   2

--- Detailed Error Log ---
❌ 2026-09-04 09:05:44 [ERROR] Failed to connect to database.
❌ 2026-09-04 10:00:15 [ERROR] NullPointerException in payment module.
```

---

*Part of the [AI/ML Learning Roadmap](../../README.md)*