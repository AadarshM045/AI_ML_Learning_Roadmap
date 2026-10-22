class Bags:
    def __init__(self, Materials, Zips, Pockets):
        self.Materials = Materials
        self.Zips = Zips
        self.Pockets = Pockets


reebok = Bags("polyster", 4, 6)
campus = Bags("Leather", 2, 8)

print(reebok.Materials)
print(campus.Materials)
