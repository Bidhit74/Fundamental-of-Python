# Question 7 - Static method - Access only Class not intance of class
# Statement: Add a static method to Car class that returns a general description of a car.

class Car:
    track_car = 0
    def __init__(self,brand,model): # Constructor
        self.brand = brand 
        self.model = model
        Car.track_car += 1

    @staticmethod # Static Method
    def general_description():
        return "Cars are means of transport."



my_car1 = Car("Tata","Safari")
my_car2 = Car("Tata","Nexon")

# print(my_car1.general_description()) # not access static method
print(Car.general_description())
