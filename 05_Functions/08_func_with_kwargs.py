# Question 8 - Function with **kwargs
# kwargs (Keyword Arguments)
# Statement: Create a function that accepts any number of keyword arguments and print them in the format key:value

# def print_kwargs(name, power):
#    print("Name: ", name, " Power: ", power)

# print_kwargs(name="Shaktiman", power="Laser")
# print_kwargs(power="Laser", name="Shaktiman") # flip karne ke baad bhi same wark karta hai
# print_kwargs("Shaktiman","Laser")
# print_kwargs("Laser","Shaktiman")


def print_kwargs(**kwargs):
   # print(kwargs) # return dictionaries
   # print(*kwargs) # return dictionaries key

   for key,value in kwargs.items():
      # print(key,value)
      print(f"{key}: {value}")

# print_kwargs("Shaktiman","Laser") # does not work 
print_kwargs(name="Shaktiman", power="Laser")
print_kwargs(name="Shaktiman")
print_kwargs(name="Shaktiman", power="Laser", enemy="Dr. Jackaal")
