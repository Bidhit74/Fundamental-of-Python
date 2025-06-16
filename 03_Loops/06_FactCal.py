# Question: 06 - Factorial Calculate
# Statement: Compute the factorial of number using while loops

num = int(input("Enter the number: "))
fact = 1
while num>1:
    fact *= num
    num -= 1

print("Factorial = ", fact)