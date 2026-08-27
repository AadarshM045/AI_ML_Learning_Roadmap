import random

def main():
    print("🎮 WELCOME TO THE NUMBER GUESSING GAME 🎮")

    
    while True:
        try:
            level = int(input("Enter the level (a positive number): "))
            if level > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    number = random.randint(1, level)
    

    print(f"\nI'm thinking of a number between 1 and {level}. Can you guess it?")

   
    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > level:
                print(f"Your guess is out of range! Please guess between 1 and {level}.")
                continue

            if guess > number:
                print("Too high! Try again.")
            elif guess < number:
                print("Too low! Try again.")
            else:
                print("🎉 Congratulations! You guessed the correct number!")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

main()
