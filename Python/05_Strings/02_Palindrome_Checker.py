def Is_Palindrom(text):
    cleaned_text = "".join(text.lower().split())
    reversed = cleaned_text[::-1]
    return cleaned_text == reversed


def main():
    text = input("Enter The text: ")
    reversed = Is_Palindrom(text)
    if Is_Palindrom(text):
        print("Is Palindrom")
    else:
        print("Not palindrom")


if __name__ == "__main__":
    main()
