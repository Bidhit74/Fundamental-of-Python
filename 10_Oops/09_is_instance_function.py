# Question 9: Class inheritance and isinstance() function
# Statement: Demonstrate the use of isinstance() to check if my_tesla in instance of Car and ElectricCar.

class Car:
    def __init__(self,brand,model): # Constructor
        self.brand = brand
        self.model = model

    def display(self):
        return f"Barand Name: {self.brand} and model:- {self.model}"


# Inheritance
class ElectricCar(Car): # inheritance
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_car = Car("Toyota","Carolla")
my_tesla = ElectricCar("Tesla","Model S","85kWh")

print(isinstance(my_car,Car)) # True
print(isinstance(my_tesla,Car)) # True
print(isinstance(my_car,ElectricCar)) # False
print(isinstance(my_tesla,ElectricCar)) # True

print(issubclass(ElectricCar,Car)) # True # ElectricCar sub class of Car
print(issubclass(Car,ElectricCar)) # False # Car does not sub class of ElectricCar
