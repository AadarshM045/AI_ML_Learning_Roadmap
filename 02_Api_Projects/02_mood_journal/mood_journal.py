import os
import json
import requests
import datetime as dt

JOURNAL_FILE = "journal.json"


def fetch_advice():
    url = "https://api.adviceslip.com/advice"
    try:
        responce = requests.get(url, timeout=5)
        responce.raise_for_status()
        data = responce.json()
        return data
    except requests.exceptions.ConnectionError:
        return "Could not fetch advice — check your internet connection."
    except requests.exceptions.HTTPError as e:
        return f"API error: {e}"
    except (KeyError, ValueError):
        return "Advice unavailable right now."


def load_journal():
    if not os.path.exists(JOURNAL_FILE):
        return []
    try:
        with open("JOURNAL_FILE", "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("⚠  Could not read journal file — starting fresh.")
        return []


def save_journal(entries):
    with open("JOURNAL_FILE", "w") as f:
        return json.dump(entries, f, indent=2)


def add_entry() -> None:

    print("\n── New Entry ──────────────────────────────────")

    moods = {
        "1": "😄 Happy",
        "2": "😐 Neutral",
        "3": "😔 Sad",
        "4": "😤 Frustrated",
        "5": "😰 Anxious",
        "6": "⚡ Energetic",
    }
    print("How are you feeling?")
    for key, label in moods.items():
        print(f"  {key}. {label}")

    mood_choice = input("Enter Number (1-6): ")
    mood = moods.get(mood_choice, "😶 Unknown")

    note = input("Add a note (or press Enter to skip):").strip()

    print("Fetching advice for you...", end=" ", flush=True)
    advice = fetch_advice()
    print("Done.")

    entry = {
        "date": dt.now().strftime("%y-%m-%d"),
        "time": dt.now().strftime("%H:%M"),
        "mood": mood,
        "note": note if note else "(no note)",
        "advice": advice
    }
    entries.append(entry)
    save_journal(entries)
    print(f"\n✅ Saved!\n💡 Today's advice: {advice}")


def view_entries(entries):
    if not entries:
        print("\nNo entries yet — add your first one!")
        return

    print(f"\n── Your Journal ({len(entries)} entries) ──────────────────")
    for entry in reversed(entries):
        print(f"\n📅 {entry['date']}  🕐 {entry['time']}")
        print(f"   Mood   : {entry['mood']}")
        print(f"   Note   : {entry['note']}")
        print(f"   Advice : {entry['advice']}")
    print("\n" + "─" * 50)


def main():
    data = fetch_advice()
    entries = load_journal()
    print(entries)
    print(data["slip"]["advice"])
    add_entry()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting — your journal is saved. 👋")
