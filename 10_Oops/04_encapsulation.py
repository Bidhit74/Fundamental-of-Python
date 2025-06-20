# Question 4: Encapsulation
# Statement: Modify the Car class to encapsulate the brand attribute,making it private, and provide a getter method for it.

class Car:
    def __init__(self,brand,model): # Constructor
        self.__brand = brand # __brand this privat only access class not object
        self.model = model

    def display(self):
        return f"Barand Name: {self.__brand} and model:- {self.model}"
    
    def get_brand(self):
        return self.__brand
    
    def set_brand(self,newBrand):
        self.__brand = newBrand
    
my_car = Car("Toyota","Carolla")
# print(my_car.__brand) # not access this is private # throw error - AttributeError
print(my_car.get_brand()) # now access
print(my_car.display()) 

my_car.set_brand("Tesla") # modify brand name
print(my_car.get_brand()) # now print new brand
print(my_car.display()) 
