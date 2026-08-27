def bmi_calculator(weight, height):
    bmi = weight/(height**2)  # ** is used for power calculation
    return bmi


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


print("Welcome to the BMI Calculator!")
while True:
    print("""
========== BMI CALCULATOR MENU ==========
1. Calculate BMI
2. Exit
=========================================
""")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        weight = float(input("Enter Your Weight in kg: "))
        height = float(input("Enter Your Height in meters: "))
        bmi = bmi_calculator(weight, height)
        category = get_bmi_category(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
    elif choice == "2":
        print("Exiting BMI Calculator... Good Bye")
        break
    else:
        print("Invalid Choice! Please try again.")
