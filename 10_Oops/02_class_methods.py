# Question 2: Class Method and self
# Statement :- Add a method to the Car class that displays the full name of the car(brand and model)/

class Car:
    def __init__(self,brand,model): # Constructor
        self.brand = brand
        self.model = model

    def display(self):
        return f"Barand Name: {self.brand} and model:- {self.model}"


my_car = Car("Toyota","Carolla")
print(my_car.display())