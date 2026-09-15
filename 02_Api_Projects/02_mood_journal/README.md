# 02 — Mood Journal with Advice API

> A personal mood tracker that fetches a real piece of advice from the internet every time you log an entry — your first project that talks to a live API.

---

## 📂 Files

| File | Purpose |
|------|---------|
| [`mood_journal.py`](./mood_journal.py) | Main program |
| [`journal.json`](./journal.json) | Auto-created on first run — stores all your entries |

---

## 🌐 API Used

| | |
|---|---|
| **Name** | [Advice Slip API](https://api.adviceslip.com/) |
| **Endpoint** | `https://api.adviceslip.com/advice` |
| **Auth** | None — no API key needed |
| **What it returns** | `{"slip": {"id": 1, "advice": "some advice here"}}` |

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Add entry** | Pick a mood, write an optional note, get live advice from the API |
| 2 | **View all entries** | Displays entries newest-first with date, time, mood, note, and advice |
| 3 | **Mood summary** | Counts how often each mood appears with a visual bar chart |
| 4 | **Search entries** | Case-insensitive keyword search across notes and moods |
| 5 | **Delete last entry** | Shows a preview and asks for confirmation before deleting |

---

## 🧠 What You'll Learn

- `requests.get()` — making HTTP GET requests to a live API
- `response.json()` — decoding a JSON response into a Python dictionary
- `response.raise_for_status()` — catching server-side errors (4xx, 5xx)
- Handling network errors — `ConnectionError`, `HTTPError`, `KeyError`
- `json.load()` and `json.dump()` — reading and writing JSON files
- `os.path.exists()` — checking if a file exists before opening it
- Constants in ALL_CAPS — `JOURNAL_FILE = "journal.json"`
- Storing functions as dictionary values and calling them dynamically
- `reversed()` — iterating a list backwards without modifying it
- `lambda` — inline anonymous functions for sorting (`key=lambda x: -x[1]`)
- Negative indexing — `entries[-1]` to access the last item
- Type hints — `def fetch_advice() -> str`, `def load_journal() -> list`
- `f"{mood:<18}"` — left-aligned f-string formatting for neat output

---

## 💡 Key Concepts in Practice

```python
import requests, json, os
from datetime import datetime

# ── API call ──────────────────────────────────────────
response = requests.get("https://api.adviceslip.com/advice", timeout=5)
response.raise_for_status()                    # raises if 4xx/5xx
data = response.json()                         # dict from JSON
advice = data["slip"]["advice"]                # dig into nested dict

# ── JSON file I/O ─────────────────────────────────────
with open("journal.json", "r") as f:
    entries = json.load(f)                     # JSON → Python list

with open("journal.json", "w") as f:
    json.dump(entries, f, indent=2)            # Python list → JSON

# ── Storing functions in a dictionary ────────────────
menu = {
    "1": ("Add today's entry", add_entry),
    "2": ("View all entries",  view_entries),
}
label, action = menu[choice]
action(entries)                                # calls the function

# ── Mood frequency counter ────────────────────────────
counts = {}
for entry in entries:
    mood = entry["mood"]
    counts[mood] = counts.get(mood, 0) + 1    # same dict trick as Word Counter

# ── Sort by count descending with lambda ─────────────
for mood, count in sorted(counts.items(), key=lambda x: -x[1]):
    bar = "█" * count
    print(f"  {mood:<18} {bar} ({count})")

# ── List comprehension search ─────────────────────────
results = [
    e for e in entries
    if keyword in e["note"].lower() or keyword in e["mood"].lower()
]

# ── Negative indexing + confirmation before delete ───
last = entries[-1]
if confirm == "yes":
    entries.pop()
    save_journal(entries)
```

---

## ▶️ How to Run

**Install the one dependency first:**
```bash
pip install requests
```

**Then run:**
```bash
python3 mood_journal.py
```

> `journal.json` is created automatically on your first entry. You can add it to `.gitignore` if you don't want your personal entries committed.

---

## 🖥️ Sample Output

```
╔══════════════════════════════════╗
║       🌿 Mood Journal  v1.0       ║
╚══════════════════════════════════╝

What would you like to do?
  1. Add today's entry
  2. View all entries
  3. Mood summary
  4. Search entries
  5. Delete last entry
  6. Quit
→ 1

── New Entry ──────────────────────────────────
How are you feeling?
  1. 😄 Happy
  2. 😐 Neutral
  3. 😔 Sad
  4. 😤 Frustrated
  5. 😰 Anxious
  6. ⚡ Energetic
Pick a number (1–6): 1
Add a note (or press Enter to skip): Finished my mood journal project!
Fetching advice for you... done.

✅ Saved!
💡 Today's advice: Always do your best, and people will respect you for it.
```

```
→ 3

── Mood Summary ───────────────────────────────
  😄 Happy           ███ (3)
  😐 Neutral         █ (1)
  ⚡ Energetic       █ (1)

  Most frequent mood: 😄 Happy
──────────────────────────────────────────────
```

---

## 🔗 How This Project Uses Previous Skills

| Skill | Where it appears |
|-------|-----------------|
| Functions | Every feature is its own function |
| Dictionaries | Entry storage, mood counter, menu system |
| File I/O | `load_journal()` / `save_journal()` |
| Lists | `entries` list, comprehension search |
| Strings | `.lower()`, `.strip()`, f-string formatting |
| `datetime` | Timestamping every entry |
| `try/except` | API errors, file read errors |

---

*Part of the [AI/ML Learning Roadmap](../../../README.md)*