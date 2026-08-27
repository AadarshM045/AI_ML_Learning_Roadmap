# 02_Multiplication_Table.py

print("=== Multiplication Table Generator ===")

# Get the number from the user
num = int(input("Enter a number: "))

print(f"\nMultiplication Table for {num}:")
print("----------------------------")

# Loop from 1 to 10
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
