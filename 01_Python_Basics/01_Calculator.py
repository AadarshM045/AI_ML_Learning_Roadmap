import time
import math

# Calculator functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero."
def square(a): return a * a
def cube(a): return a * a * a
def power(a, b): return a ** b
def square_root(a): return math.sqrt(a)
def percentage(a, b): return (a * b) / 100

# Exit animation function
def exit_animation():
    print("Exiting calculator", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\nGoodbye!")

# Main calculator logic
def calculator():
    print("Welcome to Upgraded Python Calculator!")
    last_result = None
    history = []

    while True:
        print("\nSelect operation:")
        print("1 or + : Add")
        print("2 or - : Subtract")
        print("3 or * : Multiply")
        print("4 or / : Divide")
        print("5      : Square")
        print("6      : Cube")
        print("7      : Power")
        print("8      : Square Root")
        print("9      : Percentage")
        print("H      : Show History")
        print("0      : Exit")

        choice = input("Enter choice: ").strip()

        if choice == "0":
            exit_animation()
            break

        if choice.upper() == "H":
            if history:
                print("\n--- Calculation History ---")
                for record in history:
                    print(record)
            else:
                print("No calculations yet.")
            continue

        try:
            # Two-number operations
            if choice in ["1", "2", "3", "4", "+", "-", "*", "/"]:
                if last_result is not None:
                    print(f"Press Enter to use last result ({last_result}) as first number.")
                    num1_input = input("Enter first number: ")
                    num1 = float(num1_input) if num1_input else last_result
                else:
                    num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice in ["1", "+"]:
                    result = add(num1, num2)
                    history.append(f"{num1} + {num2} = {result}")
                elif choice in ["2", "-"]:
                    result = subtract(num1, num2)
                    history.append(f"{num1} - {num2} = {result}")
                elif choice in ["3", "*"]:
                    result = multiply(num1, num2)
                    history.append(f"{num1} * {num2} = {result}")
                elif choice in ["4", "/"]:
                    result = divide(num1, num2)
                    history.append(f"{num1} / {num2} = {result}")

            # Single-number operations
            elif choice in ["5", "6", "7", "8", "9"]:
                if last_result is not None:
                    print(f"Press Enter to use last result ({last_result}) as number.")
                    num_input = input("Enter number: ")
                    num = float(num_input) if num_input else last_result
                else:
                    num = float(input("Enter number: "))

                if choice == "5":
                    result = square(num)
                    history.append(f"{num}^2 = {result}")
                elif choice == "6":
                    result = cube(num)
                    history.append(f"{num}^3 = {result}")
                elif choice == "7":
                    exp = float(input("Enter power: "))
                    result = power(num, exp)
                    history.append(f"{num}^{exp} = {result}")
                elif choice == "8":
                    result = square_root(num)
                    history.append(f"√{num} = {result}")
                elif choice == "9":
                    perc = float(input("Enter percentage of: "))
                    result = percentage(num, perc)
                    history.append(f"{perc}% of {num} = {result}")

            else:
                print("Invalid choice! Try again.")
                continue

            last_result = result
            print("Result:", result)

        except ValueError:
            print("Invalid input! Please enter a number.")

# Main function
def main():
    calculator()

if __name__ == "__main__":
    main()
