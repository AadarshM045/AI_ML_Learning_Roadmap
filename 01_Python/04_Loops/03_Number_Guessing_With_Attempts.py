import random

secret_number = random.randint(1, 100)
max_attempts = 7
Attempts_Used = 0


print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it!\n")


while Attempts_Used < max_attempts:
    guess = int(input(f"What is Your First Guess: "))
    Attempts_Used = Attempts_Used+1
    if guess > secret_number:
        print("High")
    elif guess < secret_number:
        print("low")
    else:
        print(f"\nBingo! You guessed it in {Attempts_Used} attempts!")
        break
    remaning = max_attempts-Attempts_Used
    if remaning > 0:
        print(f"You have {remaning} attempts left")
    if remaning == 0 and guess != secret_number:
        print(f"You ran out of attempts. The secret number is {secret_number}")
