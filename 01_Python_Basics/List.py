tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities[1])
print(tea_varities[1:3])
print(tea_varities[:3])
print(tea_varities[2:])
print(tea_varities[0:4:2])
tea_varities[3] = "Herbal"
print(tea_varities)
print(tea_varities[1:2])
tea_varities[1:2] = "lemon"
print(tea_varities)
tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)
tea_varities[1:2] = ["lemon"]
print(tea_varities)

print(tea_varities[1:1]) # []
tea_varities[1:1] = ["test1", "test2"]
print(tea_varities) # ['Black', 'test1', 'test2', 'lemon', 'Oolong', 'White']
print(tea_varities[1:3]) # ['test1', 'test2']
tea_varities[1:3] = [] # deletion operation perform hua hai
print(tea_varities)  # ['Black', 'lemon', 'Oolong', 'White']

for tea in tea_varities:
    print(tea)

for tea in tea_varities:
    print(tea, end=" ")

print("\n")

if "Oolong" in tea_varities:
    print("I have Oolong tea")

if "Oolonga" in tea_varities:
    print("I have Oolonga tea")


tea_varities = ["Black", "Green", "Oolong", "Herbal"]
tea_varities.append("Lemon")
print(tea_varities) # ['Black', 'Green', 'Oolong', 'Herbal', 'Lemon']
tea_varities.pop() # 'Lemon'
print(tea_varities) # ['Black', 'Green', 'Oolong', 'Herbal']

tea_varities.remove("Green")

print(tea_varities) # ['Black', 'Oolong', 'Herbal']

tea_varities.insert(0,"Lemon") # index, object
print(tea_varities) # ['Lemon', 'Black', 'Oolong', 'Herbal']

tea_varities = ["Black", "Green", "Oolong", "Herbal"]
tea_varities_copy = tea_varities.copy() # es tarah copy karne se dono ka alag alag reference banega
tea_varities_copy.append("Lemon")
print(tea_varities_copy)
# ['Black', 'Green', 'Oolong', 'Herbal', 'Lemon']
print(tea_varities)
# ['Black', 'Green', 'Oolong', 'Herbal']

# in list use for loops

print(range(10)) # range(0, 10)
squared_nums = [x ** 2 for x in range(10)]
print(squared_nums) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
cube_nums = [y**3 for y in range(11)]
print(cube_nums) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

cube_nums = [y**3 for y in range(5,12,2)] # range(start,stop,step)
print(cube_nums) # [125, 343, 729, 1331]