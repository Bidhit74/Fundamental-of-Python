# Question 10: Multiple Inheritance
# Statement: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demostrating multiple inheritance


class Car:
    def __init__(self,brand,model): # Constructor
        self.brand = brand
        self.model = model

    def display(self):
        return f"Barand Name: {self.brand} and model:- {self.model}"


class Battery:
    def battery_info(self):
        return 'This is battery.'

class Engine:
    def engine_info(self):
        return 'This is engine.'
    
# multiple inheritance
class ElectricCar(Car,Battery,Engine): 
    pass

my_car = ElectricCar("Tesla","Model S") # Access all class (Car,Battery,Engine)

print(my_car.battery_info())
print(my_car.engine_info())
print(my_car.brand)
print(my_car.model)
print(my_car.display())