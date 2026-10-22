class Animal:
    def __init__(self, name):
        self.name = name


class Humans:
    def __init__(self, id):
        self.id = id


class Robots(Humans, Animal):
    def __init__(self, id, name):
        Humans.__init__(self, id)
        Animal.__init__(self, name)


robo = Robots(15, "Chhiti")
