# Question:02 - Sum of even numbers
# Statement: Calculate the sum of even numbers up to a given numbers n.

nums = int(input("Enter the number: "))
sum = 0
for x in range(2, nums+1,2):
    sum += x

print("Sum of even numbers: ", sum)