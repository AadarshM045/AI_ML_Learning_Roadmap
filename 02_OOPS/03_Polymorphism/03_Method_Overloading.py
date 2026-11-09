# =====================================================================
# 1. IS METHOD OVERLOADING AVAILABLE IN PYTHON?
# =====================================================================
# No. Python does not support native method overloading.
# If you write two methods with the exact same name inside a class,
# Python will simply overwrite (replace) the first one with the second one.
# Only the last defined method will survive!

class Demo:
    def greet(self):
        print("Hello")

    # Python overwrites the first greet() with this one!
    def greet(self, name):
        print(f"Hello {name}")


# --- Testing Demo ---
d = Demo()

# d.greet()  <-- This would CRASH! Python forgot the first greet() method entirely.
d.greet("Aadarsh")  # Works! Output: Hello Aadarsh


# =====================================================================
# 2. WHY IS METHOD OVERLOADING NOT AVAILABLE IN PYTHON?
# =====================================================================
# There are two core reasons built into how Python was designed:
#
# REASON 1: Methods are treated like variables
# In Python, methods are treated like regular variables holding function objects.
# Just like writing x = 10 and then x = 20 overwrites 10 with 20,
# defining a second method named 'greet' overwrites the first 'greet'.
# Python stores the function name in a lookup dictionary, and a key
# can only hold one value at a time.
#
# REASON 2: Python is Dynamically Typed (No Static Signatures)
# In languages like Java or C++, the compiler checks data types beforehand
# (like int, String) to know which version of a function to call.
# Python is dynamically typed—it doesn't enforce parameter data types at compile time.
# Because every variable is evaluated at runtime, Python's execution engine
# cannot distinguish between two methods based on their argument types alone.
