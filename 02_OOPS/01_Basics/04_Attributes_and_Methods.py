class user:
    # A class variable shared by all instances
    base_role = "Guest"

    def __init__(self, username):
        self.username = username  # Object/Instance Attributes

    def introduce(self):  # Instance/Object Method captures the location of Object
        print(f"Hello, I am {self.username}")

    @classmethod
    def change_base_role(cls, new_role):  # Class Method Contains the Location of class
        cls.base_role = new_role

    @staticmethod
    def hello():
        print("Hello i am a static Method")


Role = user("Guest")
Role.introduce()
# user.change_base_role("Member")
Role2 = user("Member")
Role2.introduce()
