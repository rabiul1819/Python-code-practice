class Person:
    def __init__(self,name):
        self.name = name
    def greet(self):
        return "Hello " + self.name
    def welcome(self):
        message = self.greet()
        print( message + " Welcome my code")
p1 = Person("Ryan")
p1.welcome()