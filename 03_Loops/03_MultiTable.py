# Question: 03 - Print the multiplication table for given number up to 10, but skip the fith iteration.

nums = int(input("Enter the number: "))

for i in range(1,11):
    if i == 5:
        continue
    print(i*nums)