def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


def celsius_to_kelvin(c):
    return c + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


print("Welcome to the Temperature Converter!")
while True:
    print("""
    ========== TEMPERATURE CONVERTER MENU ==========
    1. Celsius to Fahrenheit
    2. Fahrenheit to Celsius
    3. Celsius to Kelvin
    4. Kelvin to Celsius
    5. Exit
    ================================================
    """)
    choice = input("Enter Your Choice: ")
    if choice == "1":
        c = float(input("Enter Tempreature in Celsius: "))
        print(f"{c}°C is equal to {celsius_to_fahrenheit(c):.2f}°F")
    elif choice == "2":
        f = float(input("Enter Tempreature in Fahrenheit: "))
        print(f"{f}°F is equal to {fahrenheit_to_celsius(f):.2f}°C")
    elif choice == "3":
        c = float(input("Enter Tempreature in Celsius: "))
        print(f"{c}°C is equal to {celsius_to_kelvin(c):.2f}K")
    elif choice == "4":
        k = float(input("Enter Tempreature in Kelvin: "))
        print(f"{k}K is equal to {kelvin_to_celsius(k):.2f}°C")
    elif choice == "5":
        print("Exiting Temperature Converter... Good Bye")
        break
    else:
        print("Invalid Choice! Please try again.")
