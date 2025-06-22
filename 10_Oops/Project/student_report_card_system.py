# Project Name: Student Report Card System
# 🔹 Objective: Use classes, objects, inheritance, encapsulation, and polymorphism to create a system that manages student data and calculates results.

# ✅ 1. Person (Base Class)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
class Student(Person): #Inheritance
    __marks = {} # Encapsulated
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def add_marks(self, subject, mark):
        if 0 <= mark <= 100:
            self.__marks[subject] = mark
        else:
            print("Invalid mark")
    
    def calculate_result(self):
        total_marks = sum(self.__marks.values())
        percentage = total_marks / len(self.__marks) if self.__marks else 0
        return f"Total Marks: {total_marks}, Percentage: {percentage:.2f}%"
    
    def show_report_card(self):
        self.show_info()
        print(f"Roll No: {self.roll_no}")
        
        for sub,mark in self.__marks.items():
            print(f"Subject: {sub}, Mark: {mark}")

        print(self.calculate_result())

s1 = Student("Bidhit",23,"BCA101")
s1.add_marks("Physics",75)
s1.add_marks("Math",95)
s1.add_marks("CSC",75)
s1.add_marks("Chemistry",80)
s1.add_marks("English",83)

s1.show_report_card()
