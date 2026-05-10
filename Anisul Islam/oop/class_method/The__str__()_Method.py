'''
# without __str__ method
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Reham",5)
print(p1)
'''
#with __str__ method
class Person:
    def __init__(self,name,age):

        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
p1 = Person("Reham",5)
print(p1)