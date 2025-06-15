# Question: 4 - Reverse String using loops

str = "tihdiB"  # Output - Bidhit
newStr = ""

# for i in range(0,len(str)):
#     newStr += str[len(str)-i-1]

# or

for char in str:
    newStr = char + newStr

print(newStr)
