# =====================================================================
# PUBLIC, "PROTECTED", AND PRIVATE MEMBERS IN PYTHON
# =====================================================================

class BankAccount:
    def __init__(self, owner, balance, pin):
        
        # 1. PUBLIC MEMBER (No underscores)
        # Fully accessible from anywhere—inside or outside the class.
        self.owner = owner

        # 2. "PROTECTED" MEMBER (Single underscore prefix: '_')
        # NOTE: Python doesn't have true hard-enforced protected variables!
        # This is just a developer convention (an honor system) meaning: 
        # "Treat this as internal. Avoid accessing it directly from outside."
        # However, Python WILL still let you access it if you try.
        self._balance = balance

        # 3. PRIVATE MEMBER (Double underscore prefix: '__')
        # Triggers "name mangling". Python actually alters the name behind 
        # the scenes to block direct access from outside the class.
        self.__pin = pin


# =====================================================================
# TESTING THE CODE IN YOUR IDE
# =====================================================================

account = BankAccount("Aadarsh", 1000, 1234)

# 1. Accessing Public Member (Works fine)
print(f"Owner: {account.owner}")  # Output: Aadarsh

# 2. Accessing "Protected" Member (Works because it's just a convention!)
print(f"Balance: {account._balance}")  # Output: 1000 (Python doesn't block this)

# 3. Accessing Private Member (Blocked by Python name mangling)
# print(account.__pin)  # <-- AttributeError! Python actively blocks direct access.