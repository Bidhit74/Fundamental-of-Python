# Question 8:- Property Decorators
# Statement: Use a property decorator in the Car class to make the model atrribute read_only.
class Car:
    track_car = 0
    def __init__(self,brand,model): 
        self.brand = brand 
        self.__model = model
        Car.track_car += 1

    @property # now you cal this method like property
    def my_model(self):
        return self.__model

my_car1 = Car("Tata","Safari")
# print(my_car1.model)
# my_car1.my_model = "Nexon" # modify/change model 
# print(my_car1.model)

# my_car1.my_model = "Nexon" # Not possible modify/change model 
print(my_car1.my_model) # now you are cal this method like property

