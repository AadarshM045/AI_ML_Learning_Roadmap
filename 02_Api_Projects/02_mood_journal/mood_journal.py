"""
Mood Journal with Advice API
────────────────────────────
API used: https://api.adviceslip.com/advice  (no key needed)
Roadmap skills: Functions, Loops, Strings, Files, Dictionaries, datetime
"""

# third-party library to make HTTP requests (pip install requests)
import requests
import json       # built-in — reads and writes JSON files
import os         # built-in — used to check if journal.json exists on disk
from datetime import datetime  # built-in — gives us current date and time


# ── Where the journal lives on disk ───────────────────────────────────────────
# Written in ALL_CAPS = constant, this value never changes
# Every function uses this variable so we only define the filename once
JOURNAL_FILE = "journal.json"


# ══════════════════════════════════════════════════════════════════════════════
# 1. API
# Talks to the internet and returns a piece of advice as a string
# ══════════════════════════════════════════════════════════════════════════════

def fetch_advice() -> str:
    url = "https://api.adviceslip.com/advice"
    try:
        # Send a GET request to the API — like typing the URL in a browser
        # timeout=5 means: give up if no response within 5 seconds
        response = requests.get(url, timeout=5)

        # If server returned an error (404, 500 etc.) raise an exception immediately
        response.raise_for_status()

        # .json() decodes the response into a Python dictionary automatically
        # the API returns: {"slip": {"id": 1, "advice": "some advice here"}}
        data = response.json()

        # Dig into the nested dict to get just the advice string
        return data["slip"]["advice"]

    except requests.exceptions.ConnectionError:
        # No internet connection
        return "Could not fetch advice — check your internet connection."
    except requests.exceptions.HTTPError as e:
        # Server returned a 4xx or 5xx error
        return f"API error: {e}"
    except (KeyError, ValueError):
        # API returned unexpected data we couldn't parse
        return "Advice unavailable right now."


# ══════════════════════════════════════════════════════════════════════════════
# 2. FILE HELPERS
# These two functions handle all reading and writing to journal.json
# Every other function uses these — never opens the file directly
# ══════════════════════════════════════════════════════════════════════════════

def load_journal() -> list:
    # First run: journal.json doesn't exist yet — return empty list instead of crashing
    if not os.path.exists(JOURNAL_FILE):
        return []
    try:
        # Open in read mode ("r") and parse JSON into a Python list of dicts
        with open(JOURNAL_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # File is corrupted or unreadable — start fresh rather than crashing
        print("⚠  Could not read journal file — starting fresh.")
        return []


def save_journal(entries: list) -> None:
    # Open in write mode ("w") — this overwrites the file completely each time
    # indent=2 makes the JSON human-readable with nice indentation
    with open(JOURNAL_FILE, "w") as f:
        json.dump(entries, f, indent=2)


# ══════════════════════════════════════════════════════════════════════════════
# 3. CORE ACTIONS
# One function per menu option — each does exactly one job
# ══════════════════════════════════════════════════════════════════════════════

def add_entry(entries: list) -> None:

    print("\n── New Entry ──────────────────────────────────")

    # Dictionary mapping number keys to mood labels
    # moods.get(choice, fallback) lets us handle invalid input gracefully
    moods = {
        "1": "😄 Happy",
        "2": "😐 Neutral",
        "3": "😔 Sad",
        "4": "😤 Frustrated",
        "5": "😰 Anxious",
        "6": "⚡ Energetic",
    }

    # Print all mood options from the dictionary
    print("How are you feeling?")
    for key, label in moods.items():
        print(f"  {key}. {label}")

    # .strip() removes accidental spaces or newlines from user input
    mood_choice = input("Pick a number (1–6): ").strip()

    # If user types something invalid, second argument is the fallback default
    mood = moods.get(mood_choice, "😶 Unknown")

    # Note is optional — .strip() handles empty Enter press
    note = input("Add a note (or press Enter to skip): ").strip()

    # Hit the API — this is the one moment we talk to the internet
    # end=" " keeps the cursor on the same line so "done." prints next to it
    print("Fetching advice for you...", end=" ", flush=True)
    advice = fetch_advice()
    print("done.")

    # Build the entry as a dictionary — one key per field
    # "note if note else" = ternary: if note is empty string (falsy), store "(no note)"
    # strftime formats the date/time as a readable string
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),  # e.g. 2026-09-15
        "time": datetime.now().strftime("%H:%M"),     # e.g. 14:35
        "mood": mood,
        "note": note if note else "(no note)",
        "advice": advice,
    }

    # Add new entry to the in-memory list, then write the whole list to disk
    entries.append(entry)
    save_journal(entries)
    print(f"\n✅ Saved!\n💡 Today's advice: {advice}")


