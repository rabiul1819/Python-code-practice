'''
class Student:
    roll=""
    gpa =""
    def set_value(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"Roll: {self.roll} GPA: {self.gpa}")

nime = Student()
nime.set_value(101,6)
nime.display()


lily = Student()
lily.set_value(102,"60")
lily.display()
'''

# constructor
class Student:
    roll=""
    gpa =""
    def __init__(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"Roll: {self.roll} GPA: {self.gpa}")

nime = Student(101,3.89)
nime.display()


lily = Student(102,3.40)
lily.display()