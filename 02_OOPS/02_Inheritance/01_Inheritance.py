# =====================================================================
# PYTHON INHERITANCE SUMMARY & NOTES
# =====================================================================
# - In Python, inheritance works between classes rather than
#   real-world entities like an old man and a child[cite: 1].
# - Inheritance allows a class (child class) to inherit properties
#   and behaviors (attributes and methods) from another class (parent class)[cite: 1].
# - Benefits of using inheritance[cite: 1]:
#     * Code reusability[cite: 1]
#     * Organized structure[cite: 1]
#     * Easy to maintain and extend[cite: 1]
# =====================================================================

class Animal:  # Parent Class
    a = 5

    def __init__(self, name):
        self.name = name

    def details(self):
        print(f"Hello your name is {self.name}")


class Human(Animal):  # Child Class
    pass


obj1 = Animal("Lion")
obj1.details()
obj2 = Human("Rohit")
obj2.details()
