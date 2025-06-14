# Question 02: Movie Ticket Pricing
# Statement: Movie tickets are priced based on age:$12 for adults(18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter your age: "))
day= str(input("Today day name : "))

# if(age<18):
#     if(day=="Wednesday" or "wednesday"):
#         print("Today Movie Ticket Price: $6")
#     else:
#         print("Movie Ticket Price: $8")
# else:
#     if(day=="Wednesday" or "wednesday"):
#         print("Today Movie Ticket Price: $10")
#     else:
#         print("Movie Ticket Price: $12")

# or

price = 12 if age>=18 else 8

if day == "Wednesday":
    price -= 2
    
print("Movie ticket price for you: $",price)
