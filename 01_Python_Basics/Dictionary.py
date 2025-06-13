chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green":"Mild"}
print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
print(chai_types["Ginger"]) # Zesty
# print(chai_types["ginger"]) # error - key error
# print(chai_types["Mild"]) # KeyError

print(chai_types.get("Masala")) # Spicy
print(chai_types.get("Zesty")) # None

# chai_types.get("Green") = "Fresh" # SyntaxError

chai_types["Green"] = "Fresh"
print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

# Use for loops in Dictionaries
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green":"Mild"}
for chai in chai_types:
    print(chai)
    
# Masala
# Ginger
# Green

for chai in chai_types:
    print(chai," - " + chai_types[chai])
    
# Masala  - Spicy
# Ginger  - Zesty
# Green  - Mild

# for key, value in chai_types: # ValueError
#     print(key,"- " + value) 

for key, value in chai_types.items():
    print(key,"- " + value)

# Masala - Spicy
# Ginger - Zesty
# Green - Mild
print(len(chai_types)) # 3

# Delete Method used

chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green":"Mild"}
chai_types["Earl Gray"] = "Citrus"
print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Earl Gray': 'Citrus'}
chai_types.pop("Green") # key
print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Earl Gray': 'Citrus'}
chai_types.popitem() # last item delete
# ('Earl Gray', 'Citrus')
print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty'}
del chai_types["Ginger"]
print(chai_types)

# Dictionay ke andar dictionary
tea_shop = {
    "chai": {'Masala': 'Spicy', 'Ginger': 'Zesty'},"tea": {"Green":"Mild",'Earl Gray': 'Citrus'} }
print(tea_shop)
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'tea': {'Green': 'Mild', 'Earl Gray': 'Citrus'}}
tea_shop["chai"]
#{'Masala': 'Spicy', 'Ginger': 'Zesty'}
tea_shop["chai"]["Ginger"] # 'Zesty'

#for loops 
squred_num = {x:x**2 for x in range(1,11)}
print(squred_num)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
cube_nums = {y:y**3 for y in range(1,11)}
print(cube_nums)
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}

squred_num.clear()
print(squred_num)

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys,default_value)
print(new_dict)
#{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
new_dict = dict.fromkeys(keys,keys)
print(new_dict)
#{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
