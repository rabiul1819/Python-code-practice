class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print('Hello,My name is ',self.name)
p1=Person('Rony',20)
p1.greet()