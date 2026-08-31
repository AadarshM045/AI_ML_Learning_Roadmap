
text = input("Enter Text to encrypt: ")
shift = int(input("shifting: "))
i = 0
for i in text:
    text[i] = text[i]+shift
print(text)
