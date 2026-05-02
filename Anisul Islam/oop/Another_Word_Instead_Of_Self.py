class Person:
    def __init__(myObject,name,age):
        myObject.name=name
        myObject.age=age
    def greet(abc):
        print("Hello! My name is ",abc.name)
p1 = Person("Ryan",3)
p1.greet()