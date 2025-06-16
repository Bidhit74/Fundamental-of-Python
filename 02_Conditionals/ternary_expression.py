# A ternary expression is a one-line if-else statement used for conditional assignment.
# value_if_true if condition else value_if_false

# Example of a ternary expression
age = 20
message = "You are an adult." if age >= 18 else "You are a minor."

print(message)  # Output: You are an adult.
# Another example with a different condition
temperature = 30
weather = "It's hot outside." if temperature > 25 else "It's cool outside."
print(weather)  # Output: It's hot outside.
# Using a ternary expression to assign a value based on a condition  
is_even = False
number = 3
result = "Even number" if is_even else "Odd number"
print(result)  # Output: Odd number

# Using in a function
def check_number(num):
   return "Positive" if num > 0 else "Negative or Zero"
print(check_number(5))  # Output: Positive
print(check_number(-3))  # Output: Negative or Zero

# Example with a list comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x**2 if x % 2 == 0 else x for x in numbers]
print(squared)  # Output: [1, 4, 3, 16, 5]
# Using a ternary expression with a function call