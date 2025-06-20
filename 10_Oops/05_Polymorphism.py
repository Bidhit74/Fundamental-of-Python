# Question 5 - Polymorphism - Same name and work different
# Statement: Demonstrate polymorphism by defing a method fuel_type in both Car and ElectricCar classes, but with different behaviours

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand
    
    def set_brand(self,new_brand):
        self.__brand = new_brand

    def display(self):
        print(f"Brand:- {self.__brand} and Model:- {self.model}")

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car): # Inherit class Car
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Tesla", "Model", "85kWh")
print(my_tesla.fuel_type())
my_car = Car("Toyota","Carolla")
print(my_car.fuel_type())

