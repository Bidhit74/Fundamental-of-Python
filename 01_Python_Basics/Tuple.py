tea_types = ("Black", "Green", "Oolong")
print(tea_types[0] )# 'Black'
print(tea_types[-1]) # 'Oolong'
print(tea_types[1:]) # ('Green', 'Oolong')
# tea_types[0] = "Lemon" # TypeError: 'tuple' object does not support item assignment
print(len(tea_types)) # 3
more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print(all_tea) # ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')

# if use
if "Green" in all_tea:
    print("I have green tea")

more_tea = ("Herbal", "Earl Grey", "Herbal")
print(more_tea.count("Herbal"))\


print(tea_types)
(black,green,oolong) = tea_types # ek sath variable set
print(black)
print(green)
print(oolong)

print(type(tea_types)) # <class 'tuple'>