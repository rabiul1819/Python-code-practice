from abc import ABC,abstractmethod


class shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    @abstractmethod
    def area(self):#abstract class
        pass

class triangle(shape):
    def area(self):
        area =.5 * self.dim1 * self.dim2
        print("Area of triangle is = ", area)

class rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of rectangle is = ", area)


t1= triangle(20,30)
t1.area()
r1= rectangle(20,30)
r1.area()