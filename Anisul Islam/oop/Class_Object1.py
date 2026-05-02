class Student:
    name = ""
    roll =""
    GPA= ""
Reham = Student()
print(isinstance(Reham, Student))
Reham.name = "Reham"
Reham.roll = 101
Reham.GPA = 3.99

print(f"Name:{Reham.name}\nRoll:{Reham.roll} \nGPA:{Reham.GPA}")
