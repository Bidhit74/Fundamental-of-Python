# s1 = str() # create string using constructor
# s1 = str("Hello")
# print(type(s1))
# print(s1)
# other way create a string
# name = 'ZBidhixt' # or "Bidhit" # Both are String

# # In Buit function in python
# print(len(name)) # length of string # 6
# print(min(name)) # minimum character and uppre character in string 
# print(max(name)) # maximum character and lower latter in string


# Access the String
name = 'Bidhit'
print(name[0]) # first character
print(name[-1]) # End character

# Use for loop
for ch in name:
    print(ch,end=" ")

print()
# Use While loop

index = 0
while index < len(name):
    print(name[index], end=" ")
    index += 1

# Change String - but String is immutable 
name = 'ILovePython'
print(name)
# name[0] = 'U' # throw error - String is immutable 
# other way to change
name2 = "U" + name[1:]
print(name2)
# syntax: replace(old,new,count(optional))
str = "Lovely Professional Lovely Lovely Lovely"
print(str)
print(str.replace("Lovely","University")) # Har jagah yah change karega
# University Professional University University University
print(str.replace("Lovely","University",2)) # 2 jagah hi change karega
# University Professional University Lovely Lovely



