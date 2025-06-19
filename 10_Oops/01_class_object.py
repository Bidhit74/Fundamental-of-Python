# Question 1: Basic Class and Object
# Statement: Create a Car class with attributes like brand, model. Then create an instance of the class.

# Class is a blueprint of objects

class Car:
    def __init__(self,brand,model): # Constructor
        self.brand = brand
        self.model = model


my_car = Car("Toyota","Carolla")
print(my_car.brand)
print(my_car.model)

my_car1 = Car("TATA","Safari")
print(my_car1.brand)
print(my_car1.model)

