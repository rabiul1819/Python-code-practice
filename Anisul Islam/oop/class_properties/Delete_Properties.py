class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Ford",35)
print(p1.name)
del p1.age
print(p1.age)
