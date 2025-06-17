# A set is mutable and an unordered, unindexed collection of unique elements in Python.
# 🔹 Real-Life Use Case: Unique students who attended class:
'''
my_set = {"Bidhit", "Aman", "Rita", "Bidhit"}
print(type(my_set)) # set
print(my_set) # {'Aman', 'Rita', 'Bidhit'}

# other way create set - using set()
# s1 = set([1,2,3,3,2]) 
# or
val = (1,2,3,3,2)
s1 = set(val)
print(s1) 
print(type(s1)) # set
print(val)
print(type(val)) # tuple

# 'in' and 'not in' use in set
my_set = {"Bidhit", "Aman", "Rita"}
print("Bidhit" in my_set) # True
print("Bidhit" not in my_set) # False
'''

'''
# 🔹 1. add() : Adds an item to the set.
s = {1, 2}
s.add(3)
print(s)  # {1, 2, 3}

# 🔹 2. remove() & discard()
# remove(): Deletes item (gives error if item not found).
# discard(): Deletes item (no error if item not found).
s = {1, 2, 3}
s.remove(2)
# s.remove(4) # error - KeyError
s.discard(5)  # no error
s.discard(1)
print(s)  # {3}

# # 🔹 3. pop() :- Removes and returns a random item.
s = {10, 20, 30}
x = s.pop()
print(x)  # Randomly 10 or 20 or 30

# # 🔹 4. clear() :- Removes all elements from set.
s = {1, 2, 3}
s.clear()
print(s)  # Output: set()

# # 🔹 5. union() :- Combines elements from both sets (removes duplicates).
a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3} # no duplicate value
# | - logical or  operator
print(a | b)  # {1, 2, 3} # no duplicate value

# # 🔹 6. intersection() :- Returns common elements from both sets.
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}
# & - Logical and operator
print(a & b)

# # 🔹 7. difference() :- Items present in one set but not in another.
a = {1, 2, 3}
b = {2, 4}
print(a.difference(b))  # {1, 3}
print(a - b)  # {1, 3}

# # 🔹 8. issubset() & issuperset()
# # A.issubset(B): A is fully inside B.
# # A.issuperset(B): A contains all elements of B.
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))   # True
print(b.issubset(a))   # False
print(b.issuperset(a)) # True
print(a.issuperset(b)) # False

# Symmetric difference
a = {1, 2, 3}
b = {2, 4}

print(a.symmetric_difference(b)) # {1, 3, 4} # all uncomman element print
print(a ^ b) # {1, 3, 4} # all uncomman element print
'''

# Set Iteration
# Using for loops
numbers = {1,2,3,4,5}

for num in numbers:
    print(num, end=" ")

# Using while loops - first convert set to list then use while loop because sets do not support indexing.

# set comprehensions
# syntax
# new_set = {expression for item in iterable if condition}
print()
square = {x ** 2 for x in range(1, 6)}
print(square) # {1, 4, 9, 16, 25}

# 🔹 Real-Life Use Case: When you need a constant set of values (e.g., permanent settings, roles, categories). To use as a dictionary key (normal sets can’t be used as keys).
# A frozenset is an immutable set – once created, you cannot change it.


fs = frozenset([1, 2, 3])
print(fs)              # Output: frozenset({1, 2, 3})
print(2 in fs)         # True
print(fs.union([4]))   # frozenset({1, 2, 3, 4})
# set functions like union, intersection, difference can be used with frozensets.

# ❌ These will give error:
# fs.add(5)      # Error: 'frozenset' object has no attribute 'add'
# fs.remove(1)   # Error