# =====================================================================
# PYTHON ABSTRACTION (USING THE ABC MODULE)
# =====================================================================
# 1. DOES PYTHON HAVE NATIVE ABSTRACTION?
# No. Abstraction does not natively exist as a built-in keyword in Python's
# core syntax. However, Python allows us to achieve true abstraction by
# importing the built-in 'abc' (Abstract Base Classes) module/library.
#
# 2. WHAT IS ABSTRACTION?
# Abstraction is used to simplify complex systems by focusing on essential
# features and hiding unnecessary details. It defines a strict blueprint
# or common interface that forces child classes to implement specific methods.

from abc import ABC, abstractmethod

# 3. Abstract Base Class (The Blueprint/Enforcer)
# Inheriting from 'ABC' makes this an abstract class.
# You CANNOT create objects directly from an abstract class.


class enforce(ABC):

    # Abstract Method
    # This has no body (uses 'pass'). Any child class MUST provide
    # its own version of this method, or Python will throw an error at startup.
    @abstractmethod
    def enginestart(self):
        pass


# 4. Concrete Child Classes
# Each child class inherits from 'enforce' and implements the required 'enginestart' method.

class Car(enforce):
    def enginestart(self):
        print("Car engine started with a push button.")


class Bike(enforce):
    def enginestart(self):
        print("Bike engine started with a self-start button.")


class Truck(enforce):
    def enginestart(self):
        print("Truck engine started with a heavy key turn.")


# =====================================================================
# TESTING THE CODE IN YOUR IDE
# =====================================================================

# Note: Writing `obj = enforce()` here would crash immediately
# because Python prevents you from instantiating an abstract class!

obj1 = Car()
obj2 = Bike()
obj3 = Truck()

obj1.enginestart()  # Output: Car engine started with a push button.
obj2.enginestart()  # Output: Bike engine started with a self-start button.
obj3.enginestart()  # Output: Truck engine started with a heavy key turn.
