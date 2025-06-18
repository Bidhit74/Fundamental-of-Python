# Python lunch fstring - version 3.6
name = "Bidhit"
print(f"My name is {name}")

# Math Inside f-string:
a = 5
b = 3
print(f"Sum is {a + b}")   # Sum is 8

# With Function:
def greet(name):
    return f"Hello, {name}!"

print(greet("Ravi"))   # Hello, Ravi!

# Formatting Numbers:
pi = 3.14159
print(f"Pi = {pi:.2f}")  # Pi = 3.14

# 🔹 Old Way vs f-string:
# Old way
print("Hello, {}".format(name))

# f-string way
print(f"Hello, {name}")

# Function Call inside f-string:
print(f"Length of 'Python' is {len('Python')}")
