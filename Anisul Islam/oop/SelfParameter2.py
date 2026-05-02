class Person:
    def __init__(self,name):
        self.name=name
    def printName(self):
        print(self.name)
p1= Person("Rama")
p2= Person("Sama")
p1.printName()
p2.printName()