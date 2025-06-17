'''
t1 = (1,2,3,4,5)
t2 = 1,2,3,4,5  # without () is tuple
print(t1)
print(t2)
print(type(t2)) # tuple
t3 = (5) # single value not a tuple
print(type(t3)) # int
t4 = (5,) # now tuple use ,
print(type(t4)) # tuple
t5 = () # empty tuple
print(type(t5)) # tuple

t6 = tuple("Bidhit") # ('B', 'i', 'd', 'h', 'i', 't')
print(t6)
'''

'''
# List
my_list = [1, 2, 3]
my_list.append(4)   # Allowed
print(my_list)

# Tuple
my_tuple = (1, 2, 3)
# my_tuple.append(4)  # ❌ Not Allowed – gives error

# Tuple Unpacking :  Assigning values from a tuple directly to variables.
#  Number of variables must match number of items in the tuple.
person = ("Bidhit", 22, "India")
name, age, country = person

print(name)     # Output: Bidhit
print(age)      # Output: 22
print(country)  # Output: India

# Nested Tuple
nested = (("apple", "banana"), (1, 2, 3))

print(nested[0])       # Output: ("apple", "banana")
print(nested[0][1])    # Output: banana
print(nested[1][2])    # Output: 3

'''

'''
# General in buit function support tuple
t1 = (1,2,3,40,5)
print(len(t1)) # 5
print(max(t1)) # 40
print(min(t1)) # 1
print(sum(t1)) # 51
print(t1.index(40)) # index 40 = 3
t2 = tuple("Bidhit")
print(t2.count("i")) # count of i = 2
'''
'''
# Tuble accesing like list
t3 = ('B', 'i', 'd', 'h', 'i', 't')
print(t3[0]) # positive indexing # B
print(t3[2]) # positive indexing # d
print(t3[-1]) # negetive indexing # t
print(t3[-3]) # negetive indexing # h
print(t3[2:5])# slecing like list # ('d', 'h', 'i')
'''
'''
# Operation perform
t1 = (1,2,3)
t2 = (3,4,5)
t3 = t1 + t2 # join operation or concatanation
t4 = t1 * 3 # Repete 3 times
print(t3) # (1, 2, 3, 3, 4, 5)
print(t4) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
'''

'''
# Sort function use but tuble not support can you do this
t1 = (3,4,5,1,2,7,6,9,8)
print(t1)
l1 = list(t1) # list use sort in buit function
print(l1) 
l1.sort()
print(l1)
t1 = tuple(l1)
print(t1) 
'''

'''
# zip function - in built function in python
# zip() combines two or more sequences (like lists/tuples) element-wise into a sequence of tuples.
# zip - pair banata hai
names = ("Ram", "Shyam", "Mohan")
scores = (85, 90, 78)

combined = zip(names,scores)
print(list(combined)) # [('Ram', 85), ('Shyam', 90), ('Mohan', 78)]

#  Tuple Unpacking with zip():
pairs = [('Ram', 85), ('Shyam', 90), ('Mohan', 78)]

for name,score in pairs:
    print(f"Name:- {name} and Score:- {score}")

# 🔹 Unzipping: * operator is used to unpack the zipped list of tuples.
names, scores = zip(*pairs)
print(names) # ('Ram', 'Shyam', 'Mohan')
print(scores) #(85, 90, 78)
'''

# enumerate() + zip() in Python (with Tuple Unpacking)
# enumerate() adds a counter (index) to an iterable.
fruits = ["apple", "banana", "mango"]

for index,fruit in enumerate(fruits):
    print(index, ": " + fruit)

# 0 : apple
# 1 : banana
# 2 : mango

# 🔹 2. zip() + enumerate() Together
# Use Case: When you want both index and paired values from multiple lists.

names = ["Ram", "Shyam", "Mohan"]
marks = [85, 90, 78]

names_marks = list(zip(names,marks))

for i, (name,score) in enumerate(names_marks):
    print(i, "- Name:- ", name, " Score:- ", score)