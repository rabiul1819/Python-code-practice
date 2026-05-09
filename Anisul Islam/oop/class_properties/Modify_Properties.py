class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Reham",5)
print(p1.name)
p1.age = 6
print(p1.age)