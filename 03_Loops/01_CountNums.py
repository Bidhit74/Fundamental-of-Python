# Question:01 - Counting Positive Numbers
# Statement: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

nums = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0
for num in nums:
    if num>0:
        count += 1

print("Positive Numbers: " , count)