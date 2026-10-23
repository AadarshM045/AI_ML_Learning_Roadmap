class Animal:
    def speak(self):
        print("Animals dont speak")


class Humans:
    def speak(self):
        print("Humans Do speak")


obj1 = Animal()
obj2 = Humans()

obj1.speak()
obj2.speak()
