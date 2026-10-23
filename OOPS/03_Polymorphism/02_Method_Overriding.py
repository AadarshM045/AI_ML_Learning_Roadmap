class Animal:
    a = 10

    def __init__(self, name):
        self.name = name

    def details(self):
        print(f"Your name is {self.name}")


class Human(Animal):
    b = 5

    def __init__(self, name):
        super().__init__(name)

    def details(self):
        print(f"Your info is {self.name} this is all we have")


obj = Human("Aadarsh")
print(obj.a)
print(obj.b)
obj.details()
