# =====================================================================
# *ARGS AND **KWARGS IN PYTHON FUNCTIONS
# =====================================================================
# These special syntax tools are used when you don't know ahead of time
# how many arguments will be passed into your function. They allow your
# functions to accept a flexible, variable number of inputs.


# =====================================================================
# 1. *ARGS (Arbitrary Positional Arguments)
# =====================================================================
# The asterisk (*) collects any number of extra positional arguments
# passed into the function and packs them all together into a TUPLE.
# Note: The name 'args' is just a convention; the asterisk (*) is what matters.

def sum_all_numbers(*args):
    # 'args' is now a tuple containing all the passed numbers: (1, 2, 3, 4, 5)
    print(f"Tuple of args: {args}")

    total = 0
    for num in args:
        total += num
    return total


# --- Testing *args ---
print("--- Testing *args ---")
result1 = sum_all_numbers(1, 2, 3)
print(f"Sum 1: {result1}")  # Output: 6

result2 = sum_all_numbers(10, 20, 30, 40, 50)
# Output: 150 (We can pass as many arguments as we want!)
print(f"Sum 2: {result2}")


# =====================================================================
# 2. **KWARGS (Arbitrary Keyword Arguments)
# =====================================================================
# The double asterisk (**) collects any number of extra keyword (named)
# arguments and packs them together into a DICTIONARY (key-value pairs).
# Note: The name 'kwargs' is a convention; the double asterisk (**) is what matters.

def print_user_profile(**kwargs):
    # 'kwargs' is now a dictionary containing all named arguments passed in
    print(f"Dictionary of kwargs: {kwargs}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")


# --- Testing **kwargs ---
print("\n--- Testing **kwargs ---")
print_user_profile(name="Aadarsh", age=22, city="Kathmandu", role="Developer")
