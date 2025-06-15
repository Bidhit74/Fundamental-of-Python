x = True
y = False
# print(x and y)  # Logical AND # Both must be True 
# print(x or y)   # Logical OR  # At least one must be True
# print(not x)    # Logical NOT # Inverts the value of x
# print(x != y)   # Logical XOR (not equal)  # One is True, the other is False
# print(x == y)   # Equality check
# print(x is y)   # Identity check    
print(x is not y)  # Identity check (not equal) # True
print((x and y) or (not x))  # Combined logical expression  # False
print((x or y) and (not y))  # Another combined logical expression # True
print((x and not y) or (not x and y))  # XOR-like expression # True
