class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def displayInfo(self):
        print(f"Brand:{self.brand}\n Model:{self.model}\n Year:{self.year}")
Car1 = Car("Toyota",'Corolla',2020)
Car1.displayInfo()