def view_entries(entries: list) -> None:

    # Empty list is falsy — "if not entries" catches the no-entries case
    if not entries:
        print("\nNo entries yet — add your first one!")
        return

    print(f"\n── Your Journal ({len(entries)} entries) ──────────────────")

    # reversed() loops the list backwards (newest first) without modifying the original
    for entry in reversed(entries):
        print(f"\n📅 {entry['date']}  🕐 {entry['time']}")
        print(f"   Mood   : {entry['mood']}")
        print(f"   Note   : {entry['note']}")
        print(f"   Advice : {entry['advice']}")

    print("\n" + "─" * 50)


def mood_summary(entries: list) -> None:

    if not entries:
        print("\nNo entries to summarise yet.")
        return

    # Count how many times each mood appears
    # counts.get(mood, 0) returns current count or 0 if mood not seen yet
    counts = {}
    for entry in entries:
        mood = entry["mood"]
        counts[mood] = counts.get(mood, 0) + 1

    # max() with key= compares moods by their count value, not alphabetically
    most_common = max(counts, key=lambda m: counts[m])

    print("\n── Mood Summary ───────────────────────────────")

    # sorted() with -x[1] sorts by count descending (highest first)
    for mood, count in sorted(counts.items(), key=lambda x: -x[1]):
        bar = "█" * count   # repeat block character to draw a simple bar
        print(f"  {mood:<18} {bar} ({count})")
        # :<18 = left-align in a 18-char wide field so all bars line up

    print(f"\n  Most frequent mood: {most_common}")
    print("─" * 50)


def search_entries(entries: list) -> None:

    if not entries:
        print("\nNo entries to search.")
        return

    # .lower() on both sides makes the search case-insensitive
    keyword = input("Search keyword: ").strip().lower()

    # List comprehension — builds a new list of only matching entries
    # reads as: "give me every e where keyword appears in note OR mood"
    results = [
        e for e in entries
        if keyword in e["note"].lower() or keyword in e["mood"].lower()
    ]

    if not results:
        print(f"  No entries found for '{keyword}'.")
        return

    print(f"\n── {len(results)} result(s) for '{keyword}' ────────────")
    for entry in results:
        print(f"\n  📅 {entry['date']}  {entry['mood']}")
        print(f"     {entry['note']}")


def delete_last_entry(entries: list) -> None:

    if not entries:
        print("\nNothing to delete.")
        return

    # entries[-1] = negative indexing — always the last item in the list
    last = entries[-1]
    note_preview = last["note"]

    # Show the entry details before deleting so user knows what they're removing
    print(f"\nLast entry: {last['date']}  {last['mood']}  \"{note_preview}\"")
    confirm = input("Delete this entry? (yes / no): ").strip().lower()

    if confirm == "yes":
        entries.pop()        # removes and returns the last item
        save_journal(entries)  # write the shorter list back to disk
        print("🗑  Entry deleted.")
    else:
        print("Cancelled.")


# ══════════════════════════════════════════════════════════════════════════════
# 4. MAIN — the program's engine
# Loads the journal once, then loops forever showing the menu
# until the user picks Quit
# ══════════════════════════════════════════════════════════════════════════════

def main() -> None:
    print("╔══════════════════════════════════╗")
    print("║       🌿 Mood Journal  v1.0       ║")
    print("╚══════════════════════════════════╝")

    # Load journal once at startup — all functions share this same list in memory
    entries = load_journal()

    # Menu dictionary: key → (display label, function to call)
    # Functions are objects in Python — you can store them in a dictionary
    menu = {
        "1": ("Add today's entry",   add_entry),
        "2": ("View all entries",    view_entries),
        "3": ("Mood summary",        mood_summary),
        "4": ("Search entries",      search_entries),
        "5": ("Delete last entry",   delete_last_entry),
        "6": ("Quit",                None),
    }

    # Run forever until user picks 6 (Quit) which hits break
    while True:
        print("\nWhat would you like to do?")

        # _ means "I know there's a value here but I don't need it right now"
        # here we only need the label for printing, not the function
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")

        choice = input("→ ").strip()

        # Quit — break exits the while loop and ends the program
        if choice == "6":
            print("\nTake care. See you tomorrow. 🌱")
            break

        # Invalid input — continue jumps back to the top of the while loop
        if choice not in menu:
            print("Invalid choice — pick 1 to 6.")
            continue

        # Unpack the tuple: ("Add today's entry", add_entry) → label, action
        label, action = menu[choice]

        # Call whichever function the user picked, passing the entries list
        # e.g. if choice == "1", this becomes add_entry(entries)
        if choice in ("2", "3", "4", "5"):
            action(entries)
        elif choice == "1":
            action(entries)


# ── Entry point ───────────────────────────────────────────────────────────────
# __name__ == "__main__" is only True when you run this file directly
# If someone imports this file into another script, main() won't auto-run
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Ctrl+C pressed — print a clean goodbye instead of a scary traceback
        print("\n\nExiting — your journal is saved. 👋")
