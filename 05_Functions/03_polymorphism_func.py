# Question 3 - Polymorphism in function
# Statement: Write a function multiply that multiplies two numbers, but can also accept string and multiply strings.

def multiply(a,b):
   return (a * b) 

print(multiply(20,35))
print(multiply("B", 5)) # Python By default use karta hai polymorphism
print(multiply(5, 'B')) # Python By default use karta hai polymorphism