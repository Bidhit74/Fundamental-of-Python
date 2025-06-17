# Dictionaries are mutable, unordered collections of key-value pairs.
""""
# Dictionaries Creation 5 ways
# # 1. Using curly braces
# use case: All elements are known at the time of creation
chai_types1 = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_types1)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}

# 2. Using the dict() constructor
# Use Case:- When you want to create a dictionary from keyword arguments
chai_types2 = dict(Masala="Spicy", Ginger="Zesty", Green="Mild")
print(chai_types2)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}    

# 3. Using a list of tuples
# Use Case:- When you have a list of key-value pairs
chai_types3 = dict([("Masala", "Spicy"), ("Ginger", "Zesty"), ("Green", "Mild")])
print(chai_types3)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}

# 4. {}
chai_types4 = {}
# Use Case:- When you want to create an empty dictionary and add elements later
# This is useful when the elements are not known at the time of creation
chai_types4["Masala"] = "Spicy"
chai_types4["Ginger"] = "Zesty"
chai_types4["Green"] = "Mild"
print(chai_types4)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}

# 5. Using the zip() function
# Use Case:- When you have two lists, one for keys and one for values
keys = ["Masala", "Ginger", "Green"]
values = ["Spicy", "Zesty", "Mild"]
chai_types5 = dict(zip(keys, values))
print(chai_types5)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}

"""
"""
# Adding and Replacing Value
chai_types = {"Masala": "Spicy", "Ginger": "Zesty"}
# Adding a new key-value pair
# Syntax : Dic_Name[Key] = value
print(chai_types)
chai_types["Green"] = "Mild"
print(chai_types)
# Replacing value
chai_types["Green"] = "Good"
print(chai_types)
# key ke dwara value acces
print(chai_types["Ginger"])
# print(chai_types["Ginge"]) # not present throw error : KeyError

# Delete
print(chai_types)
del chai_types['Ginger']
print(chai_types)

"""

"""

# Built-in Functions with Dictionaries
# 1. len() - Returns the number of key-value pairs in the dictionary
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(len(chai_types))  # Output: 3
# 2. keys() - Returns a view object that displays a list of all the keys in the dictionary
print(chai_types.keys())  # Output: dict_keys(['Masala', 'Ginger', 'Green'])
# 3. values() - Returns a view object that displays a list of all the values in the dictionary
print(chai_types.values())  # Output: dict_values(['Spicy', 'Zesty', 'Mild'])
# 4. items() - Returns a view object that displays a list of dictionary's key-value tuple pairs
print(chai_types.items())  # Output: dict_items([('Masala', 'Spicy'), ('Ginger', 'Zesty'), ('Green', 'Mild')])
# 5. get() - Returns the value for the specified key if key is in dictionary, else None
print(chai_types.get("Ginger"))  # Output: Zesty
# 6. pop() - Removes the specified key and returns the corresponding value
print(chai_types.pop("Ginger"))  # Output: Zesty
# 7. popitem() - Removes and returns the last inserted key-value pair
print(chai_types.popitem())  # Output: ('Green', 'Mild')
# 8. clear() - Removes all the elements from the dictionary
chai_types.clear()
print(chai_types)  # Output: {}
# 9. copy() - Returns a shallow copy of the dictionary
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
chai_types_copy = chai_types.copy()
print(chai_types_copy)  # Output: {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
# 10. fromkeys() - Returns a new dictionary with keys from the given sequence and values set to a specified value
keys = ["Masala", "Ginger", "Green"]
default_value = "Unknown"
chai_types_fromkeys = dict.fromkeys(keys, default_value)
print(chai_types_fromkeys)  # Output: {'Masala': 'Unknown', 'Ginger': 'Unknown', 'Green': 'Unknown'}
# 11. update() - Updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs
chai_types.update({"Earl Gray": "Citrus", "Chamomile": "Floral"})
print(chai_types)  # Output: {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Earl Gray': 'Citrus', 'Chamomile': 'Floral'}

"""

# in, is, Identity vs Equality in Python Dictionaries
# 1. 'in' operator checks if a key exists in the dictionary
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print("Masala" in chai_types)  # Output: True
# 2. 'is' operator checks if two variables point to the same object in memory
chai_types1 = {"Masala": "Spicy", "Ginger": "Zesty"}
chai_types2 = chai_types1
print(chai_types1 is chai_types2)  # Output: True
# 3. '==' operator checks if two dictionaries have the same key-value pairs
print(chai_types1 == chai_types2)  # Output: True
# 4. 'is not' operator checks if two variables do not point to the same object in memory
chai_types3 = {"Masala": "Spicy", "Ginger": "Zesty"}
print(chai_types1 is not chai_types3)  # Output: True
# 5. '!=' operator checks if two dictionaries do not have the same key-value pairs
print(chai_types1 != chai_types3)  # Output: False
# 6. 'not in' operator checks if a key does not exist in the dictionary
print("Earl Gray" not in chai_types)  # Output: True



