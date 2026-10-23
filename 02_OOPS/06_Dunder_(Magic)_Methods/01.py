# # =====================================================================
# # DUNDER (MAGIC) METHODS IN PYTHON
# # =====================================================================
# # "Dunder" stands for **Double Underscore** (because they start and end
# # with two underscores, like `__init__`).
# #
# # What are they?
# # They are special built-in methods in Python that allow your custom classes
# # to hook into Python's native operations and built-in functions (like print(),
# # len(), +, etc.). You don't usually call them directly; Python calls them
# # automatically behind the scenes when certain actions happen.

# class Book:
#     def __init__(self, title, author, pages):
#         # 1. __init__ is the most common dunder method (Constructor)
#         # Automatically called when you create a new object from the class.
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         # 2. __str__ controls how the object is displayed when converted
#         # to a string (such as when you pass it to print()).
#         # Without this, print(obj) would just show a messy memory address like <__main__.Book object at 0x...>
#         return f"'{self.title}' by {self.author}"

#     def __len__(self):
#         # 3. __len__ allows your object to work with Python's built-in len() function!
#         # It defines what "length" means for your custom object (in this case, total pages).
#         return self.pages

#     def __add__(self, other):
#         # 4. __add__ overrides the addition operator (+) so you can add
#         # two custom objects together! Here, we add the pages of two books.
#         return self.pages + other.pages


# # =====================================================================
# # TESTING DUNDER METHODS IN YOUR IDE
# # =====================================================================

# # Creating two Book objects (triggers __init__)
# book1 = Book("Python Crash Course", "Eric Matthes", 544)
# book2 = Book("Fluent Python", "Luciano Ramalho", 1014)

# # 1. Using __str__
# # When we print 'book1', Python automatically looks for the __str__ method.
# print(book1)  # Output: 'Python Crash Course' by Eric Matthes

# # 2. Using __len__
# # Python automatically calls the __len__ method we defined above.
# print(f"Pages in Book 1: {len(book1)}")  # Output: Pages in Book 1: 544

# # 3. Using __add__
# # Using the '+' operator between two Book objects automatically triggers __add__.
# total_pages = book1 + book2
# print(f"Total pages of both books: {total_pages}")  # Output: Total pages of both books: 1558

print(dir(list))
