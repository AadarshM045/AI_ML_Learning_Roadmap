import time

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error! Division by zero."
def square(a):
    return a*a
def cube(a):
    return a*a*a;
def sqroot(a):
    return a**(1/2)
def cbroot(a):
    return a**(1/3)
def power(a,b):
    return a**b

def calculator():
    print("Welcome to Our first Python Calculator")
    time.sleep(1.5)
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


        n=input("Enter: ")
        if n=="0":
            print("Exiting Calculator... Good Bye")
            time.sleep(1)
            break
        try:
            if n in ["1","2","3","4","9"]:
                a=float(input("Enter the first Number: "))
                b=float(input("Enter the second Number: "))
                if n=="1":
                    print(f"Result: {add(a,b)}")
                    time.sleep(1.5)
                elif n=="2":
                    print(f"Result: {sub(a,b)}")
                    time.sleep(1.5)
                elif n=="3":
                    print(f"Result: {multiply(a,b)}")
                    time.sleep(1.5)
                elif n=="4":
                    print(f"Result: {divide(a,b)}")
                    time.sleep(1.5)
                elif n=="9":
                    print(f"Result: {power(a,b)}")
                    time.sleep(1.5)
            elif n in ["5","6","7","8"]:
                c=float(input("Enter the Number: "))
                if n=="5":
                    print(f"Result: {square(c)}")
                    time.sleep(1.5)
                elif n=="6":
                    print(f"Result: {cube(c)}")
                    time.sleep(1.5)
                elif n=="7":
                    print(f"Result: {sqroot(c)}")
                    time.sleep(1.5)
                elif n=="8":
                    print(f"Result: {cbroot(c)}")
                    time.sleep(1.5)
            else:
                print("Invalid Input! Please check the input")
                time.sleep(1.5)

        except ValueError:
            print("Invalid input! Please enter a number.") 
            time.sleep(1.5)
def main():
    calculator()

if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting gracefully...")
            time.sleep(1)


                
                    



       
        
        
