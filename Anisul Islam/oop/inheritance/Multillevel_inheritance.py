'''
class A:
    def display1(self):
        print("I am from A class")

class B(A):
    def display2(self):
        print("I am from B class")

class C(B):
    #display1 and display2
    def display3(self):
        print("I am from C class")

obj = C()
obj.display1()
obj.display2()
obj.display3()
print("---------------------------")
obj1 = B()
obj1.display1()
obj1.display2()
print("---------------------------")
obj2 = B()
obj2.display1()
'''
#update version
class A:
    def display1(self):
        print("I am from A class")

class B(A):
    def display2(self):
        super().display1()
        print("I am from B class")

class C(B):
    #display1 and display2
    def display3(self):
        super().display1()
        super().display2()
        print("I am from C class")
obj1 = C()
obj1.display3()
print("---------------------------")
obj2 =B()
obj2.display2()


