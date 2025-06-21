# Question 6: Class Variable
# Statement: Add a class variable to Car that keeps track of the number of car created.


class Car:
    track_car = 0 # Variable
    def __init__(self,brand,model): # Constructor
        self.brand = brand 
        self.model = model
        Car.track_car += 1


    
my_car = Car("Toyota","Carolla")
my_car1 = Car("Tata","Safari")
my_car2 = Car("Tata","Nexon")

print("Total Car Created = ", Car.track_car) # 3
