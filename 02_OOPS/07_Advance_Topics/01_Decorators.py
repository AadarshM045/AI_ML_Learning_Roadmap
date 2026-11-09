# =====================================================================
# PYTHON DECORATORS (ADDING EXTRA BEHAVIOR TO EXISTING FUNCTIONS)
# =====================================================================
# What is a Decorator?
# A decorator is a design pattern in Python used to modify or extend the
# behavior of a function or method *without* permanently changing its source code.
# It takes a function as input, adds some functionality, and returns a new function.

# 1. The Decorator Function
def extragreeting(func):
    # This nested 'wrapper' function holds the extra logic we want to add
    def wrapper():
        print("Good Morning")  # Extra behavior added *before* the main function
        func()                  # Calls the original function passed into the decorator

    return wrapper  # Returns the wrapper function (not calling it yet!)


# 2. Applying the Decorator using the '@' syntax (Syntactic Sugar)
# Writing '@extragreeting' right above 'greeting' is shorthand for writing:
# greeting = extragreeting(greeting)
@extragreeting
def greeting():
    print("Hey How are you?")


# =====================================================================
# TESTING THE CODE IN YOUR IDE
# =====================================================================

# When we call 'greeting()', we are actually calling the 'wrapper' function
# created inside the decorator, which runs the extra print statement first!
greeting()

# --- Output of this code ---
# Good Morning
# Hey How are you?
