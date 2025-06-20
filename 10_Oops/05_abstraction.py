# Abstraction : Abstraction ka matlab hai complex cheezein chhupana aur sirf important cheezein dikhana.

# 🔹 Real-Life Example:
# Car: You use the steering, gear, brake — but you don’t see the engine’s internal working.

# Python supports abstraction using:
# from abc import ABC, abstractmethod
# ABC: Abstract Base Class
# @abstractmethod: Method jiska body child class me banaya jaata hai.

from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):  # Abstract method
        pass

class Circle(Shape):  # Concrete class
    def area(self):
        return 3.14 * 5 * 5

c = Circle()
print(c.area())

