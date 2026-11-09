# =====================================================================
# POLYMORPHISM (Same method name in different, independent classes)
# =====================================================================

class Animal:
    def speak(self):
        print("Animals dont speak")


class Humans:
    def speak(self):
        print("Humans Do speak")


# --- Testing the Code ---
obj1 = Animal()
obj1.speak()  # Output: Animals dont speak

obj2 = Humans()
obj2.speak()  # Output: Humans Do speak
