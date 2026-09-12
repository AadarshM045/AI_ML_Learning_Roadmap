def word_counter():
    try:
        text=input("Enter text to count: ")
        if not text.strip():
            raise ValueError("You didn't enter any text!")
        words=text.split()
        wordcount=len(words)
        charcount=len(text)
        sentence_count = text.count('.') + text.count('!') + text.count('?')
        print("\n---- Text Statistics ----")
        print(f"Characters: {charcount}")
        print(f"Words: {wordcount}")
        print(f"Sentences: {sentence_count}")
    except ValueError as e:
        print(f"⚠️ Error: {e}")

    except Exception as e:
        print(f"❌ Something went wrong: {e}")

word_counter()