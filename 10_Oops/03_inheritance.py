# Question: 3 - Inheritance
# Statement: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    def __init__(self,brand,model): # Constructor
        self.brand = brand
        self.model = model

    def display(self):
        return f"Barand Name: {self.brand} and model:- {self.model}"


my_car = Car("Toyota","Carolla")


# Inheritance
class ElectricCar(Car): # inheritance
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_electric_car = ElectricCar("Tesla", "Model S","85kWh")

print(my_electric_car.battery_size)
print(my_electric_car.brand)
print(my_electric_car.model)
print(my_electric_car.display())