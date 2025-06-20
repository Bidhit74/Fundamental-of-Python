# Question 5 - Polymorphism - Same name and work different
# Statement: Demonstrate polymorphism by defing a method fuel_type in both Car and ElectricCar classes, but with different behaviours

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fuel_type(self): 
        return "Petrol or Diesel"
    
class ElectricCar(Car): # Inherit class Car
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self): # Function Overriding (Inheritance)
        return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model", "85kWh")
# print(my_tesla.fuel_type())
# my_car = Car("Toyota","Carolla")
# print(my_car.fuel_type())

# Type of polymorphism:  2. Duck Typing (No need to check type)
class Cat:
    def speak(self):
        print("Meow")

class Person:
    def speak(self):
        print("Hello")

def call_speak(obj):
    obj.speak()

call_speak(Cat())     # Meow
call_speak(Person())  # Hello
#  call_speak() function sabhi objects ke liye kaam karta hai jisme speak() method hai.

# Type of polymorphism🔹 3. Built-in Polymorphism (Operator Overloading)

print(2 + 3)           # 5 → addition
print("A" + "B")       # AB → string join
print([1, 2] + [3, 4]) # [1, 2, 3, 4] → list merge

# ✅ Same operator +, different behavior based on data type.



