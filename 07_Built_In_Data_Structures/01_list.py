'''
fruits = ['apple', 'banana', 'cherry', 'date']
numbers = [1,2,3,4,5]
mixed = [1,2, 'apple', 3,True,'data']
print(mixed)
# Heterogeous list : Item of different type
# Nested List : list can contain other list
nested_list = [1,2,[3,4],[5,7],[5,6,[2,5,6]]]
print(nested_list)

# len()
print(len(mixed))


# Membership (in, not in) : if an item exits within a list using the 'in' and not in operators
print('apple' in fruits) # True
print('apple' not in fruits) # false
'''

# Repitition (*)
list1 = [1,3,5]
print(list1*3) # [1, 3, 5, 1, 3, 5, 1, 3, 5]

# list Comprehension
square = [x**2 for x in range(5)]
print(square)

# Nested operation
nested = [[1,2,3],[4,5,6]]
flattend = [item for sublist in nested for item in sublist]
print(flattend)

# list deletion or remove operation perform
fruits = ['apple', 'banana', 'cherry', 'orange']
print(fruits)
fruits.remove("apple") # name base delete karte hai 
print(fruits)
del fruits[1] # yah index base delete karta
print(fruits)
fruits.pop() # last element delete
print(fruits)
fruits.clear() # complete delete or clear
print(fruits)


# Shuffle list
import random
l1 = [20,40,60,80,100]
random.shuffle(l1)
print(l1)
random.shuffle(l1)
print(l1)

# Max and Min function
print(max(l1))
print(min(l1))

# is 
A = 'RED'
B = 'RED' 
print(A is B) # True # String is same objects

l2 = ['A','B','C']
l3 = ['A','B','C']
print(l2 is l3) # False   #Even if two list are the same but python create two different objects 

l4 = ["Bidhit"]
l5 = ["Bidhit"]
print(l4 is l5) # False

name = "Bidhit"
li = list(name) 
print(li)