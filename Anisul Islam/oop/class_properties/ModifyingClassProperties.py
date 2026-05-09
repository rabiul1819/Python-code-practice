class Person:
    lastName = ""
    def __init__(self, name):
        self.name = name
p1 = Person("A")
p2 = Person("B")

Person.lastName = "Refsnes"
print(p1.lastName)
print(p2.lastName)

print("Ata ami bujini")

