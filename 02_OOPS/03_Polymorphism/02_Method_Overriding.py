# =====================================================================
# INHERITANCE AND METHOD OVERRIDING IN PYTHON
# =====================================================================

class Animal:
    a = 10  # Class variable belonging to the Parent class (Animal)

    def __init__(self, name):
        self.name = name  # Instance variable initialized for the object

    def details(self):
        print(f"Your name is {self.name}")


# Human inherits from Animal (Human is the Child, Animal is the Parent)
class Human(Animal):
    b = 5  # Class variable unique to the Child class (Human)

    def __init__(self, name):
        # super().__init__() calls the parent class (Animal) constructor
        # so we don't have to rewrite self.name = name.
        super().__init__(name)

    # -----------------------------------------------------------------
    # METHOD OVERRIDING:
    # When a child class defines a method with the exact same name as
    # a method in its parent class, the child's version OVERRIDES
    # (replaces/takes precedence over) the parent's version.
    # -----------------------------------------------------------------
    def details(self):
        print(f"Your info is {self.name} this is all we have")


# =====================================================================
# TESTING THE CODE
# =====================================================================

# Creating an object of the child class (Human) passing "Aadarsh"
obj = Human("Aadarsh")

# Accessing class variable 'a' which is inherited from the parent (Animal)
print(obj.a)  # Output: 10

# Accessing class variable 'b' which belongs to the child class (Human)
print(obj.b)  # Output: 5

# Calling the details method:
# Because of Method Overriding, this runs the Human class's version
# of 'details', completely overriding the Animal class's version.
obj.details()  # Output: Your info is Aadarsh this is all we have
