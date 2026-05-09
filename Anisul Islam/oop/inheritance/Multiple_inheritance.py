
#update version
class A:
    def display(self):
        print("I am from A class")

class B:
    def display(self):
        print("I am from B class")

class C(B,A):# j class age seta ashbe
   pass

obj1 = C()
obj1.display()



