x, y = 5, 10
print(x)  # 5
print(y)  # 10

# Advantage of simultaneous assignment:
# 1. It allows for swapping values without needing a temporary variable.
a, b = 1, 2
a, b = b, a
print(a, b)  # Output: 2 1

# 2. I can return multiple values from a function and assign them to multiple variables in one line.
def get_coordinates():
    return (3, 4)
x, y = get_coordinates()
print(x, y)  # Output: 3 4

# 3. It can be used to assign multiple variables in a single line.
def get_values():
    return 1, 2, 3
x, y, z = get_values()
print(x, y, z)  # Output: 1 2 3

# 4. It can be used to unpack values from a tuple or list.

value = [1,2,3]
a,b,c = value

print("a:", a)  # Output: a: 1
print("b:", b)  # Output: b: 2
print("c:", c)  # Output: c: 3
# 5. It can be used to unpack values from a dictionary. 
def get_dict():
    return {'x': 10, 'y': 20}
x, y = get_dict().values()
print(x, y)  # Output: 10 20

# 6. It can be used ingnore some values while unpacking.
# in this case, we can use an underscore (_) to ignore the values we don't need.
def get_mixed_values():
    return 1, 2, 3, 4
x, _, y, _ = get_mixed_values()
print(x, y)  # Output: 1 3