# Question 10 - Recursive Function
# Statement: Create a recursive function to calculate the factorial of a number.

"""  
def factorial(n):
   if(n==0): # base case
      return 1
   else:
      return n * factorial(n-1)
   

print(factorial(5))

"""

def fibonacci(n):
   if (n==0): # base case
      return 0
   elif(n==1): # base case
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2) # recursive case
   
print(fibonacci(6))