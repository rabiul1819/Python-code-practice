'''
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print("says Woof!")
d1 = Dog("Buddy",3)
print(d1.name)
print(d1.age)
print(d1.bark())
'''

# Create the Dog class
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    print(self.name + " says Woof!")

# Create an object
d1 = Dog("Buddy", 3)

# Call the bark method
d1.bark()