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

