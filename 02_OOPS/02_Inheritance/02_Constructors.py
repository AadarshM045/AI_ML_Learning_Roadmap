class BagFactory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def details(self):
        print("The details of the bags are:")
        print(self.material)
        print(self.zips)
        print(self.pockets)
        print(self.color)


class Rebook(BagFactory):
    def __init__(self, material, zips, pockets, color):
        super().__init__(material, zips, pockets)
        self.color = color

    def details(self):
        print(self.color)
        return super().details()


Bag1 = BagFactory("Polyster", 4, 6)

Bag2 = Rebook("Stars", 3, 6, "Red")
Bag2.details()
