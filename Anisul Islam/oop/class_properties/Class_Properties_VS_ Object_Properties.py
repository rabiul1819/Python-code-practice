class Person:
    species = "Human"
    def __init__(self, name):
        self.name = name
p1 = Person("Ray")
p2= Person("Rabi")
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)