def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a-b;
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
    while True:
        print("Select Operatios:" \
        "1:Add:" \
        "2:Subtract:" \
        "3:Multiply:" \
        "4:Divide:" \
        "5:Square:" \
        "6:Cube:" \
        "7:Square Root:" \
        "8:Cube Root:" \
        "9:Power:" \
        "0:Exit:")


