Name = "Bidhit"
print(Name)

first_char = Name[0]
print(first_char) # B

slice_name = Name[0:6]
print(slice_name) # Bidhit

slice_name = Name[0:5]
print(slice_name) # Bidhi
num_list = "0123456789"
num_slice = num_list[0:5]
print(num_slice) # 01234
print(Name.lower()) # bidhit
print(Name.upper()) # BIDHIT
name = "    Kumar Bidhit      "
print(name) #     Kumar Bidhit      
print(name.strip()) # Kumar Bidhit


Name = "Raj"
print(Name.replace("Raj", "Bidhit")) # Bidhit
print(Name) # 'Raj'
chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(", ")) # ['Lemon', 'Ginger', 'Masala', 'Mint']

print(chai.split()) # ['Lemon,', 'Ginger,', 'Masala,', 'Mint']

chai = "masala chai"
print(chai.find("chai")) # 7
print(chai.find("Chai")) # -1
chai = "masala chai chai chai"
print(chai.count("chai")) # 3
chai_type = "Masala"
quantity = 3
order = "I ordered {} cups of {} chai"
print(order) # I ordered {} cups of {} chai
print(order.format(quantity, chai_type)) # I ordered 3 cups of Masala chai

# convert list to string
chai_variety = ["Lemon", "Ginger", "Masala", "Mint"]
print(chai_variety) # ['Lemon', 'Ginger', 'Masala', 'Mint']
print("".join(chai_variety)) # LemonGingerMasalaMint
print(" ".join(chai_variety)) # Lemon Ginger Masala Mint
print(", ".join(chai_variety)) # Lemon, Ginger, Masala, Mint
print(chai)
print(len(chai))
chai = "Masala"
print(chai)
for letter in chai:
    print(letter)

# chai = "He said, "Masala chai is awesome" " # SyntaxError: invalid syntax
chai = "He said, \"Masala chai is awesome\" "
print(chai) # He said, "Masala chai is awesome" 

chai = "Masala\nChai"
print(chai)
#Masala
#Chai
chai = r"Masala\nChai" # row string
print(chai) # Masala\nChai

