# String Methods

# 🔹 1. upper(): Converts string to uppercase

msg = "hello"
print(msg.upper())  # HELLO

# 🔹 2. lower() Converts string to lowercase

msg = "HELLO"
print(msg.lower())  # hello

# 🔹 3. title() Capitalizes first letter of each word

text = "good morning"
print(text.title())  # Good Morning

# 🔹 4. strip() Removes extra spaces from start and end

name = "  Bidhit  "
print(name.strip())  # "Bidhit"

# 🔹 5. replace(old, new, count) Replaces part of the string with something else

text = "I like Java, Java, Java"
print(text.replace("Java", "Python"))  # I like Python Python Python
print(text.replace("Java", "Python",2))  # I like Python Python Java

# 🔹 6. split() Splits string into list of words

line = "Hello World Python"
print(line.split())  # ['Hello', 'World', 'Python'] # by default space split
line2 = "Hello-World-Python"
print(line2.split('-'))  # ['Hello', 'World', 'Python']

# 🔹 7. find() Returns the index of first occurrence

text = "Python is fun"
print(text.find("fun"))  # 10

# 🔹 8. startswith() / endswith() Checks if string starts or ends with specific text

msg = "hello world"
print(msg.startswith("hello"))  # True
print(msg.endswith("world"))    # True

# %s operator
name = "Bidhit"
print("Hello %s"%(name)) # Hello Bidhit

# Format Method
# syntax : template.format(p1,p2,....K1,k2....)
str1 = "{} plus {} equal {}".format(4,5,'Nine')
print(str1)
str2 = "My name is {0} and i from {1}".format("Bidhit","India")
str3 = "My name is {1} and i from {0}".format("Bidhit","India")
print(str2) #My name is Bidhit and i from India
print(str3) # My name is India and i from Bidhit

# check String Character - isalnum() , isalpha and isdigit()
s1 = "Bidhit"
s2 = "Bidhit123"
s3 = "123456@#%"
s4 = "123456"

# print(s1.isalnum()) # True
# print(s2.isalnum()) # True
# print(s3.isalnum()) # False
# print(s4.isalnum()) # True

# print(s1.isalpha()) # True
# print(s2.isalpha()) # False
# print(s3.isalpha()) # False
# print(s4.isalpha()) # False

# print(s1.isdigit()) # False
# print(s2.isdigit()) # False
# print(s3.isdigit()) # False
# print(s4.isdigit()) # True

# swapcase()	Converts lowercase to upper and vice versa

s1 = "BidhIt KUmaR"
print(s1.swapcase()) # bIDHiT kuMAr