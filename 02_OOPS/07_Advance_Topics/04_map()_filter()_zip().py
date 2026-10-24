# =====================================================================
# MAP, FILTER, AND ZIP IN PYTHON
# =====================================================================
# These are powerful built-in utility functions used to process and
# manipulate collections (like lists and tuples) efficiently without
# writing long, traditional `for` loops.


# =====================================================================
# 1. MAP (Transforming Every Item in an Iterable)
# =====================================================================
# Syntax: map(function, iterable)
# What it does: Applies a given function to every single item in an iterable
# (like a list) and returns a 'map object' (an iterator) which we usually
# convert into a list using list().

numbers = [1, 2, 3, 4, 5]

# Using map with a lambda function to square every number in the list
# Traditional way: squares = [x**2 for x in numbers]
squared_numbers = list(map(lambda x: x**2, numbers))

print(f"Original numbers: {numbers}")
# Output: [1, 4, 9, 16, 25]
print(f"Squared numbers (using map): {squared_numbers}")


# =====================================================================
# 2. FILTER (Filtering Items Based on a Condition)
# =====================================================================
# Syntax: filter(function, iterable)
# What it does: Tests every item in an iterable against a boolean function
# (a function that returns True or False). It keeps the item only if the
# function evaluates to True.

scores = [45, 82, 60, 95, 30, 78]

# Using filter with a lambda function to keep only scores >= 60 (Passing grades)
# Just for comparison, returns booleans
passing_scores = list(map(lambda x: x >= 60, scores))
# Real filter usage:
passed_students = list(filter(lambda score: score >= 60, scores))

print(f"\nAll scores: {scores}")
# Output: [82, 60, 95, 78]
print(f"Passing scores (using filter): {passed_students}")


# =====================================================================
# 3. ZIP (Combining Multiple Iterables Together)
# =====================================================================
# Syntax: zip(iterables)
# What it does: Takes multiple lists (or other iterables) and combines them
# element-by-element into tuples. It stops as soon as the shortest list runs out.

names = ["Aadarsh", "Rahul", "Priya"]
marks = [85, 92, 78]
cities = ["Kathmandu", "Pokhara", "Lalitpur"]

# Combining three lists side-by-side
combined = list(zip(names, marks, cities))

print(f"\nZipped Data: {combined}")
# Output: [('Aadarsh', 85, 'Kathmandu'), ('Rahul', 92, 'Pokhara'), ('Priya', 78, 'Lalitpur')]

# --- Bonus: Zipping into a Dictionary ---
# You can easily combine two lists (Keys and Values) into a dictionary using dict(zip())
student_dict = dict(zip(names, marks))
print(f"Zipped Dictionary: {student_dict}")
# Output: {'Aadarsh': 85, 'Rahul': 92, 'Priya': 78}
