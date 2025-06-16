# Question - 05 : Given String, find the first non-repeated character.

str = input("Enter the Str: ")

for char in str:
    if(str.count(char)==1):
        print("Char is: " + char)
        break