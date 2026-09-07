# ============================================
#   WORD FREQUENCY COUNTER
#   Learn Python Dictionaries - Project 02
# ============================================
# A dictionary is perfect for counting things:
#   word_count = {"hello": 3, "world": 2}
#                  key     value  key   value
#                  word    count  word  count

# Our frequency counter is a dictionary!
# key   = the word
# value = how many times it appears

word_count = {}   # empty dictionary to store word counts

# ---- SAMPLE TEXTS ----

sample_texts = {
    "1": "the cat sat on the mat the cat is fat",
    "2": "python is great python is fun python is easy to learn",
    "3": "I love coding I love python I love learning new things",
}

# ---- FUNCTIONS ----


def count_words(text):
    """Count how many times each word appears in the text."""
    global word_count
    word_count = {}              # reset to empty every time

    words = text.lower().split()  # split sentence into list of words

    # THE CORE DICTIONARY TRICK:
    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1  # already seen → add 1
        else:
            word_count[word] = 1                     # first time → set to 1

    print(f"\n✅ Counted {len(words)} words, {len(word_count)} unique words.")


def show_all():
    """Show every word and its count."""
    if not word_count:
        print("❌ No text counted yet. Please count a text first.")
        return
    print(f"\n📊 All word counts:")
    for word, count in word_count.items():     # .items() gives key + value
        bar = "█" * count                      # visual bar to show count
        print(f"  {word:<15} {count}  {bar}")


def show_top(n=5):
    """Show the top N most frequent words."""
    if not word_count:
        print("❌ No text counted yet. Please count a text first.")
        return

    # sorted() sorts the dictionary by value (count), highest first
    sorted_words = sorted(word_count, key=word_count.get, reverse=True)
    top = sorted_words[:n]     # slice — take only first n items

    print(f"\n🏆 Top {n} most frequent words:")
    for i, word in enumerate(top, start=1):   # enumerate gives index + value
        count = word_count[word]
        bar = "█" * count
        print(f"  {i}. {word:<15} {count}  {bar}")


def search_word(word):
    """Check how many times a specific word appears."""
    if not word_count:
        print("❌ No text counted yet. Please count a text first.")
        return

    word = word.lower()
    if word in word_count:
        print(f"\n🔍 '{word}' appears {word_count[word]} time(s).")
    else:
        print(f"\n🔍 '{word}' not found in the text.")


def show_unique():
    """Show words that appear only once."""
    if not word_count:
        print("❌ No text counted yet. Please count a text first.")
        return

    # list comprehension — same as contact book search!
    unique = [w for w in word_count if word_count[w] == 1]

    if unique:
        print(f"\n🔤 Words appearing only once ({len(unique)} words):")
        for w in unique:
            print(f"  • {w}")
    else:
        print("\n🔤 No unique words found.")


def show_stats():
    """Show summary statistics about the text."""
    if not word_count:
        print("❌ No text counted yet. Please count a text first.")
        return

    total_words = sum(word_count.values())   # sum of all counts
    unique_words = len(word_count)            # number of keys
    most_common = max(word_count, key=word_count.get)  # key with highest value
    least_common = min(word_count, key=word_count.get)  # key with lowest value

    print(f"\n📈 Text Statistics:")
    print(f"   Total words   : {total_words}")
    print(f"   Unique words  : {unique_words}")
    print(
        f"   Most common   : '{most_common}' ({word_count[most_common]} times)")
    print(
        f"   Least common  : '{least_common}' ({word_count[least_common]} times)")

# ---- MENU ----


def menu():
    print("\n" + "="*45)
    print("       📝 WORD FREQUENCY COUNTER")
    print("="*45)
    print(" 1. Count words in your own text")
    print(" 2. Use a sample text")
    print(" 3. Show all word counts")
    print(" 4. Show top 5 words")
    print(" 5. Search for a word")
    print(" 6. Show words appearing only once")
    print(" 7. Show text statistics")
    print(" 8. Quit")
    print("="*45)

# ---- MAIN PROGRAM ----


print("\nWelcome to Word Frequency Counter!")
print("This program uses a DICTIONARY to count words.")
print("key = word,  value = how many times it appears\n")

while True:
    menu()
    choice = input("Choose (1-8): ").strip()

    if choice == "1":
        text = input("\n  Enter your text:\n  > ").strip()
        if text:
            count_words(text)
        else:
            print("⚠️  Please enter some text.")

    elif choice == "2":
        print("\n  Sample texts:")
        for key, text in sample_texts.items():
            print(f"  {key}. {text[:45]}...")
        pick = input("  Choose sample (1-3): ").strip()
        if pick in sample_texts:
            print(f"\n  Text: {sample_texts[pick]}")
            count_words(sample_texts[pick])
        else:
            print("⚠️  Invalid choice.")

    elif choice == "3":
        show_all()

    elif choice == "4":
        n = input("  How many top words to show? (default 5): ").strip()
        n = int(n) if n.isdigit() else 5
        show_top(n)

    elif choice == "5":
        word = input("  Enter word to search: ").strip()
        search_word(word)

    elif choice == "6":
        show_unique()

    elif choice == "7":
        show_stats()

    elif choice == "8":
        print("👋 Bye!")
        break

    else:
        print("⚠️  Please enter a number from 1 to 8.")
