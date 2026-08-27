print("Welcome to Our first Python Calculator")

while True:
    print("""
========== CALCULATOR MENU ==========
1. Add
2. Subtract
3. Multiply
4. Divide
5. Square
6. Cube
7. Square Root
8. Cube Root
9. Power
0. Exit
=====================================
""")

    n = input("Enter your choice: ")

    if n == "0":
        print("Exiting Calculator... Good Bye")
        break

    # Operations that require two numbers
    if n in ["1", "2", "3", "4", "9"]:
        a = float(input("Enter the first Number: "))
        b = float(input("Enter the second Number: "))

        if n == "1":
            print(f"Result: {a + b}")
        elif n == "2":
            print(f"Result: {a - b}")
        elif n == "3":
            print(f"Result: {a * b}")
        elif n == "4":
            if b == 0:
                print("Error! Division by zero.")
            else:
                print(f"Result: {a / b}")
        elif n == "9":
            print(f"Result: {a ** b}")

    # Operations that require only one number
    elif n in ["5", "6", "7", "8"]:
        c = float(input("Enter the Number: "))

        if n == "5":
            print(f"Result: {c * c}")
        elif n == "6":
            print(f"Result: {c * c * c}")
        elif n == "7":
            print(f"Result: {c ** (1/2)}")
        elif n == "8":
            print(f"Result: {c ** (1/3)}")

    else:
        print("Invalid Input! Please select a number from the menu.")
