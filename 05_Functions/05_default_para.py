# Question 5 - Default parameter value.
# Statement: Write a function that greets a user. if no name is provided, it should greet with default name.


def greet(name = "Bidhit"):
   return "Hello, " + name + " !"

print(greet())
print(greet("Binit"))