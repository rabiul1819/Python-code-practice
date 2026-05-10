class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):

        self.age += 1
        print(f"Happy Birthday to you. You are now {self.age} years old")

p1 = Person("Reham",5)
p1.celebrate_birthday()
p1.celebrate_birthday()