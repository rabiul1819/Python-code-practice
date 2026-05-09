class Bike:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def __str__(self):
        return f'{self.name} {self.color}'

    def display(self):
        print(f"Name: {self.name}, Color: {self.color}")
Bike1=Bike("Yamaha V3",'Black')
Bike2=Bike("Yamaha V3",'Black')

print(Bike1)
print(Bike2)
print(Bike1==Bike2)