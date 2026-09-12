# 02_Unit_Converter.py


# 1. Define conversion functions
def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# 2. Main program loop
def main():
    print("=== Unit Converter ===")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")

    choice = input("\nSelect a conversion (1-4): ").strip()

    if choice in ["1", "2", "3", "4"]:
        value = float(input("Enter value to convert: "))

        if choice == "1":
            result = km_to_miles(value)
            print(f"{value} km = {result:.2f} miles")
        elif choice == "2":
            result = miles_to_km(value)
            print(f"{value} miles = {result:.2f} km")
        elif choice == "3":
            result = celsius_to_fahrenheit(value)
            print(f"{value}°C = {result:.2f}°F")
        elif choice == "4":
            result = fahrenheit_to_celsius(value)
            print(f"{value}°F = {result:.2f}°C")
    else:
        print("Invalid choice. Please pick a number from 1 to 4.")


# 3. Entry point trigger
if __name__ == "__main__":
    main()
