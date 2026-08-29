# Simple Python Grade Calculator

# 1. Take score input from the user and convert it to a floating-point number
score = float(input("Enter your percentage/score (0-100): "))

# 2. Check score ranges from highest to lowest
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 0:
    grade = "F"
else:
    grade = "Invalid (Score cannot be negative)"

# 3. Output the result
print(f"Your final grade is: {grade}")
