def caesar_cipher(message, shift, mode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message = message.lower()
    result = ""

    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)

            if mode == "encode":
                new_position = (position + shift) % 26
            elif mode == "decode":
                new_position = (position - shift) % 26

            result += alphabet[new_position]
        else:
            result += letter

    return result


def main():
    print("🔐 Caesar Cipher")
    print("-" * 20)

    message = input("Enter your message: ")

    mode = input("Encode or decode? ").lower()
    while mode not in ["encode", "decode"]:       # keep asking if wrong input
        print("Please type 'encode' or 'decode'")
        mode = input("Encode or decode? ").lower()

    # input() gives a string, int() converts it to a number
    shift = int(input("Enter shift number (e.g. 3): "))

    result = caesar_cipher(message, shift, mode)
    print(f"\nResult: {result}")


if __name__ == "__main__":
    main()
