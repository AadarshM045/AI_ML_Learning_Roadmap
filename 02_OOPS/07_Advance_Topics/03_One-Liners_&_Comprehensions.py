# =====================================================================
# ONE-LINERS & COMPREHENSIONS IN PYTHON
# =====================================================================
# Comprehensions and one-liners allow you to write concise, highly
# readable, and efficient code to create collections (lists, dicts, sets)
# or execute short logic without writing multi-line loops.


# =====================================================================
# 1. LIST COMPREHENSIONS
# =====================================================================
# Syntax: [expression for item in iterable if condition]

# --- Example A: Basic List Comprehension (Square of numbers 1 to 5) ---
# Traditional way:
# squares = []
# for i in range(1, 6):
#     squares.append(i**2)

squares = [i**2 for i in range(1, 6)]
print(f"Squares: {squares}")  # Output: [1, 4, 9, 16, 25]


# --- Example B: List Comprehension with a Condition (Filtering Evens) ---
# Only keeps numbers where `num % 2 == 0` is True
evens = [num for num in range(1, 11) if num % 2 == 0]
print(f"Even numbers: {evens}")  # Output: [2, 4, 6, 8, 10]


# --- Example C: List Comprehension with If-Else (Ternary inside) ---
# If the number is even, keep it; if odd, label it "Odd"
labeled_numbers = [num if num % 2 == 0 else "Odd" for num in range(1, 6)]
print(f"Labeled: {labeled_numbers}")  # Output: ['Odd', 2, 'Odd', 4, 'Odd']


# =====================================================================
# 2. DICTIONARY COMPREHENSIONS
# =====================================================================
# Syntax: {key_expr: value_expr for item in iterable if condition}

# Creating a dictionary mapping numbers to their cubes
numbers = [1, 2, 3, 4, 5]
cubes_dict = {num: num**3 for num in numbers}
# Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
print(f"Cubes Dict: {cubes_dict}")


# =====================================================================
# 3. SET COMPREHENSIONS
# =====================================================================
# Syntax: {expression for item in iterable if condition}
# Automatically drops duplicate values because sets only store unique items.

text = "programming"
unique_vowels = {char for char in text if char in "aeiou"}
# Output: {'o', 'a'} (unordered set)
print(f"Unique vowels found: {unique_vowels}")


# =====================================================================
# 4. LAMBDA FUNCTIONS (Anonymous One-Liner Functions)
# =====================================================================
# Syntax: lambda arguments: expression
# Used for creating small, throw-away functions without using the `def` keyword.

# Regular function vs Lambda equivalent:
# def add(a, b): return a + b

def add_lambda(a, b): return a + b


print(f"Lambda Addition: {add_lambda(10, 5)}")  # Output: 15

# Often used with built-in functions like `sorted()` or `map()`:
students = [("Aadarsh", 85), ("Rahul", 92), ("Priya", 78)]
# Sort students based on their score (index 1 of the tuple)
sorted_students = sorted(
    students, key=lambda student: student[1], reverse=True)
print(f"Sorted Students by Score: {sorted_students}")


# =====================================================================
# 5. TERNARY OPERATORS (Inline If-Else One-Liner)
# =====================================================================
# Syntax: value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")  # Output: Adult
