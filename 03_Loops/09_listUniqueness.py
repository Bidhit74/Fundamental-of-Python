# Question 9:- List Uniqueness Checker
# Statement: Check if all element in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

# items = ["apple", "banana", "orange", "apple", "mango"] 

items = ["apple", "banana", "orange", "mango", "orange"] 

# for item in items:
#     if items.count(item)>1:
#         print("Duplicat item : " + item)
#         break

# another way solve
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicat item : " + item)
        break
    unique_item.add(item)

# print(unique_item)

